import os
import re
import shutil

def rename_files():
    # Parameters extracted from folder name
    edit_id = "rvn001"
    code = "00W5"
    
    # Mapping for suffixes
    suffix_mapping = {
        "Eligiable": "posi",
        "bypass": "nega",
        "market": "ex",
        "dos": "ex"
    }
    
    # Source directory containing the files
    source_dir = "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads/smoke"
    
    # Destination directory
    dest_dir = r"C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_files\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads\smoke"
    
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} not found!")
        return
    
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Get all JSON files in the source directory
    json_files = [f for f in os.listdir(source_dir) if f.endswith('.json')]
    
    print("Files to be renamed and moved:")
    print("=" * 60)
    
    for filename in json_files:
        # Parse the current filename
        # Expected format: TC_XX#suffix.json (2 parts)
        parts = filename.split('#')
        
        if len(parts) == 2:
            # Handle 2-part template: TC_XX#suffix.json
            tc_part = parts[0]  # TC_01, TC_02, etc.
            suffix = parts[1].replace('.json', '')  # Eligiable, bypass, market, dos
            
            # Get the correct suffix mapping for the new template
            mapped_suffix = suffix_mapping.get(suffix, suffix)
            
            # Create new filename according to new template
            new_filename = f"{tc_part}#{suffix}#{edit_id}#{code}#{mapped_suffix}.json"
            
            print(f"Current: {filename}")
            print(f"Converting to new template...")
            print(f"New:     {new_filename}")
            print(f"Moving to: {dest_dir}")
            print("-" * 40)
            
        else:
            print(f"Warning: {filename} doesn't match expected format (needs exactly 2 parts)")
            continue
        
        # Source and destination paths
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, new_filename)
        
        try:
            # Copy the file to destination with new name
            shutil.copy2(source_path, dest_path)
            print(f"✓ Successfully copied and renamed: {filename} → {new_filename}")
            
            # Remove the original file
            os.remove(source_path)
            print(f"✓ Removed original file: {filename}")
            
        except Exception as e:
            print(f"✗ Error processing {filename}: {e}")
    
    print("\n" + "=" * 60)
    print("Renaming and moving completed!")
    print(f"Files moved to: {dest_dir}")

if __name__ == "__main__":
    rename_files()
