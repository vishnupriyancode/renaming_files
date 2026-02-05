"""
Postman Collection Generator - Generate Postman API collections from JSON files
Converts organized JSON files into Postman collections for API testing and validation

STAGE 1: IMPORTS AND DEPENDENCIES
- json: For reading/writing JSON files and data manipulation
- os: For file system operations and directory walking
- re: For regular expressions to parse directory names and patterns
- uuid: For generating unique identifiers for Postman requests
- pathlib.Path: For cross-platform file path handling
- typing: For type hints to improve code clarity and IDE support
- datetime: For timestamp generation (though not actively used in current implementation)
"""

import json
import os
import re
import uuid
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


class PostmanCollectionGenerator:
    """Generate Postman API collections from organized JSON files."""
    
    def __init__(self, source_dir: str = "renaming_jsons", output_dir: str = "postman_collections"):
        """
        STAGE 2: CLASS INITIALIZATION
        - Sets up source directory (where JSON files are located)
        - Sets up output directory (where Postman collections will be saved)
        - Creates output directory if it doesn't exist
        - Defines minimal Postman collection template structure
        """
        self.source_dir = Path(source_dir)  # Convert to Path object for better file handling
        self.output_dir = Path(output_dir)  # Convert to Path object for better file handling
        self.output_dir.mkdir(exist_ok=True)  # Create output directory if it doesn't exist
        
        # Postman collection structure template - minimal format for better compatibility
        # This template defines the basic structure that all generated collections will follow
        self.collection_template = {
            "version": "1",           # Collection version identifier
            "name": "",               # Collection name (will be set dynamically)
            "type": "collection",     # Postman collection type
            "items": []               # Array to hold individual API requests
        }
    
    def _parse_filename(self, filename: str) -> Optional[Dict[str, str]]:
        """
        STAGE 3: FILENAME PARSING
        Parse Postman-style filename to extract test case information.
        Expected format: TC#ID#edit_id#eob_code#suffix.json
        
        Args:
            filename: Filename in format TC#ID#edit_id#eob_code#suffix.json
            
        Returns:
            Dictionary with parsed components or None if parsing fails
        """
        # Step 3.1: Validate file extension
        if not filename.endswith('.json'):
            return None
            
        # Step 3.2: Remove file extension for parsing
        name_without_ext = filename.replace('.json', '')
        
        # Step 3.3: Check if filename contains hash separators
        if '#' in name_without_ext:
            parts = name_without_ext.split('#')
            # Step 3.4: Validate that we have exactly 5 parts (TC#ID#edit_id#eob_code#suffix)
            if len(parts) == 5:
                return {
                    'tc_prefix': parts[0],  # TC (Test Case prefix)
                    'tc_id': parts[1],      # 000001_53626 (Test Case ID)
                    'edit_id': parts[2],    # rvn002 (Edit identifier)
                    'eob_code': parts[3],   # 00W06 (EOB code)
                    'suffix': parts[4],     # LR/NR/EX (Response type suffix)
                    'original_filename': filename  # Keep original for reference
                }
        
        return None
    
    def _get_headers(self, is_gbdf_model: bool, format_type: str = "v2.1.0") -> List[Dict]:
        """
        Get headers for Postman request based on model type.
        
        Args:
            is_gbdf_model: Whether this is a GBDF model
            format_type: Postman format type ("v2.1.0" or "minimal")
            
        Returns:
            List of header dictionaries
        """
        if is_gbdf_model:
            if format_type == "v2.1.0":
                return [{"key": "Client_Transaction_ID", "value": "20115660390020220225161114893", "type": "text"}]
            else:
                return [{"uid": str(uuid.uuid4()), "name": "Client_Transaction_ID", "value": "20115660390020220225161114893", "enabled": True}]
        else:
            if format_type == "v2.1.0":
                return [
                    {"key": "Content-Type", "value": "application/json", "type": "text"},
                    {"key": "meta-transid", "value": "20220117181853TMBL20359Cl893580999", "type": "text"},
                    {"key": "meta-src-envrmt", "value": "IMSH", "type": "text"}
                ]
            else:
                return [
                    {"uid": str(uuid.uuid4()), "name": "Content-Type", "value": "application/json", "enabled": True},
                    {"uid": str(uuid.uuid4()), "name": "meta-transid", "value": "20220117181853TMBL20359Cl893580999", "enabled": True},
                    {"uid": str(uuid.uuid4()), "name": "meta-src-envrmt", "value": "IMSH", "enabled": True}
                ]
    
    def _create_postman_request(self, json_file_path: Path, parsed_info: Dict[str, str], is_gbdf_model: bool = False) -> Dict[str, Any]:
        """
        STAGE 4: POSTMAN REQUEST CREATION
        Create a Postman request from a JSON file with proper structure and headers.
        
        Args:
            json_file_path: Path to the JSON file
            parsed_info: Parsed filename information
            is_gbdf_model: Whether this is a GBDF model (affects headers)
            
        Returns:
            Postman request structure
        """
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                json_content = json.load(f)
        except Exception as e:
            print(f"Warning: Could not read {json_file_path}: {e}")
            json_content = {}
        
        method = {'LR': 'POST', 'NR': 'POST', 'EX': 'POST'}.get(parsed_info['suffix'], 'POST')
        
        return {
            "uid": str(uuid.uuid4()),
            "name": json_file_path.stem,
            "type": "http",
            "method": method,
            "url": "https://pi-timber-claims-api-uat.ingress-nginx.dig-gld-shared.gcpdns.internal.das/claims/Timber/GetRecommendations",
            "headers": self._get_headers(is_gbdf_model, "minimal"),
            "body": {"mode": "raw", "raw": json.dumps(json_content, indent=2)}
        }
    
    
    def generate_postman_collection(self, collection_name: str = "TestCollection", custom_filename: str = None, is_gbdf_model: bool = False) -> Optional[Path]:
        """
        STAGE 5: MAIN COLLECTION GENERATION
        Generate Postman-compatible collection for JSON files in source directory.
        This is the primary method that orchestrates the entire collection creation process.
        
        Args:
            collection_name: Name of the collection to generate
            custom_filename: Optional custom filename for the collection file
            is_gbdf_model: Whether this is a GBDF model (affects headers)
            
        Returns:
            Path to generated Postman collection file or None if no files found
        """
        # Step 5.1: Validate source directory exists
        if not self.source_dir.exists():
            print(f"Source directory '{self.source_dir}' not found")
            return None
        
        # Step 5.2: Find all JSON files in the source directory and subdirectories
        json_files = []
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                if file.endswith('.json'):
                    json_files.append(Path(root) / file)
        
        if not json_files:
            print(f"No JSON files found in '{self.source_dir}'")
            return None
        
        print(f"Found {len(json_files)} JSON files for collection '{collection_name}'")
        
        # Step 5.3: Create Postman collection structure (v2.1.0 format)
        postman_collection = {
            "info": {
                "name": f"{collection_name} API Collection",
                "description": f"API collection for {collection_name} test cases",
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": [],  # Array to hold all API requests
            "variable": [  # Collection-level variables
                {
                    "key": "baseUrl",
                    "value": "http://localhost:3000",  # Default base URL
                    "type": "string"
                }
            ]
        }
        
        # Step 5.4: Parse files and create requests
        for json_file in json_files:
            parsed_info = self._parse_filename(json_file.name)
            if parsed_info:
                # Step 5.4.1: Read JSON content from file
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        json_content = json.load(f)
                except Exception as e:
                    print(f"Warning: Could not read {json_file}: {e}")
                    json_content = {}
                
                # Step 5.4.2: Determine HTTP method based on suffix
                # Mapping for suffixes based on the expected output format
                method_map = {
                    'LR': 'POST',  # Limited Response - POST for validation
                    'NR': 'POST',  # No Response - POST for validation
                    'EX': 'POST'   # Exception - POST for validation
                }
                method = method_map.get(parsed_info['suffix'], 'POST')
                
                # Step 5.4.3: Create Postman request - use the actual filename (without .json extension)
                # Step 5.4.4: Build Postman request structure (v2.1.0 format)
                postman_request = {
                    "name": json_file.stem,
                    "request": {
                        "method": method,
                        "header": self._get_headers(is_gbdf_model, "v2.1.0"),
                        "url": {
                            "raw": "https://pi-timber-claims-api-uat.ingress-nginx.dig-gld-shared.gcpdns.internal.das/claims/Timber/GetRecommendations",
                            "host": ["{{baseUrl}}"],
                            "path": ["api", "validate", "{{tc_id}}"]
                        },
                        "body": {
                            "mode": "raw",
                            "raw": json.dumps(json_content, indent=2),
                            "options": {"raw": {"language": "json"}}
                        }
                    }
                }
                
                # Step 5.4.5: Add request to collection
                postman_collection["item"].append(postman_request)
        
        # Step 5.5: Validate that we have requests to save
        if not postman_collection["item"]:
            print(f"No valid requests could be created for collection '{collection_name}'")
            return None
        
        # Step 5.6: Save Postman collection file
        collection_dir = self.output_dir / collection_name
        collection_dir.mkdir(exist_ok=True)
        
        # Step 5.7: Use custom filename if provided, otherwise use default
        filename = custom_filename if custom_filename else "postman_collection.json"
        postman_file = collection_dir / filename
        
        try:
            # Step 5.8: Write collection to JSON file
            with open(postman_file, 'w', encoding='utf-8') as f:
                json.dump(postman_collection, f, indent=2, ensure_ascii=False)
            
            # Step 5.9: Print success information
            print(f"SUCCESS: Generated Postman collection: {postman_file}")
            print(f"   - Collection: {collection_name}")
            print(f"   - Requests: {len(postman_collection['item'])}")
            print(f"   - Files processed: {len(json_files)}")
            
            return postman_file
            
        except Exception as e:
            print(f"ERROR: Error saving Postman collection for {collection_name}: {e}")
            return None

    def generate_collection_for_directory(self, dir_name: str, is_gbdf_model: bool = False) -> Optional[Path]:
        """
        STAGE 6: DIRECTORY-SPECIFIC COLLECTION GENERATION
        Generate Postman collection for a specific directory using minimal format.
        This method creates collections for individual directories with smart naming.
        
        Args:
            dir_name: Name of the directory to generate collection for
            is_gbdf_model: Whether this is a GBDF model (affects headers)
            
        Returns:
            Path to generated collection file or None if no files found
        """
        # Step 6.1: Validate directory exists
        dir_path = self.source_dir / dir_name
        
        if not dir_path.exists():
            print(f"Directory '{dir_path}' not found")
            return None
        
        # Step 6.2: Find all JSON files in the directory and subdirectories
        json_files = list(dir_path.glob("**/*.json"))
        
        if not json_files:
            print(f"No JSON files found in '{dir_path}'")
            return None
        
        print(f"Found {len(json_files)} JSON files for directory '{dir_name}'")
        
        # Step 6.3: Parse files and create requests using minimal format
        requests = []
        for json_file in json_files:
            parsed_info = self._parse_filename(json_file.name)
            if parsed_info:
                request = self._create_postman_request(json_file, parsed_info, is_gbdf_model)
                requests.append(request)
            else:
                print(f"Warning: Could not parse filename '{json_file.name}'")
        
        if not requests:
            print(f"No valid requests could be created for directory '{dir_name}'")
            return None
        
        # Step 6.4: Create collection structure - minimal format
        collection = self.collection_template.copy()
        collection["name"] = f"{dir_name} API Collection"
        collection["items"] = requests
        
        # Step 6.5: Create Postman collection directory structure with flexible naming
        # Extract TS number from directory name for consistent naming
        # Handle CSBDTS_ prefix first, then TS_ prefix
        csbdts_match = re.match(r'CSBDTS_(\d{1,3})_(.+?)_WGS_CSBD_', dir_name)
        if csbdts_match:
            ts_number = csbdts_match.group(1)
            model_name = csbdts_match.group(2)
            # Use the model name to create proper collection name
            if "AntepartumServices" in model_name:
                collection_dir_name = f"CSBDTS_{ts_number}_AntepartumServices_Collection"
            elif "Observation_Services" in model_name:
                collection_dir_name = f"CSBDTS_{ts_number}_Observation_Services_Collection"
            else:
                # Fallback: use directory name pattern
                collection_dir_name = f"CSBDTS_{ts_number}_{model_name}_Collection"
        else:
            ts_match = re.match(r'TS_(\d{1,3})_', dir_name)
            if ts_match:
                ts_number = ts_match.group(1)
                collection_dir_name = f"TS_{ts_number}_collection"
            else:
                collection_dir_name = f"{dir_name.replace(' ', '_')}_collection"
        
        collection_dir = self.output_dir / collection_dir_name
        collection_dir.mkdir(parents=True, exist_ok=True)
        
        # Step 6.6: Save collection.json file
        collection_file = collection_dir / "collection.json"
        
        try:
            with open(collection_file, 'w', encoding='utf-8') as f:
                json.dump(collection, f, indent=2, ensure_ascii=False)
            
            print(f"SUCCESS: Generated Postman collection: {collection_file}")
            print(f"   - Directory: {dir_name}")
            print(f"   - Requests: {len(requests)}")
            print(f"   - Files processed: {len(json_files)}")
            print(f"   - Collection directory: {collection_dir}")
            
            return collection_file
            
        except Exception as e:
            print(f"ERROR: Error saving collection for {dir_name}: {e}")
            return None
    
    def generate_all_collections(self) -> Dict[str, Path]:
        """
        STAGE 7: BULK COLLECTION GENERATION
        Generate a single Postman collection for all JSON files in source directory.
        Collection name is extracted from the directory structure automatically.
        
        Returns:
            Dictionary with single collection entry
        """
        collections = {}
        
        # Step 7.1: Validate source directory exists
        if not self.source_dir.exists():
            print(f"Source directory '{self.source_dir}' not found")
            return collections
        
        # Step 7.2: Extract collection name from directory structure
        collection_name = "TS_01_REVENUE_WGS_CSBD_rvn001_00W5"  # Default fallback name
        
        # Step 7.3: Look for directories that match the pattern TS_*_payloads_dis
        for item in self.source_dir.iterdir():
            if item.is_dir() and item.name.startswith("TS_") and "_payloads_dis" in item.name:
                # Extract collection name by removing "_payloads_dis" suffix
                collection_name = item.name.replace("_payloads_dis", "")
                break
        
        # Step 7.4: Generate a single collection for all files
        print(f"Generating collection '{collection_name}' for all files...")
        collection_path = self.generate_postman_collection(collection_name)
        
        if collection_path:
            collections[collection_name] = collection_path
        
        return collections
    
    def list_available_directories(self) -> List[str]:
        """
        STAGE 8: DIRECTORY LISTING UTILITY
        List all available directories in the source directory for user selection.
        
        Returns:
            List of directory names sorted alphabetically
        """
        if not self.source_dir.exists():
            return []
        
        # Get all directory names and sort them for consistent output
        dirs = [d.name for d in self.source_dir.iterdir() if d.is_dir()]
        return sorted(dirs)
    
    def get_directory_stats(self, dir_name: str) -> Dict[str, Any]:
        """
        STAGE 9: DIRECTORY STATISTICS ANALYSIS
        Get comprehensive statistics for a specific directory including file counts and metadata.
        
        Args:
            dir_name: Name of the directory to analyze
            
        Returns:
            Dictionary containing directory statistics
        """
        # Step 9.1: Validate directory exists
        dir_path = self.source_dir / dir_name
        
        if not dir_path.exists():
            return {"error": f"Directory '{dir_path}' not found"}
        
        # Step 9.2: Find all JSON files in directory and subdirectories
        json_files = list(dir_path.glob("**/*.json"))
        
        # Step 9.3: Initialize statistics structure
        stats = {
            "directory_name": dir_name,
            "total_files": len(json_files),
            "file_types": {},      # Count of files by suffix (LR, NR, EX)
            "edit_ids": set(),     # Unique edit identifiers
            "eob_codes": set(),    # Unique EOB codes
            "suffixes": set()      # Unique suffixes found
        }
        
        # Step 9.4: Analyze each JSON file
        for json_file in json_files:
            parsed_info = self._parse_filename(json_file.name)
            if parsed_info:
                suffix = parsed_info['suffix']
                # Count files by type (suffix)
                stats["file_types"][suffix] = stats["file_types"].get(suffix, 0) + 1
                # Collect unique identifiers
                stats["edit_ids"].add(parsed_info['edit_id'])
                stats["eob_codes"].add(parsed_info['eob_code'])
                stats["suffixes"].add(suffix)
        
        # Step 9.5: Convert sets to lists for JSON serialization
        stats["edit_ids"] = list(stats["edit_ids"])
        stats["eob_codes"] = list(stats["eob_codes"])
        stats["suffixes"] = list(stats["suffixes"])
        
        return stats
    
    def validate_collection(self, collection_path: Path) -> Dict[str, Any]:
        """
        STAGE 10: COLLECTION VALIDATION
        Validate a Postman collection file to ensure it meets required format standards.
        Supports both Postman v2.1.0 format and minimal format validation.
        
        Args:
            collection_path: Path to the collection file to validate
            
        Returns:
            Dictionary containing validation results with errors, warnings, and stats
        """
        # Step 10.1: Initialize validation result structure
        validation_result = {
            "valid": False,
            "errors": [],
            "warnings": [],
            "stats": {}
        }
        
        try:
            # Step 10.2: Read and parse JSON collection file
            with open(collection_path, 'r', encoding='utf-8') as f:
                collection = json.load(f)
            
            # Step 10.3: Check for Postman v2.1.0 format first
            if "info" in collection and "item" in collection:
                # Postman v2.1.0 format validation
                required_fields = ["info", "item"]
                for field in required_fields:
                    if field not in collection:
                        validation_result["errors"].append(f"Missing required field: {field}")
                
                # Check collection structure
                if "item" in collection and isinstance(collection["item"], list):
                    total_requests = len(collection["item"])
                    validation_result["stats"]["total_requests"] = total_requests
                
                # Check if collection has requests
                if validation_result["stats"].get("total_requests", 0) == 0:
                    validation_result["warnings"].append("Collection contains no requests")
                
                # If no errors, mark as valid
                if not validation_result["errors"]:
                    validation_result["valid"] = True
                    
            else:
                # Step 10.4: Minimal format validation
                required_fields = ["version", "name", "type", "items"]
                for field in required_fields:
                    if field not in collection:
                        validation_result["errors"].append(f"Missing required field: {field}")
                
                # Check collection structure
                if "items" in collection and isinstance(collection["items"], list):
                    total_requests = len(collection["items"])
                    validation_result["stats"]["total_requests"] = total_requests
                
                # Check if collection has requests
                if validation_result["stats"].get("total_requests", 0) == 0:
                    validation_result["warnings"].append("Collection contains no requests")
                
                # If no errors, mark as valid
                if not validation_result["errors"]:
                    validation_result["valid"] = True
            
        except json.JSONDecodeError as e:
            validation_result["errors"].append(f"Invalid JSON format: {e}")
        except Exception as e:
            validation_result["errors"].append(f"Validation error: {e}")
        
        return validation_result


def main():
    """
    STAGE 11: COMMAND LINE INTERFACE
    Main function for standalone execution with comprehensive CLI options.
    Provides multiple ways to interact with the Postman collection generator.
    """
    import argparse
    
    # Step 11.1: Set up command line argument parser
    parser = argparse.ArgumentParser(description="Generate Postman collections from JSON files")
    parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    parser.add_argument("--output-dir", default="postman_collections", help="Output directory for Postman collections")
    parser.add_argument("--collection-name", default="TestCollection", help="Name for the collection")
    parser.add_argument("--directory", help="Generate collection for specific directory")
    parser.add_argument("--list-directories", action="store_true", help="List available directories")
    parser.add_argument("--stats", help="Show statistics for specific directory")
    
    args = parser.parse_args()
    
    # Step 11.2: Initialize the generator with command line arguments
    generator = PostmanCollectionGenerator(args.source_dir, args.output_dir)
    
    # Step 11.3: Handle different command line options
    if args.list_directories:
        # List all available directories in source folder
        directories = generator.list_available_directories()
        if directories:
            print("Available directories:")
            for directory in directories:
                print(f"  - {directory}")
        else:
            print("No directories found")
    
    elif args.stats:
        # Show detailed statistics for a specific directory
        stats = generator.get_directory_stats(args.stats)
        if "error" in stats:
            print(f"Error: {stats['error']}")
        else:
            print(f"Statistics for {args.stats}:")
            print(f"  Total files: {stats['total_files']}")
            print(f"  File types: {stats['file_types']}")
            print(f"  Edit IDs: {stats['edit_ids']}")
            print(f"  EOB Codes: {stats['eob_codes']}")
            print(f"  Suffixes: {stats['suffixes']}")
    
    elif args.directory:
        # Generate collection for a specific directory
        collection_path = generator.generate_collection_for_directory(args.directory)
        if collection_path:
            print(f"Collection generated: {collection_path}")
        else:
            print("Failed to generate collection")
    
    else:
        # Default: Generate collection for all files with specified name
        collection_path = generator.generate_postman_collection(args.collection_name)
        if collection_path:
            print(f"Collection generated: {collection_path}")
        else:
            print("Failed to generate collection")


if __name__ == "__main__":
    """
    STAGE 12: SCRIPT EXECUTION ENTRY POINT
    This is the entry point when the script is run directly from command line.
    It calls the main() function which handles all CLI operations.
    """
    main()
