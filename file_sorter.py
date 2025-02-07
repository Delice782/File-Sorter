         
import os
import shutil

# Define file type categories and their corresponding folders
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.jpeg'],
    'Videos': ['.mp4', '.avi'],
    'Music': ['.mp3', '.wav']
}

# Function to get the folder name based on the file extension
def get_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return None  # If the file extension is not recognized

# Function to organize the file
def organize_file(file_path):
    # Get the file name and extension
    file_name, file_extension = os.path.splitext(file_path)
    
    # Determine the category for the file
    category = get_category(file_extension)
    
    if category is None:
        print(f"File type '{file_extension}' is not supported for file: {file_path}")
        return
    
    # Create the folder for the category if it doesn't exist
    folder_path = os.path.join(os.path.expanduser("~"), category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Define the destination path
    destination = os.path.join(folder_path, os.path.basename(file_path))
    
    # Move the file to the appropriate folder
    try:
        shutil.move(file_path, destination)
        print(f"File successfully moved to {destination}")
    except Exception as e:
        print(f"Error while moving the file: {e}")

# Main function to run the program
def main():
    # Ask for the file path to organize
    file_path = input("Enter the file path: ")
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return
    
    # Organize the file
    organize_file(file_path)

# Test the program
if __name__ == "__main__":
    main()
