# Automatic File Sorter Script

A Python script designed to automatically organize files into categorical folders based on their extensions. The script correctly handles duplicate names and skips hidden files.

## Features

* **Categorization by Extensions**: Distributes files into the following folders:
  * `Documents` — `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`
  * `Images` — `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`
  * `Archives` — `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
  * `Applications` — `.exe`, `.msi`, `.dmg`
  * `Others` — files with other extensions or without any.
* **Overwrite Protection**: If a file with the same name already exists in the target folder, the script automatically appends a numeric suffix (e.g., `file_1.txt`, `file_2.txt`).
* **Safety**: Ignores subdirectories and hidden files (those starting with a dot).
* **Logging**: Outputs a detailed report to the console for each moved file, along with the total number of processed items.

## Requirements

* Python 3.4 or higher (uses the built-in `pathlib` module).
* No external libraries required (uses standard `shutil` and `pathlib` modules).

## Usage

1. Open the script file and specify the path to the target directory in the `__main__` block:
   ```python
   folder_to_sort = r"C:\Users\User\Downloads" # Replace with your path

Error Handling
•	The script verifies the existence of the specified directory before starting. If the path is invalid, execution terminates with an error message.
•	Moving each individual file is wrapped in a try-except block. If a file is locked by the system or inaccessible, the script will display a warning and continue processing the remaining files.
