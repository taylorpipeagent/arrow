# filename: upload_files.py

import os

# Files to be uploaded
files_to_upload = [
    "README.rst",
    "CHANGELOG.rst",
    "docs/index.rst",
    "docs/Makefile",
    "docs/conf.py",
    "docs/guide.rst",
    "docs/make.bat",
    "docs/releases.rst",
    "docs/api-guide.rst",
    "docs/getting-started.rst"
]

# Base directory
base_dir = "/var/folders/64/0bk9412j2mjbvs0w8pl_h__80000gn/T/tmpp20kojyk"

# Function to read the content of a file
def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to upload a file to the knowledge base
def upload_file(file_name, file_content):
    from functions import write_file
    response = write_file({
        "working_dir": base_dir,
        "file_path": file_name,
        "file_content": file_content
    })
    return response

# Upload each file and print the status
for file in files_to_upload:
    file_path = os.path.join(base_dir, file)
    file_content = read_file_content(file_path)
    response = upload_file(file, file_content)
    print(f"Uploading {file}: Response: {response}")