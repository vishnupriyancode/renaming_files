"""
Postman Collection Generator - Generate Postman API collections from JSON files
Converts organized JSON files into Postman collections for API testing and validation
"""

import json
import os
import uuid
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


class PostmanCollectionGenerator:
    """Generate Postman API collections from organized JSON files."""
    
    def __init__(self, source_dir: str = "renaming_jsons", output_dir: str = "postman_collections"):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Postman collection structure template - minimal format for better compatibility
        self.collection_template = {
            "version": "1",
            "name": "",
            "type": "collection",
            "items": []
        }
    
    def _parse_filename(self, filename: str) -> Optional[Dict[str, str]]:
        """Parse Postman-style filename to extract test case information.
        
        Args:
            filename: Filename in format TC#ID#edit_id#eob_code#suffix.json
            
        Returns:
            Dictionary with parsed components or None if parsing fails
        """
        if not filename.endswith('.json'):
            return None
            
        name_without_ext = filename.replace('.json', '')
        
        if '#' in name_without_ext:
            parts = name_without_ext.split('#')
            if len(parts) == 5:
                return {
                    'tc_prefix': parts[0],  # TC
                    'tc_id': parts[1],      # 000001_53626
                    'edit_id': parts[2],    # rvn002
                    'eob_code': parts[3],   # 00W06
                    'suffix': parts[4],     # LR/NR/EX
                    'original_filename': filename
                }
        
        return None
    
    def _create_postman_request(self, json_file_path: Path, parsed_info: Dict[str, str]) -> Dict[str, Any]:
        """Create a Postman request from a JSON file.
        
        Args:
            json_file_path: Path to the JSON file
            parsed_info: Parsed filename information
            
        Returns:
            Postman request structure
        """
        # Read JSON content
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                json_content = json.load(f)
        except Exception as e:
            print(f"Warning: Could not read {json_file_path}: {e}")
            json_content = {}
        
        # Create request name based on actual filename (without .json extension)
        request_name = json_file_path.stem  # This gets the filename without extension
        
        # Determine HTTP method based on suffix
        method_map = {
            'LR': 'POST',  # Limited Response - POST for validation
            'NR': 'POST',  # No Response - POST for validation
            'EX': 'POST'   # Exception - POST for validation
        }
        method = method_map.get(parsed_info['suffix'], 'POST')
        
        # Create Postman request structure - ultra-minimal format
        request = {
            "uid": str(uuid.uuid4()),
            "name": request_name,
            "type": "http",
            "method": method,
            "url": "{{baseUrl}}/api/validate/{{tc_id}}",
            "headers": [
                {
                    "uid": str(uuid.uuid4()),
                    "name": "Content-Type",
                    "value": "application/json",
                    "enabled": True
                },
                {
                    "uid": str(uuid.uuid4()),
                    "name": "X-Edit-ID",
                    "value": parsed_info['edit_id'],
                    "enabled": True
                },
                {
                    "uid": str(uuid.uuid4()),
                    "name": "X-EOB-Code",
                    "value": parsed_info['eob_code'],
                    "enabled": True
                },
                {
                    "uid": str(uuid.uuid4()),
                    "name": "X-Test-Type",
                    "value": parsed_info['suffix'],
                    "enabled": True
                }
            ],
            "body": {
                "mode": "raw",
                "raw": json.dumps(json_content, indent=2)
            }
        }
        
        return request
    
    
    def generate_postman_collection(self, collection_name: str = "TestCollection", custom_filename: str = None) -> Optional[Path]:
        """Generate Postman-compatible collection for JSON files in source directory.
        
        Args:
            collection_name: Name of the collection to generate
            
        Returns:
            Path to generated Postman collection file or None if no files found
        """
        if not self.source_dir.exists():
            print(f"Source directory '{self.source_dir}' not found")
            return None
        
        # Find all JSON files in the source directory and subdirectories
        json_files = []
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                if file.endswith('.json'):
                    json_files.append(Path(root) / file)
        
        if not json_files:
            print(f"No JSON files found in '{self.source_dir}'")
            return None
        
        print(f"Found {len(json_files)} JSON files for collection '{collection_name}'")
        
        # Create Postman collection structure
        postman_collection = {
            "info": {
                "name": f"{collection_name} API Collection",
                "description": f"API collection for {collection_name} test cases",
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": [],
            "variable": [
                {
                    "key": "baseUrl",
                    "value": "http://localhost:3000",
                    "type": "string"
                }
            ]
        }
        
        # Parse files and create requests
        for json_file in json_files:
            parsed_info = self._parse_filename(json_file.name)
            if parsed_info:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        json_content = json.load(f)
                except Exception as e:
                    print(f"Warning: Could not read {json_file}: {e}")
                    json_content = {}
                
                # Determine HTTP method based on suffix
                method_map = {
                    'LR': 'POST',
                    'NR': 'POST',
                    'EX': 'POST'
                }
                method = method_map.get(parsed_info['suffix'], 'POST')
                
                # Create Postman request - use the actual filename (without .json extension)
                request_name = json_file.stem  # This gets the filename without extension
                
                postman_request = {
                    "name": request_name,
                    "request": {
                        "method": method,
                        "header": [
                            {
                                "key": "Content-Type",
                                "value": "application/json",
                                "type": "text"
                            },
                            {
                                "key": "X-Edit-ID",
                                "value": parsed_info['edit_id'],
                                "type": "text"
                            },
                            {
                                "key": "X-EOB-Code",
                                "value": parsed_info['eob_code'],
                                "type": "text"
                            },
                            {
                                "key": "X-Test-Type",
                                "value": parsed_info['suffix'],
                                "type": "text"
                            }
                        ],
                        "url": {
                            "raw": "{{baseUrl}}/api/validate/{{tc_id}}",
                            "host": ["{{baseUrl}}"],
                            "path": ["api", "validate", "{{tc_id}}"]
                        },
                        "body": {
                            "mode": "raw",
                            "raw": json.dumps(json_content, indent=2),
                            "options": {
                                "raw": {
                                    "language": "json"
                                }
                            }
                        }
                    }
                }
                
                postman_collection["item"].append(postman_request)
        
        if not postman_collection["item"]:
            print(f"No valid requests could be created for collection '{collection_name}'")
            return None
        
        # Save Postman collection file
        collection_dir = self.output_dir / collection_name
        collection_dir.mkdir(exist_ok=True)
        
        # Use custom filename if provided, otherwise use default
        filename = custom_filename if custom_filename else "postman_collection.json"
        postman_file = collection_dir / filename
        
        try:
            with open(postman_file, 'w', encoding='utf-8') as f:
                json.dump(postman_collection, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Generated Postman collection: {postman_file}")
            print(f"   - Collection: {collection_name}")
            print(f"   - Requests: {len(postman_collection['item'])}")
            print(f"   - Files processed: {len(json_files)}")
            
            return postman_file
            
        except Exception as e:
            print(f"❌ Error saving Postman collection for {collection_name}: {e}")
            return None

    def generate_collection_for_directory(self, dir_name: str) -> Optional[Path]:
        """Generate Postman collection for a specific directory.
        
        Args:
            dir_name: Name of the directory to generate collection for
            
        Returns:
            Path to generated collection file or None if no files found
        """
        dir_path = self.source_dir / dir_name
        
        if not dir_path.exists():
            print(f"Directory '{dir_path}' not found")
            return None
        
        # Find all JSON files in the directory
        json_files = list(dir_path.glob("**/*.json"))
        
        if not json_files:
            print(f"No JSON files found in '{dir_path}'")
            return None
        
        print(f"Found {len(json_files)} JSON files for directory '{dir_name}'")
        
        # Parse files and create requests
        requests = []
        for json_file in json_files:
            parsed_info = self._parse_filename(json_file.name)
            if parsed_info:
                request = self._create_postman_request(json_file, parsed_info)
                requests.append(request)
            else:
                print(f"Warning: Could not parse filename '{json_file.name}'")
        
        if not requests:
            print(f"No valid requests could be created for directory '{dir_name}'")
            return None
        
        # Create collection structure - minimal format
        collection = self.collection_template.copy()
        collection["name"] = f"{dir_name} API Collection"
        collection["items"] = requests
        
        # Create Postman collection directory structure
        collection_dir = self.output_dir / f"{dir_name.lower().replace(' ', '_')}_collection"
        collection_dir.mkdir(exist_ok=True)
        
        # Save collection.json file
        collection_file = collection_dir / "collection.json"
        
        try:
            with open(collection_file, 'w', encoding='utf-8') as f:
                json.dump(collection, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Generated Postman collection: {collection_file}")
            print(f"   - Directory: {dir_name}")
            print(f"   - Requests: {len(requests)}")
            print(f"   - Files processed: {len(json_files)}")
            print(f"   - Collection directory: {collection_dir}")
            
            return collection_file
            
        except Exception as e:
            print(f"❌ Error saving collection for {dir_name}: {e}")
            return None
    
    def generate_all_collections(self) -> Dict[str, Path]:
        """Generate a single Postman collection for all JSON files in source directory.
        Collection name is extracted from the directory structure.
        
        Returns:
            Dictionary with single collection entry
        """
        collections = {}
        
        if not self.source_dir.exists():
            print(f"Source directory '{self.source_dir}' not found")
            return collections
        
        # Extract collection name from directory structure
        collection_name = "TS_01_REVENUE_WGS_CSBD_rvn001_00W5"
        
        # Look for directories that match the pattern TS_*_payloads_dis
        for item in self.source_dir.iterdir():
            if item.is_dir() and item.name.startswith("TS_") and "_payloads_dis" in item.name:
                # Extract collection name by removing "_payloads_dis" suffix
                collection_name = item.name.replace("_payloads_dis", "")
                break
        
        # Generate a single collection for all files
        print(f"Generating collection '{collection_name}' for all files...")
        collection_path = self.generate_postman_collection(collection_name)
        
        if collection_path:
            collections[collection_name] = collection_path
        
        return collections
    
    def list_available_directories(self) -> List[str]:
        """List all available directories in the source directory.
        
        Returns:
            List of directory names
        """
        if not self.source_dir.exists():
            return []
        
        dirs = [d.name for d in self.source_dir.iterdir() if d.is_dir()]
        return sorted(dirs)
    
    def get_directory_stats(self, dir_name: str) -> Dict[str, Any]:
        """Get statistics for a specific directory.
        
        Args:
            dir_name: Name of the directory
            
        Returns:
            Dictionary containing directory statistics
        """
        dir_path = self.source_dir / dir_name
        
        if not dir_path.exists():
            return {"error": f"Directory '{dir_path}' not found"}
        
        json_files = list(dir_path.glob("**/*.json"))
        
        stats = {
            "directory_name": dir_name,
            "total_files": len(json_files),
            "file_types": {},
            "edit_ids": set(),
            "eob_codes": set(),
            "suffixes": set()
        }
        
        for json_file in json_files:
            parsed_info = self._parse_filename(json_file.name)
            if parsed_info:
                suffix = parsed_info['suffix']
                stats["file_types"][suffix] = stats["file_types"].get(suffix, 0) + 1
                stats["edit_ids"].add(parsed_info['edit_id'])
                stats["eob_codes"].add(parsed_info['eob_code'])
                stats["suffixes"].add(suffix)
        
        # Convert sets to lists for JSON serialization
        stats["edit_ids"] = list(stats["edit_ids"])
        stats["eob_codes"] = list(stats["eob_codes"])
        stats["suffixes"] = list(stats["suffixes"])
        
        return stats
    
    def validate_collection(self, collection_path: Path) -> Dict[str, Any]:
        """Validate a Postman collection file.
        
        Args:
            collection_path: Path to the collection file
            
        Returns:
            Dictionary containing validation results
        """
        validation_result = {
            "valid": False,
            "errors": [],
            "warnings": [],
            "stats": {}
        }
        
        try:
            with open(collection_path, 'r', encoding='utf-8') as f:
                collection = json.load(f)
            
            # Check for Postman v2.1.0 format first
            if "info" in collection and "item" in collection:
                # Postman v2.1.0 format
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
                # Minimal format
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
    """Main function for standalone execution."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate Postman collections from JSON files")
    parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    parser.add_argument("--output-dir", default="postman_collections", help="Output directory for Postman collections")
    parser.add_argument("--collection-name", default="TestCollection", help="Name for the collection")
    parser.add_argument("--directory", help="Generate collection for specific directory")
    parser.add_argument("--list-directories", action="store_true", help="List available directories")
    parser.add_argument("--stats", help="Show statistics for specific directory")
    
    args = parser.parse_args()
    
    generator = PostmanCollectionGenerator(args.source_dir, args.output_dir)
    
    if args.list_directories:
        directories = generator.list_available_directories()
        if directories:
            print("Available directories:")
            for directory in directories:
                print(f"  - {directory}")
        else:
            print("No directories found")
    
    elif args.stats:
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
        collection_path = generator.generate_collection_for_directory(args.directory)
        if collection_path:
            print(f"Collection generated: {collection_path}")
        else:
            print("Failed to generate collection")
    
    else:
        collection_path = generator.generate_postman_collection(args.collection_name)
        if collection_path:
            print(f"Collection generated: {collection_path}")
        else:
            print("Failed to generate collection")


if __name__ == "__main__":
    main()
