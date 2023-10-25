import os, sys

def replace_in_directory(directory, search_string, replacement_string):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            with open(item_path, 'r') as file:
                contents = file.read()
            modified_contents = contents.replace(search_string, replacement_string)
            with open(item_path, 'w') as file:
                file.write(modified_contents)
        elif os.path.isdir(item_path):
            replace_in_directory(item_path, search_string, replacement_string)

if len(sys.argv) < 2:
    print("Usage: python bump_version.py <old_version> <new_version>")
    exit(0)

old_version = sys.argv[1]
new_version = sys.argv[2]

replace_in_directory('./PrusaSlicer/filament', "filament_notes = " + old_version, "filament_notes = " + new_version)
replace_in_directory('./PrusaSlicer/print', "notes = " + old_version, "notes = " + new_version)
replace_in_directory('./PrusaSlicer/printer', "printer_notes = " + old_version, "printer_notes = " + new_version)
