# File Organizer App

## Overview ✨

The File Organizer App is a Python application that helps you keep your files organized. With just a few clicks, you can sort your files into folders based on their file types, making it easier to find and manage your files. 

(This is still a WIP)

## Features 🚀

- Organize files into folders based on their file types (e.g., Documents, Images, Videos, Music, Compressed, Programming, Others).
- User-friendly graphical interface built with Tkinter.
- Customizable source and destination folders.

## Getting Started 📁

- Clone the repository.
- Run the file app.py file 
- The app will open in a new window.
- If you want to run the .app instead go to the dist folder and run the FileOrganizer.app.

## Requirements 

- Python 3.11 or above 
- Tkinter
- Pillow
- Pyinstaller
- shutil

## Code Info 📄

- This function checks if a directory exists and creates it if it doesn't:

`def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)`

- We use another function to organize files from the source folder to the destination folders based on their file types. It uses a dictionary called file_type_folders to determine the category of each file:

`def organize_files(source_dir, dest_dir, status_label):
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1][1:].lower()`

            - It takes 3 parameters:  source_dir, dest_dir, and status_label
            - we use a loop to iterate over each file in the current directory
            - We combine the root (current directory) and file (current file name) to create the full path to the current file.
            - splitext(file) splits the file name into its base name and extension. For example, separates "example.txt" into ("example", ".txt").


- This function opens a file dialog for selecting a folder and updates the specified entry field with the chosen folder path: 

`def select_folder(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)`



