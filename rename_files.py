#!/usr/bin/env python3
"""
Alternative command interface for rename_files_with_postman.py
This file provides a shorter command format for convenience.
Now supports dynamic TS number discovery.
"""

import sys
import os
import subprocess
import argparse

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main function to handle command line arguments and execute the appropriate script."""
    
    # Set up argument parser for this wrapper
    parser = argparse.ArgumentParser(
        description="Short command interface for file renaming and Postman collection generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python rename_files.py --TS01    # Process TS01 model
  python rename_files.py --TS02    # Process TS02 model  
  python rename_files.py --TS 03   # Process TS03 model (auto-discovered)
  python rename_files.py --TS 04   # Process TS04 model (auto-discovered)
  python rename_files.py --all     # Process all discovered models
  python rename_files.py --list    # List all available TS models
        """
    )
    
    # Add model-specific arguments
    parser.add_argument("--TS01", action="store_true", 
                       help="Process TS01 model")
    parser.add_argument("--TS02", action="store_true", 
                       help="Process TS02 model")
    parser.add_argument("--all", action="store_true", 
                       help="Process all discovered models")
    parser.add_argument("--list", action="store_true", 
                       help="List all available TS models")
    parser.add_argument("--no-postman", action="store_true", 
                       help="Skip Postman collection generation")
    
    # Add dynamic TS number support
    parser.add_argument("--TS", type=str, metavar="NUMBER",
                       help="Process specific TS model by number (e.g., --TS 03)")
    
    args = parser.parse_args()
    
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    main_script = os.path.join(script_dir, "rename_files_with_postman.py")
    
    # Build command arguments
    cmd_args = [sys.executable, main_script]
    
    # Convert arguments to the main script format
    if args.TS01:
        cmd_args.append("--TS01")
    if args.TS02:
        cmd_args.append("--TS02")
    if args.all:
        cmd_args.append("--all")
    if args.list:
        cmd_args.append("--list")
    if args.no_postman:
        cmd_args.append("--no-postman")
    if args.TS:
        cmd_args.extend(["--TS", args.TS])
    
    # If no arguments provided, show help
    if len(cmd_args) == 2:  # Only sys.executable and main_script
        parser.print_help()
        return
    
    # Run the main script with the converted arguments
    try:
        print(f"🚀 Executing: {' '.join(cmd_args)}")
        result = subprocess.run(cmd_args, check=True)
        sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except Exception as e:
        print(f"Error running main script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
