import os

def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS
        os.system('clear')


def list_folders_and_files(directory, show_folders=True, show_files=True):
    """Lists folders and/or files in a directory, excluding hidden ones.

    Args:
        directory (str): The path to the directory.
        show_folders (bool, optional): If True, lists folders. Defaults to True.
        show_files (bool, optional): If True, lists files. Defaults to True.
    """

    try:
        for i, item in enumerate(os.listdir(directory), start=1):
            if not item.startswith('.'):
                if show_folders and os.path.isdir(os.path.join(directory, item)):
                    print(f"{i}. {item} (Folder)")
                if show_files and os.path.isfile(os.path.join(directory, item)):
                    print(f"{i}. {item} (File)")  
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")


def open_folder(directory):
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
    if os.path.exists(filepath):
        os.startfile(filepath)
    else:
        print(f"File '{filepath}' not found.")

def get_folder_path(folder_name, directory=None):
    if directory is None:
        directory = os.getcwd()
    for root,dirs,files in os.walk(directory):
        if folder_name in dirs:
            return os.path.join(root,folder_name)
    return None

def get_file_path(file_name, directory=None):
    if directory is None:
        directory = os.getcwd()
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return None


def get_relative_folder_path(folder_name):
    current_dir = os.getcwd()
    folder_path = get_folder_path(folder_name)
    if folder_path and folder_path.startswith(current_dir):
        return folder_path[len(current_dir) + 1:]
    return folder_path


def main():
    """Main function to manage the file explorer."""

    Path = os.getcwd()
    clear()

    while True:
        print(f"Current Path: {Path}")
        list_folders_and_files(Path,True,True)  # List files and folders with numbers

        print("\n")
        print("1. Open Folder")
        print("2. Open File")
        print("3. Back")
        print("9. Exit")
        print("\n")

        choice = int(input("Enter Choice (Number): "))

        if choice == 1:
            clear()
            print("Folders:")
            list_folders_and_files(Path, True,False)  # List only folders

            folder_number = int(input("Enter Folder Number: ")) - 1

            if folder_number :
                folder_name = os.listdir(Path)[folder_number]
                relative_folder_path = get_relative_folder_path(folder_name)
                if relative_folder_path:
                    Path = os.path.join(Path, relative_folder_path)
                    open_folder(Path)  # Open the folder
                else:
                    print("Invalid folder number.")
        elif choice == 2:
            clear()
            print("Files:")
            list_folders_and_files(Path,False,True)  # List only files

            file_number = int(input("Enter File Number: ")) - 1

            if file_number:
                file_name = os.listdir(Path)[file_number]
                file_path = get_file_path(file_name, Path)
                if file_path:
                    open_file(file_path)
                else:
                    print(f"File '{file_name}' not found.")
            else:
                print("Invalid file number.")
        elif choice == 3:
            os.chdir('..')
            Path = os.getcwd()
            clear()
        elif choice == 9:
            clear()
            break
        else:
            clear()
            print("Invalid Choice")

if __name__ == "__main__":
    main()