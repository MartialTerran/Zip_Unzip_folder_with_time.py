"""
Python script to automatically compress a specified folder into a ZIP file with a unique, time-stamped filename. Ideal for regular backups and archiving.

Safety Analysis of the Python Script
Based on the provided code, the Python script appears to be safe to run from the CMD console in Windows 10. Here's a breakdown of its actions:
Imports: It uses standard libraries like tkinter, shutil, datetime, os, and json for file selection, compression, time stamping, and file handling. These libraries are safe and commonly used.
Folder Selection: The script allows you to choose a folder using a graphical interface, which reduces the risk of accidentally selecting the wrong directory.
Zipping: It creates a ZIP file of the chosen folder in the parent directory. The filename includes a timestamp for uniqueness. The script uses shutil.make_archive, a standard library function, for creating the ZIP file.
Error Handling: The script includes basic error handling to catch potential issues during the zipping process and display an error message.
Remembering Folder: It stores the path of the last selected folder in a JSON file for convenience in future uses. This file is read and written using the json library.
Potential Considerations:
While the script seems safe, here are some points to consider:
Large Folders: If you choose a very large folder, the zipping process might take a long time and consume significant system resources.
Existing Files: The script will overwrite any existing ZIP file with the same name in the parent directory.
File Permissions: Ensure you have the necessary permissions to read and write files in the chosen directory and its parent directory.
Recommendations:
Test with a small folder first to ensure it works as expected.
Review the code if you have any concerns about its functionality.
Be cautious with large folders and monitor the process.
Conclusion:
The provided Python script appears safe to run, implementing standard libraries and good practices. However, as with any script, it's recommended to understand its functionality and take necessary precautions before execution.

Original Main:
def main():
    #Main function to handle the folder selection, zipping, and remembering process.
    #Adds GUI-based feedback to the user.

    last_folder = load_last_folder()
    selected_folder = select_folder(last_folder)
    if selected_folder:
        zip_file_path = zip_folder(selected_folder)
        if zip_file_path:
            print (f"Folder zipped successfully: {zip_file_path}")
            #messagebox.showinfo("Success", f"Folder zipped successfully: {zip_file_path}") # activating this popup messsage will prevent closure of the script.
        remember_folder(selected_folder)
if __name__ == "__main__":
    main()

Unzip Option
Rewrite the script to offer to DeCompress the Zipped_Folder.zip if the filename of the selected item is .zip  If the offer to decompress the zipped_folder.zip is not accepted, then end the script.

Explanation of Changes:
ZIP File Check: Inside the main function, after the folder is selected, we check if the selected_folder string ends with ".zip" using endswith(".zip").
Decompress Option: If it's a ZIP file, we use messagebox.askyesno to ask the user if they want to decompress it.
Decompression: If they choose "Yes", we use shutil.unpack_archive to extract the contents of the ZIP file to its parent directory. A success message is displayed if the decompression is successful, or an error message if there's an issue.
No Decompression: If the user chooses "No" to decompression or the selected file is not a ZIP file, the script proceeds with its normal zipping behavior as before.
Exiting: If the user chooses not to decompress the .zip file, the script ends without taking any action.

Original:
def select_folder(initial_dir):
    #Opens a dialog to select a folder and returns the selected folder's path.
    #Uses a more efficient method without creating and hiding the root window.

    folder_path = filedialog.askdirectory(initialdir=initial_dir, title="Select a Folder")
    return folder_path

Explanation of Changes:
askopenfilename Instead of askdirectory: We switched from filedialog.askdirectory to filedialog.askopenfilename. This allows the user to select a single file (which can be a ZIP file) in addition to folders.
filetypes Argument: We added the filetypes argument to specify the allowed file types for selection.
("ZIP files", "*.zip") allows selection of files with the ".zip" extension.
("Folders", "*") allows selection of folders (represented by "*").
Return Value: The function now returns the path to the selected file (which could be a folder or a ZIP file) as file_path.
Additional Considerations:
The rest of the script might need slight modifications to handle both folders and ZIP files appropriately. For example, you might need to add checks to distinguish between them before zipping or decompressing.
You might want to update the title of the dialog box or the messages displayed to the user to reflect that both folders and ZIP files can be selected.


When the zippled_folderDATE.zip is unzipped, its contents are spilled all over the parent directory, instead of creating a new folder named rewite to mkdir a zippled_folderDATE folder and then insert the unzipped files contents into the new zippled_folderDATE folder:
Explanation of Changes:
Get Base Filename: We extract the base filename (without the ".zip" extension) from the selected_folder path using os.path.splitext. This will be used as the name for the new folder where the contents will be extracted.
Create Target Folder: We construct the path for the target folder using os.path.join and then use os.makedirs(..., exist_ok=True) to create the folder if it doesn't already exist. The exist_ok=True parameter prevents an error if the folder already exists.
Extract to Target Folder: We modify the shutil.unpack_archive call to extract the contents of the ZIP file into the newly created target_folder instead of the parent directory.
# ... (rest of the code remains the same)

def main():
    # ... (rest of the main function remains the same)

    if selected_folder:
        if selected_folder.endswith(".zip"):
            decompress = messagebox.askyesno("Decompress", "Do you want to decompress the selected ZIP file?")
            if decompress:
                try:
                    # 1. Get the base filename without the .zip extension
                    folder_name = os.path.splitext(os.path.basename(selected_folder))[0]

                    # 2. Create the target folder for extraction
                    target_folder = os.path.join(os.path.dirname(selected_folder), folder_name)
                    os.makedirs(target_folder, exist_ok=True)  # Create if it doesn't exist

                    # 3. Extract the ZIP file into the target folder
                    shutil.unpack_archive(selected_folder, target_folder)
                    messagebox.showinfo("Success", "ZIP file decompressed successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while decompressing: {e}")
            else:
                messagebox.showinfo("Exiting", "Exiting the script. No action taken.")
       # ... (rest of the main function remains the same)


LATER Add a COMPARE FOLDERS option:
Can I CTRL-select  TWO FOLDERS in  filedialog.askopenfilename, then detect of TWO FOLDERS have been selected, and if so, launch the def compare_folders():,  And, write the def compare_folders():
Model
Unfortunately, the filedialog.askopenfilename function in Tkinter does not directly support Ctrl-selecting multiple folders. It's primarily designed for selecting single files.
Workarounds:
Use filedialog.askopenfilenames for Multiple Files:
This function allows the user to select multiple files (including ZIP files) using Ctrl/Shift clicks.
You would then need to check if the selected files are folders (using os.path.isdir) and handle the comparison logic accordingly.
Custom File/Folder Selection Dialog (Advanced):
Create a custom dialog using Tkinter's more advanced widgets like Listbox and implement your own selection logic to allow multiple folder selections.
Example (Using askopenfilenames):
import os
from tkinter import filedialog, messagebox

# ... (rest of your code)

def select_files():
    ###Allows selection of multiple files/folders (with limitations).###
    file_paths = filedialog.askopenfilenames(
        initialdir=initial_dir,
        title="Select Files/Folders",
        filetypes=[("All files", "*")]  # Allow all file types
    )

    if len(file_paths) == 2:
        # Check if both selections are folders
        if all(os.path.isdir(path) for path in file_paths):
            compare_folders(file_paths[0], file_paths[1])
        else:
            messagebox.showwarning("Warning", "Please select two folders to compare.")
    else:
        messagebox.showinfo("Info", "Please select exactly two folders to compare.")

def compare_folders(folder1, folder2):
    ### Compares the contents of two folders.  ###
    # Implement your folder comparison logic here 
    # (e.g., using filecmp, comparing file lists, etc.)
    messagebox.showinfo("Comparison", "Folder comparison is not yet implemented.")  # Replace with your comparison logic

# ... (rest of your code)

Implementation for compare_folders:
The specific implementation of compare_folders will depend on your exact comparison requirements. Here are some general approaches you could consider:
filecmp Module: Use the filecmp module in Python to compare files and directories. This module provides functions like cmpfiles for comparing files and dircmp for comparing directories.
Manual Comparison:
Get lists of files in both folders using os.listdir.
Compare the file lists (names, sizes, timestamps, etc.) to identify differences.
You can also recursively compare subdirectories if needed.
Hashing: Calculate hashes (e.g., MD5 or SHA-1) for files and compare the hashes to determine if the files are identical.
Important Considerations:
This approach has limitations as askopenfilenames is still intended for file selection, and folder selection behavior might be inconsistent across different operating systems and Tkinter versions.
Handling subdirectories and complex file structures within the comparison logic can be challenging. You'll need to carefully consider how deep you want the comparison to go and how to handle differences in folder structures.
Consider using a third-party library specifically designed for directory comparison if you need more robust and feature-rich functionality.
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import datetime
import os
import json

# Constants
LAST_FOLDER_FILE = "last_folder.json"   
#This line is used throughout the script to reference the filename when saving and loading the last used folder path. For example:
#Saving: When the user selects a folder, the script saves its path to the file named "last_folder.json".
#Loading: When the script starts, it tries to load the last used folder path from the "last_folder.json" file to provide a convenient starting point for the user.

#The script uses a Graphical User Interface (GUI) for selecting the folder.
#This is achieved using the tkinter library, which provides tools for creating graphical interfaces in Python. 
#Specifically, the filedialog.askdirectory() function opens a dialog box where the user can browse and choose the desired folder.


def select_folder(initial_dir):
    """Opens a dialog to select a folder or a ZIP file and returns the selected path."""

    file_path = filedialog.askopenfilename(
        initialdir=initial_dir,
        title="Select a Folder or ZIP file",
        filetypes=[("ZIP files", "*.zip"), ("Folders", "*")]  # Allow both folders and ZIP files
    )
    return file_path

def zip_folder(folder_path):

    #Zips the specified folder and saves the zip file to the parent directory.
    #The zip file is named using the folder name and current timestamp.
    #Adds error handling.

    if not folder_path:
        return None

    try:
        folder_name = os.path.basename(folder_path)
        folder_name_ = os.path.basename(folder_path).replace(" ", "_")  # .replace(" ", "_"): This new part uses the replace method on the extracted folder name. It replaces any spaces (" ") within the name with underscores ("_").
        parent_dir = os.path.dirname(folder_path)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        #zip_file_name = f"{folder_name}_{timestamp}.zip"
        zip_file_name = f"{folder_name_}_{timestamp}.zip"
        zip_file_path = os.path.join(parent_dir, zip_file_name)

        shutil.make_archive(zip_file_path.replace('.zip', ''), 'zip', folder_path)
        return zip_file_path
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred while zipping the folder {folder_name}: {e}")
        return None

def remember_folder(folder_path):

    #Saves the folder path to a file for future reference.

    with open(LAST_FOLDER_FILE, 'w') as file:
        json.dump({"last_folder": folder_path}, file)

def load_last_folder():

    #Loads the last selected folder from the file.

    if os.path.exists(LAST_FOLDER_FILE):
        with open(LAST_FOLDER_FILE, 'r') as file:
            data = json.load(file)
            return data.get("last_folder", "")
    return ""

def main():
    #Main function to handle the folder selection, zipping, and remembering process.
    #Adds GUI-based feedback to the user.

    last_folder = load_last_folder()
    selected_folder = select_folder(last_folder)

 
    if selected_folder:
        if selected_folder.endswith(".zip"):
            decompress = messagebox.askyesno("Decompress", "Do you want to decompress the selected ZIP file?")
            if decompress:
                try:
                    # 1. Get the base filename without the .zip extension
                    folder_name = os.path.splitext(os.path.basename(selected_folder))[0]

                    # 2. Create the target folder for extraction
                    target_folder = os.path.join(os.path.dirname(selected_folder), folder_name)
                    os.makedirs(target_folder, exist_ok=True)  # Create if it doesn't exist

                    # 3. Extract the ZIP file into the target folder
                    shutil.unpack_archive(selected_folder, target_folder)
                    messagebox.showinfo("Success", "ZIP file decompressed successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Error while decompressing {selected_folder}: {e}")
            else:
                print("Exiting", "Exiting the script. No action taken.")
                #messagebox.showinfo("Exiting", "Exiting the script. No action taken.")
        else:
            zip_file_path = zip_folder(selected_folder)
            if zip_file_path:
                print(f"Folder zipped successfully: {zip_file_path}")
                #messagebox.showinfo("Success", f"Folder zipped successfully: {zip_file_path}") # activating this popup messsage will prevent closure of the script.
            remember_folder(selected_folder)

if __name__ == "__main__":
    main()

