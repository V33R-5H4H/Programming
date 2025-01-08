import os
import platform
import subprocess

def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS
        os.system('clear')

def list_directory(directory, show_folders=True, show_files=True):
    """
    List the contents of a directory, optionally showing folders and/or files.
    
    Args:
        directory (str): Path to the directory to list.
        show_folders (bool): Whether to show folders. Defaults to True.
        show_files (bool): Whether to show files. Defaults to True.
    """
    try:
        items = [item for item in os.listdir(directory)
                 if not item.startswith('.') and
                 ((show_folders and os.path.isdir(os.path.join(directory, item))) or
                  (show_files and os.path.isfile(os.path.join(directory, item))))]
        
        for i, item in enumerate(items, start=1):
            path = os.path.join(directory, item)
            if show_folders and os.path.isdir(path):
                print(f"{i}. {item} (Folder)")
            if show_files and os.path.isfile(path):
                print(f"{i}. {item} (File)")
                
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")

def open_folder(directory):
    """
    Change the current working directory.
    
    Args:
        directory (str): Path to the directory to open.
    
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        os.chdir(directory)
        return True
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return False
    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")
        return False

def open_file(filepath):
    """
    Open a file using the default application based on the operating system.
    
    Args:
        filepath (str): Path to the file to be opened.
    """
    try:
        if not os.path.exists(filepath):
            print(f"File '{filepath}' not found.")
            return
        
        if platform.system() == 'Windows':
            os.startfile(filepath)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.run(['open', filepath])
        else:  # Linux
            subprocess.run(['xdg-open', filepath])
    except Exception as e:
        print(f"Error opening file: {str(e)}")

def get_folder_path(folder_name, directory=None):
    """
    Get the absolute path of a folder in the specified directory.
    
    Args:
        folder_name (str): Name of the folder to locate.
        directory (str, optional): Base directory to search in. Defaults to current working directory.
    
    Returns:
        str or None: Absolute path of the folder if found, None otherwise.
    """
    if directory is None:
        directory = os.getcwd()
    
    # Input validation    
    if not folder_name or not isinstance(folder_name, str):
        print("Invalid folder name provided")
        return None
        
    try:
        # Normalize the path to handle any path separators
        full_path = os.path.normpath(os.path.join(directory, folder_name))
        
        # Check if path exists and is a directory
        if os.path.exists(full_path) and os.path.isdir(full_path):
            return os.path.abspath(full_path)
        else:
            print(f"Folder '{folder_name}' not found in '{directory}'")
            return None
            
    except (TypeError, ValueError) as e:
        print(f"Error processing path: {str(e)}")
        return None
    except PermissionError:
        print(f"Permission denied accessing '{directory}'")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

def get_file_path(file_name, directory=None):
    """
    Get the absolute path of a file in the specified directory.
    
    Args:
        file_name (str): Name of the file to locate.
        directory (str, optional): Base directory to search in. Defaults to current working directory.
    
    Returns:
        str or None: Absolute path of the file if found, None otherwise.
    """
    if directory is None:
        directory = os.getcwd()
    
    try:
        for root, dirs, files in os.walk(directory):
            if file_name in files:
                return os.path.join(root, file_name)
        print(f"File '{file_name}' not found in '{directory}'")
        return None
    except Exception as e:
        print(f"Error processing path: {str(e)}")
        return None

def get_relative_folder_path(folder_name):
    """
    Get the relative path of a folder from the current working directory.
    
    Args:
        folder_name (str): Name of the folder to locate.
    
    Returns:
        str or None: Relative path of the folder if found, None otherwise.
    """
    current_dir = os.getcwd()
    folder_path = get_folder_path(folder_name)
    if folder_path and folder_path.startswith(current_dir):
        return folder_path[len(current_dir) + 1:]
    return folder_path

clear()
os.chdir("C:/V33R/Programming")
Path = os.getcwd()

while True:
    print(f'Path : {Path}')
    list_directory(Path, True, True)

    print("\n")
    print("1. Open Folder")
    print("2. Open File")
    print("3. Back")
    print("9. Exit")
    print("\n")

    ch = str(input("Enter Choice : "))

    if ch == '1':
        clear()
        print('Folders : \n')
        list_directory(Path, True, False)

        folder_N = int(input("\nEnter Folder Number : ")) - 1

        if folder_N >= 0:
            items = [item for item in os.listdir(Path) if not item.startswith('.') and os.path.isdir(os.path.join(Path, item))]
            if folder_N < len(items):
                folder = items[folder_N]
                relative_folder_path = get_relative_folder_path(folder)
                if relative_folder_path:
                    Path = os.path.join(Path, relative_folder_path)
                    open_folder(Path)
                    os.chdir(Path)
                    print('\n')
                else:
                    print("Invalid folder path.")
            else:
                print("Invalid folder number.")
        else:
            print("Invalid folder number.")
        clear()

    elif ch == '2':
        clear()
        print('Files : \n')
        list_directory(Path, False, True)

        file_n = int(input("Enter File No : ")) - 1

        if file_n >= 0:
            items = [item for item in os.listdir(Path) if not item.startswith('.') and os.path.isfile(os.path.join(Path, item))]
            if file_n < len(items):
                file_name = items[file_n]
                file_path = get_file_path(file_name, Path)
                if file_path:
                    open_file(file_path)
                else:
                    print(f"File '{file_name}' not found.")
            else:
                print("Invalid file number.")
        else:
            print("Invalid file number.")
        clear()

    elif ch == '3':
        os.chdir('..')
        Path = os.getcwd()
        clear()

    elif ch == '9':
        clear()
        break

    else:
        clear()
        print("Invalid Choice")