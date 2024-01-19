# -*- mode: python ; coding: utf-8 -*-
import os
import shutil
import tkinter as tk
from tkinter import PhotoImage   
from PIL import Image, ImageTk  
from tkinter import filedialog
from ttkthemes import ThemedStyle

# Function to create a directory if it doesn't exist
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# Function to organize files into folders based on their file type
def organize_files(source_dir, dest_dir, status_label):
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1][1:].lower()

            # Define folders for different file types (you can add more)
            file_type_folders = {
                "Documents 📁": ["pdf", "doc", "docx", "txt", "csv"],
                "Images 🖼️": ["jpg", "jpeg", "png", "gif", "svg", "heic"],
                "Videos 📼": ["mp4", "avi", "mkv", "mov"],
                "Music 🎵": ["mp3", "wav", "flac"],
                "Compressed 🔐": ["zip", "rar", "7z"],
                "Programming 💻": ["py", "c", "cpp", "java", "js", "html", "css", "json", "xml", "md", "html", "css", "yml"],
                "Others 🧢": ["exe", "iso", "dmg", "apk", "ipa", "app", "pkg"],
            }

            for folder, extensions in file_type_folders.items():
                if file_extension in extensions:
                    dest_folder = os.path.join(dest_dir, folder)
                    create_directory(dest_folder)
                    dest_file_path = os.path.join(dest_folder, file)

                    # Move the file to the respective folder
                    shutil.move(source_file_path, dest_file_path)
                    print(f"Moved {file} to {folder} folder")
    
    # Update the status label to indicate completion
    status_label.config(text="Organizing files completed ✅")

# Function to open a file dialog for selecting a folder
def select_folder(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

# Create the main application window
root = tk.Tk()
root.title("File Organizer")

# Load the background image using PIL
background_image = Image.open("/Users/rachellarralde/Developer/z-file-cleaner/dist/FileCleaner/bg-4.png") 
background_photo = ImageTk.PhotoImage(background_image)

# Create a ThemedStyle with a dark theme
style = ThemedStyle(root)
style.set_theme("equilux")

# Create a Label widget to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the window size
root.geometry("400x250")  # Increased height for status label

# Configure the background and foreground (text) colors for the main window
root.configure(bg='black')
root.option_add('*TButton*highlightBackground', 'black')  # Configure button highlight color

# Create and set up labels and entry fields for source and destination folders
source_label = tk.Label(root, text="Source Folder:", bg='black', fg='white')
source_label.pack()
source_entry = tk.Entry(root, width=20)
source_entry.pack()
source_button = tk.Button(root, text="Browse", command=lambda: select_folder(source_entry), bg='black', fg='black')
source_button.pack()

destination_label = tk.Label(root, text="Destination Folder:", bg='black', fg='white')
destination_label.pack()
destination_entry = tk.Entry(root, width=20)
destination_entry.pack()
destination_button = tk.Button(root, text="Browse", command=lambda: select_folder(destination_entry), bg='black', fg='black')
destination_button.pack()

# Function to start organizing files when the button is clicked
def organize_files_button():
    source_dir = source_entry.get()
    dest_dir = destination_entry.get()
    create_directory(dest_dir)
    
    # Clear the status label
    status_label.config(text="")
    
    # Organize files and update status
    organize_files(source_dir, dest_dir, status_label)

# Customize the Organize Files button to stand out, set text color to black, and give it a red border
organize_button = tk.Button(root, text="Organize Files", command=organize_files_button, bg='red', fg='black', bd=1, relief="solid")
organize_button.pack()


# Label to display the status
status_label = tk.Label(root, text="", bg='black', fg='green')
status_label.pack()

root.mainloop()
