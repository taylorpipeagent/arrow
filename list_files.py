# filename: list_files.py
import os

# List all files in the working directory
working_dir = "/var/folders/64/0bk9412j2mjbvs0w8pl_h__80000gn/T/tmpp20kojyk"

for root, dirs, files in os.walk(working_dir):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))