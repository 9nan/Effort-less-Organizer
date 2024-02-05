import os
import shutil
import time

class FileOrganizer:
    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def organize_files(self):
        """Organize files by their extensions."""
        for folder_path, _, files in os.walk(self.source_folder):
            for file in files:
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    _, file_extension = os.path.splitext(file)
                    destination_path = os.path.join(self.destination_folder, file_extension[1:].lower())
                    os.makedirs(destination_path, exist_ok=True)
                    destination_file_path = os.path.join(destination_path, file)
                    self._move_file_with_increment(file_path, destination_file_path)

    def move_specific_files(self, file_extensions):
        """Move files with specific extensions to the destination folder."""
        for foldername, subfolders, filenames in os.walk(self.source_folder):
            for filename in filenames:
                if any(filename.lower().endswith(ext) for ext in file_extensions):
                    source_path = os.path.join(foldername, filename)
                    relative_path = os.path.relpath(source_path, self.source_folder)
                    destination_path = os.path.join(self.destination_folder, relative_path)
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                    shutil.move(source_path, destination_path)

    def delete_empty_folders(self):
        """Delete empty folders in the destination directory."""
        for root, dirs, files in os.walk(self.destination_folder, topdown=False):
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                if not os.listdir(folder_path):
                    print(f"Deleting empty folder: {folder_path}")
                    os.rmdir(folder_path)

    def _move_file_with_increment(self, source_file_path, destination_file_path):
        """Helper function to move files and handle name conflicts."""
        count = 1
        base, ext = os.path.splitext(destination_file_path)
        while os.path.exists(destination_file_path):
            destination_file_path = f"{base}_{count}{ext}"
            count += 1
        shutil.move(source_file_path, destination_file_path)

def main():
    # Placeholder paths - users should replace these with their actual folder paths
    source_folder = r'C:\Path\To\Your\SourceFolder'
    organized_folder = r'C:\Path\To\Your\OrganizedFolder'
    software_folder = r'C:\Path\To\Your\SoftwareFolder'
    after_edit_folder = r'C:\Path\To\Your\AfterEditFolder'

    # Define file extensions for software and media files
    software_extensions = ['.exe', '.msi', '.apk', '.iso']
    media_extensions = ['.mp4', '.mp3', '.wav', '.jpg', '.png', '.aac']

    # Organize files by extension
    organizer = FileOrganizer(source_folder, organized_folder)
    organizer.organize_files()
    print("Files have been organized.")
    time.sleep(3)

    # Move specific software-related files
    organizer = FileOrganizer(organized_folder, software_folder)
    organizer.move_specific_files(software_extensions)
    print("Software files moved successfully.")
    time.sleep(3)

    # Move media files
    organizer = FileOrganizer(organized_folder, after_edit_folder)
    organizer.move_specific_files(media_extensions)
    print("Media files moved successfully.")
    time.sleep(3)

    # Delete any empty folders left behind
    organizer = FileOrganizer(source_folder, organized_folder)
    organizer.delete_empty_folders()
    organizer = FileOrganizer(organized_folder, after_edit_folder)
    organizer.delete_empty_folders()
    print("Empty folders deleted.")

if __name__ == "__main__":
    main()
