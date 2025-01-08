import os
def clear():
    os.system('cls')
def open_folder(directory):
    try:
        files = os.listdir(directory)
        for i, item in enumerate(files, start=1):
            if not item.startswith('.'):
                if os.path.isfile(os.path.join(directory, item)):
                    print(f"{i}. {item} (File)")
                elif os.path.isdir(os.path.join(directory, item)):
                    print(f"{i}. {item} (Folder)")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")
        
def get_file_path(file_name,directory=None):
    if directory is None:
        directory = os.getcwd()
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return os.path.join(root,file_name)
    return None
    
def get_folder_path(folder_name, directory=None):
    if directory is None:
        directory = os.getcwd()
    for root,dirs,files in os.walk(directory):
        if folder_name in dirs:
            return os.path.join(root,folder_name)
    return None

def get_relative_folder_path(folder_name):
    current_dir = os.getcwd()
    folder_path = get_folder_path(folder_name)
    if folder_path and folder_path.startswith(current_dir):
        return folder_path[len(current_dir) + 1:]
    return folder_path
clear()
Path=os.getcwd()
while True:
    print(f'Path : {Path}')
    open_folder(Path)
    print("\n")
    print("1.Open Folder")
    print("2.Open File")
    print("3.Back")
    print("9.Exit")
    print("\n")
    ch=int(input("Enter Choice : "))
    if ch==1:
        folder_N=int(input("Enter Folder Number : "))-1
        if folder_N>=0:
            folder=os.listdir(Path)[folder_N]
            relative_folder_path = get_relative_folder_path(folder)
            if relative_folder_path:
                Path=os.getcwd()
                Path=os.path.join(Path,relative_folder_path)
                open_folder(folder)
                os.chdir(Path) 
                print('\n')     
        else:
            print("Invalid folder number.")  
        clear()              
    elif ch==2:
        file_n = int(input("Enter File No : "))-1
        if file_n>0:
            file_name = os.listdir(Path)[file_n]
            file_path = get_file_path(file_name,Path)
            if file_path:
                os.startfile(file_path)
            else:
                print(f"File '{file_name}' not found.")    
        else:
            print("Invalid file number.")
        clear()
    elif ch==3:
        os.chdir('..') 
        Path=os.getcwd()
        clear()
    elif ch==9:
        clear()
        break
    else:
        clear()
        print("Invalid Choice")