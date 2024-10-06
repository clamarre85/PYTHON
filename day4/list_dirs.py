import os

root_dir = '/day4/list_dirs.py'

for root, dirs, files in os.walk(root_dir):
    print("Current Directory:", root)
    print("Subdirectories:", dirs)
    print("Files:", files)
    print()
