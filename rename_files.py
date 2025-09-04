import os
import re
import shutil

def rename_files():
    # Parameters extracted from folder name
    edit_id = "rvn001"
    code = "00W5"
    
    # Mapping for suffixes based on the expected output format
    suffix_mapping = {
        "positive": {
            "deny": "LR",    # deny -> LR
        },
        "negative": {
            "bypass": "NR",  # bypass -> NR
        },
        "Exclusion": {
            "market": "EX",   # market -> EX
            "date": "EX"      # dos -> EX
        }
    }
    
    # Source directory containing the files
    source_dir = "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/smoke"
    
    # Destination directory
    dest_dir = r"C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_files\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis\smoke"
    
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
        # Expected format: TC#XX_XXXXX#suffix.json (3 parts)
        parts = filename.split('#')
        
        if len(parts) == 3:
            # Handle 3-part template: TC#XX_XXXXX#suffix.json
            tc_part = parts[0]  # TC
            tc_id_part = parts[1]  # 01_12345
            suffix = parts[2].replace('.json', '')  # deny, bypass, market
            
            # Get the correct suffix mapping for the new template
            mapped_suffix = suffix
            for category in suffix_mapping.values():
                if suffix in category:
                    mapped_suffix = category[suffix]
                    break
            
            # Create new filename according to new template: TC#XX_XXXXX#rvn001#00W5#LR.json
            new_filename = f"{tc_part}#{tc_id_part}#{edit_id}#{code}#{mapped_suffix}.json"
            
            print(f"Current: {filename}")
            print(f"Converting to new template...")
            print(f"New:     {new_filename}")
            print(f"Moving to: {dest_dir}")
            print("-" * 40)
            
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
        else:
            print(f"Warning: {filename} doesn't match expected format (needs exactly 3 parts)")
            continue
    
    print("\n" + "=" * 60)
    print("Renaming and moving completed!")
    print(f"Files moved to: {dest_dir}")

if __name__ == "__main__":
    rename_files()
