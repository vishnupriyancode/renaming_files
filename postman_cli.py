#!/usr/bin/env python3
"""
Postman Collection CLI - Command Line Interface for generating Postman collections
from renamed JSON files in the renaming_postman_collection project
"""

# Stage 1: Import required modules
import argparse  # For command-line argument parsing
import sys      # For system-specific parameters and functions
import os       # For operating system interface
from pathlib import Path  # For object-oriented filesystem paths

# Import the Postman generator - main class that handles collection generation
from postman_generator import PostmanCollectionGenerator


def main():
    # Stage 2: Setup argument parser with help text and examples
    parser = argparse.ArgumentParser(
        description="Postman Collection Generator for renaming_postman_collection project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Generate Postman collection for all JSON files
    python postman_cli.py generate --collection-name "RevenueTestCollection"
    
    # Generate collection for specific directory
    python postman_cli.py generate --directory "renaming_jsons/CSBDTS/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"
    
    # List available directories
    python postman_cli.py list-directories
    
    # Show statistics for a directory
    python postman_cli.py stats --directory "renaming_jsons/CSBDTS/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"
    
    # Generate collections for all directories
    python postman_cli.py generate-all
    
    # Validate a collection
    python postman_cli.py validate --collection-path "postman_collections/test_collection/postman_collection.json"
        """
    )
    
    # Stage 3: Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Stage 4: Define 'generate' command - creates collection from JSON files
    generate_parser = subparsers.add_parser("generate", help="Generate Postman collection")
    generate_parser.add_argument("--collection-name", default="TestCollection", help="Name for the collection")
    generate_parser.add_argument("--directory", help="Generate collection for specific directory")
    generate_parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    generate_parser.add_argument("--output-dir", default="postman_collections", help="Output directory for Postman collections")
    
    # Stage 5: Define 'generate-all' command - processes all directories at once
    generate_all_parser = subparsers.add_parser("generate-all", help="Generate collections for all directories")
    generate_all_parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    generate_all_parser.add_argument("--output-dir", default="postman_collections", help="Output directory for Postman collections")
    
    # Stage 6: Define 'list-directories' command - shows available directories
    list_dirs_parser = subparsers.add_parser("list-directories", help="List available directories")
    list_dirs_parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    
    # Stage 7: Define 'stats' command - shows statistics for a specific directory
    stats_parser = subparsers.add_parser("stats", help="Show statistics for a directory")
    stats_parser.add_argument("--directory", required=True, help="Directory name")
    stats_parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    
    # Stage 8: Define 'validate' command - validates generated collection files
    validate_parser = subparsers.add_parser("validate", help="Validate a Postman collection")
    validate_parser.add_argument("--collection-path", required=True, help="Path to collection file")
    
    # Stage 9: Parse command line arguments
    args = parser.parse_args()
    
    # Stage 10: Check if command was provided, show help if not
    if not args.command:
        parser.print_help()
        return
    
    # Stage 11: Route to appropriate handler function based on command
    try:
        if args.command == "generate":
            handle_generate(args)  # Handle single collection generation
        elif args.command == "generate-all":
            handle_generate_all(args)  # Handle bulk collection generation
        elif args.command == "list-directories":
            handle_list_directories(args)  # Handle directory listing
        elif args.command == "stats":
            handle_stats(args)  # Handle statistics display
        elif args.command == "validate":
            handle_validate(args)  # Handle collection validation
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def handle_generate(args):
    """Handle the generate command."""
    # Stage 12: Initialize collection generation process
    print("🔧 Generating Postman API collection...")
    print("=" * 50)
    
    # Stage 13: Create PostmanCollectionGenerator instance with source and output directories
    generator = PostmanCollectionGenerator(
        source_dir=args.source_dir,  # Directory containing JSON files to process
        output_dir=args.output_dir   # Directory where collections will be saved
    )
    
    # Stage 14: Choose generation method based on arguments
    if args.directory:
        # Generate collection for specific directory
        print(f"📁 Generating collection for directory: {args.directory}")
        collection_path = generator.generate_collection_for_directory(args.directory)
    else:
        # Generate collection for all files with custom name
        print(f"📁 Generating collection: {args.collection_name}")
        collection_path = generator.generate_postman_collection(args.collection_name)
    
    # Stage 15: Display results and usage instructions
    if collection_path:
        print(f"✅ Postman collection generated: {collection_path}")
        print("\n🎯 Ready for API testing!")
        print("=" * 50)
        print("To use this collection:")
        print("1. Open Postman")
        print("2. Click 'Import'")
        print(f"3. Select the file: {collection_path}")
        print("4. Start testing your APIs!")
    else:
        print("❌ Failed to generate Postman collection")
        sys.exit(1)


def handle_generate_all(args):
    """Handle the generate-all command."""
    # Stage 16: Initialize bulk collection generation process
    print("🔧 Generating single Postman API collection for all files...")
    print("=" * 50)
    
    # Stage 17: Create generator instance for processing all directories
    generator = PostmanCollectionGenerator(
        source_dir=args.source_dir,  # Source directory with all JSON files
        output_dir=args.output_dir   # Output directory for collections
    )
    
    # Stage 18: Generate collections for all available directories
    collections = generator.generate_all_collections()
    
    # Stage 19: Display results of bulk generation
    if collections:
        print(f"✅ Generated {len(collections)} collection:")
        print("=" * 50)
        for collection_name, collection_path in collections.items():
            print(f"📦 {collection_name}: {collection_path}")
        
        print("\n🎯 Ready for API testing!")
        print("=" * 50)
        print("To use this collection:")
        print("1. Open Postman")
        print("2. Click 'Import'")
        print("3. Select the generated collection file")
        print("4. Start testing your APIs!")
    else:
        print("❌ No collection was generated")
        sys.exit(1)


def handle_list_directories(args):
    """Handle the list-directories command."""
    # Stage 20: Initialize generator for directory listing
    generator = PostmanCollectionGenerator(source_dir=args.source_dir)
    
    # Stage 21: Get list of available directories containing JSON files
    directories = generator.list_available_directories()
    
    # Stage 22: Display directory information with statistics
    if directories:
        print("Available directories for Postman collections:")
        print("=" * 50)
        for directory in directories:
            # Get detailed statistics for each directory
            stats = generator.get_directory_stats(directory)
            if "error" not in stats:
                print(f"📁 {directory}:")
                print(f"   Files: {stats['total_files']}")           # Number of JSON files
                print(f"   Types: {', '.join(stats['suffixes'])}")   # File type suffixes
                print(f"   Edit IDs: {', '.join(stats['edit_ids'])}") # Edit identifiers
                print(f"   EOB Codes: {', '.join(stats['eob_codes'])}") # EOB codes
                print()
            else:
                print(f"📁 {directory}: {stats['error']}")
    else:
        print("No directories found in source directory.")


def handle_stats(args):
    """Handle the stats command."""
    # Stage 23: Initialize generator for statistics retrieval
    generator = PostmanCollectionGenerator(source_dir=args.source_dir)
    
    # Stage 24: Get detailed statistics for specified directory
    stats = generator.get_directory_stats(args.directory)
    
    # Stage 25: Handle errors and display statistics
    if "error" in stats:
        print(f"❌ {stats['error']}")
        sys.exit(1)
    
    # Stage 26: Display comprehensive directory statistics
    print(f"Postman Collection Statistics for {args.directory}:")
    print("=" * 50)
    print(f"Total Files: {stats['total_files']}")        # Count of JSON files
    print(f"File Types: {stats['file_types']}")          # Types of files found
    print(f"Edit IDs: {stats['edit_ids']}")              # Unique edit identifiers
    print(f"EOB Codes: {stats['eob_codes']}")            # EOB (Explanation of Benefits) codes
    print(f"Suffixes: {stats['suffixes']}")              # File naming suffixes


def handle_validate(args):
    """Handle the validate command."""
    # Stage 27: Convert collection path to Path object for file operations
    collection_path = Path(args.collection_path)
    
    # Stage 28: Check if collection file exists
    if not collection_path.exists():
        print(f"❌ Collection file not found: {collection_path}")
        sys.exit(1)
    
    # Stage 29: Initialize generator and validate collection
    generator = PostmanCollectionGenerator()
    validation_result = generator.validate_collection(collection_path)
    
    # Stage 30: Display validation results
    print(f"Validation Results for {collection_path}:")
    print("=" * 50)
    
    # Stage 31: Show validation status (valid/invalid)
    if validation_result["valid"]:
        print("✅ Collection is valid!")
    else:
        print("❌ Collection has errors:")
        for error in validation_result["errors"]:
            print(f"  - {error}")
    
    # Stage 32: Display warnings if any
    if validation_result["warnings"]:
        print("⚠️  Warnings:")
        for warning in validation_result["warnings"]:
            print(f"  - {warning}")
    
    # Stage 33: Display collection statistics
    if validation_result["stats"]:
        print("\n📊 Statistics:")
        for key, value in validation_result["stats"].items():
            print(f"  {key}: {value}")


# Stage 34: Entry point - run main function when script is executed directly
if __name__ == "__main__":
    main()
