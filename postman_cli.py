#!/usr/bin/env python3
"""
Postman Collection CLI - Command Line Interface for generating Postman collections
from renamed JSON files in the renaming_postman_collection project
"""

import argparse
import sys
import os
from pathlib import Path

# Import the Postman generator
from postman_generator import PostmanCollectionGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Postman Collection Generator for renaming_postman_collection project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Generate Postman collection for all JSON files
    python postman_cli.py generate --collection-name "RevenueTestCollection"
    
    # Generate collection for specific directory
    python postman_cli.py generate --directory "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"
    
    # List available directories
    python postman_cli.py list-directories
    
    # Show statistics for a directory
    python postman_cli.py stats --directory "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"
    
    # Generate collections for all directories
    python postman_cli.py generate-all
    
    # Validate a collection
    python postman_cli.py validate --collection-path "postman_collections/test_collection/postman_collection.json"
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate Postman collection")
    generate_parser.add_argument("--collection-name", default="TestCollection", help="Name for the collection")
    generate_parser.add_argument("--directory", help="Generate collection for specific directory")
    generate_parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    generate_parser.add_argument("--output-dir", default="postman_collections", help="Output directory for Postman collections")
    
    # Generate all command
    generate_all_parser = subparsers.add_parser("generate-all", help="Generate collections for all directories")
    generate_all_parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    generate_all_parser.add_argument("--output-dir", default="postman_collections", help="Output directory for Postman collections")
    
    # List directories command
    list_dirs_parser = subparsers.add_parser("list-directories", help="List available directories")
    list_dirs_parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    
    # Stats command
    stats_parser = subparsers.add_parser("stats", help="Show statistics for a directory")
    stats_parser.add_argument("--directory", required=True, help="Directory name")
    stats_parser.add_argument("--source-dir", default="renaming_jsons", help="Source directory containing JSON files")
    
    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate a Postman collection")
    validate_parser.add_argument("--collection-path", required=True, help="Path to collection file")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == "generate":
            handle_generate(args)
        elif args.command == "generate-all":
            handle_generate_all(args)
        elif args.command == "list-directories":
            handle_list_directories(args)
        elif args.command == "stats":
            handle_stats(args)
        elif args.command == "validate":
            handle_validate(args)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def handle_generate(args):
    """Handle the generate command."""
    print("🔧 Generating Postman API collection...")
    print("=" * 50)
    
    generator = PostmanCollectionGenerator(
        source_dir=args.source_dir,
        output_dir=args.output_dir
    )
    
    if args.directory:
        print(f"📁 Generating collection for directory: {args.directory}")
        collection_path = generator.generate_collection_for_directory(args.directory)
    else:
        print(f"📁 Generating collection: {args.collection_name}")
        collection_path = generator.generate_postman_collection(args.collection_name)
    
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
    print("🔧 Generating single Postman API collection for all files...")
    print("=" * 50)
    
    generator = PostmanCollectionGenerator(
        source_dir=args.source_dir,
        output_dir=args.output_dir
    )
    
    collections = generator.generate_all_collections()
    
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
    generator = PostmanCollectionGenerator(source_dir=args.source_dir)
    directories = generator.list_available_directories()
    
    if directories:
        print("Available directories for Postman collections:")
        print("=" * 50)
        for directory in directories:
            stats = generator.get_directory_stats(directory)
            if "error" not in stats:
                print(f"📁 {directory}:")
                print(f"   Files: {stats['total_files']}")
                print(f"   Types: {', '.join(stats['suffixes'])}")
                print(f"   Edit IDs: {', '.join(stats['edit_ids'])}")
                print(f"   EOB Codes: {', '.join(stats['eob_codes'])}")
                print()
            else:
                print(f"📁 {directory}: {stats['error']}")
    else:
        print("No directories found in source directory.")


def handle_stats(args):
    """Handle the stats command."""
    generator = PostmanCollectionGenerator(source_dir=args.source_dir)
    stats = generator.get_directory_stats(args.directory)
    
    if "error" in stats:
        print(f"❌ {stats['error']}")
        sys.exit(1)
    
    print(f"Postman Collection Statistics for {args.directory}:")
    print("=" * 50)
    print(f"Total Files: {stats['total_files']}")
    print(f"File Types: {stats['file_types']}")
    print(f"Edit IDs: {stats['edit_ids']}")
    print(f"EOB Codes: {stats['eob_codes']}")
    print(f"Suffixes: {stats['suffixes']}")


def handle_validate(args):
    """Handle the validate command."""
    collection_path = Path(args.collection_path)
    
    if not collection_path.exists():
        print(f"❌ Collection file not found: {collection_path}")
        sys.exit(1)
    
    generator = PostmanCollectionGenerator()
    validation_result = generator.validate_collection(collection_path)
    
    print(f"Validation Results for {collection_path}:")
    print("=" * 50)
    
    if validation_result["valid"]:
        print("✅ Collection is valid!")
    else:
        print("❌ Collection has errors:")
        for error in validation_result["errors"]:
            print(f"  - {error}")
    
    if validation_result["warnings"]:
        print("⚠️  Warnings:")
        for warning in validation_result["warnings"]:
            print(f"  - {warning}")
    
    if validation_result["stats"]:
        print("\n📊 Statistics:")
        for key, value in validation_result["stats"].items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
