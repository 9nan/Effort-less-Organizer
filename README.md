# File Organizer Tool

The File Organizer Tool is a Python script designed to help you organize your files efficiently. It sorts files into folders based on their extension, moves specific files to designated folders, and cleans up empty directories, making file management easier and more automated.

## Features

- **Organize Files by Extension**: Automatically moves files into folders categorized by their file extensions.
- **Move Specific File Types**: Easily move files of specified extensions to a designated folder, perfect for organizing software and media files.
- **Delete Empty Folders**: Cleans up the directory by removing empty folders.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This script is compatible with Python 3.6 and above. You can download Python from [python.org](https://www.python.org/).

### Installation

1. Download the `file_organizer.py` script to your local machine.
2. Choose or create the directories you wish to use with this script (e.g., source folder, organized folder).

### Configuration

Before running the script, open it in a text editor and configure the folder paths at the bottom of the script in the `main` function:

```python
source_folder = r'C:\Path\To\Your\SourceFolder'
organized_folder = r'C:\Path\To\Your\OrganizedFolder'
software_folder = r'C:\Path\To\Your\SoftwareFolder'
after_edit_folder = r'C:\Path\To\Your\AfterEditFolder'
```

Replace the placeholders with the actual paths you intend to use.

### Usage

Run the script from a terminal or command prompt:

```sh
python file_organizer.py
```

Follow the on-screen instructions. The script will organize files, move specific types, and clean up empty folders automatically.

## Customizing

To customize which file types are moved to specific folders, adjust the `software_extensions` and `media_extensions` lists in the `main` function:

```python
software_extensions = ['.exe', '.msi', '.apk', '.iso']
media_extensions = ['.mp4', '.mp3', '.wav', '.jpg', '.png', '.aac']
```

Add or remove file extensions as needed.

## Contributing

Contributions to improve the File Organizer Tool are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is open source and available under the [MIT License](LICENSE.md).

## Acknowledgments

- Thank you to all contributors and users for your support and suggestions.

