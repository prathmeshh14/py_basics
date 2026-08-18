from pathlib import Path

def rename(folder, lst):
    for file in folder.iterdir():
        if file.is_file():
            print("Current File:", file.name)
            new_name=input("Enter the new file name:")
            new_path=folder/(new_name+file.suffix)
            file.rename(new_path)
            lst.append(new_path)
    print("File name changed sucessfully")

def display(lst):
    for number,file in enumerate(lst,start=1):
        print(number,file.name)

def remove(folder, lst):
    display(lst)
    file_name=input("Enter the file name to delete:")
    check_status=input("Are you sure to delete the file y/n:").lower()
    if check_status=="y":
        file_path=folder/file_name
        if file_path.exists():
            file_path.unlink()
        else:
            print("File not Found")
    else:
        print("File is not removed")

def main():
    lst=[]
    folder=Path(input("Enter the name of the Folder:"))
    print("\n1.Rename\n2.Display\n3.Remove")
    choice=input("Enter you choice:")
    match choice:
        case "1":
            rename(folder, lst)
        case "2":
            display(lst)
        case "3":
            remove(folder, lst)
        case _:
            print("Please enter a valid input")

if __name__ == "__main__":
    main()

