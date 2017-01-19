# coding: utf-8
import os
import sys
import psutil
import shutil

def duplicate_file(file_name):
    if os.path.isfile(file_name):
        new_file_name = file_name + '.duplicate'
        shutil.copy(file_name, new_file_name)
        if os.path.exists(new_file_name):
            print("File " + new_file_name + " has been created successfuly")
        else:
            print("Some errors in copiing")


def del_duplicate(directory_name):
    file_list = os.listdir(directory_name);
    count_deleted_files = 0
    for f in file_list:
        full_name = os.path.join(directory_name, f)
        if full_name.endswith(".duplicate"):
            os.remove(full_name)
            if not os.path.exists(full_name):
                count_deleted_files += 1
    return count_deleted_files


def sys_info():
    print("Current directory name:", os.getcwd())
    print("Current os platform:", sys.platform)
    print("Current file system encoding:", sys.getfilesystemencoding())
    print("Current user login:", os.getlogin())
    print("Count CPU:", psutil.cpu_count())


def main():
    # Комментарий
    print("Hello (Привет)")
    # name = input("Your name: ")
    # print("Hello,", name)

    # PEP-8
    answer = ''

    while answer != 'q':
        answer = input("Lets work? (Y/N/q):")
        if answer == 'Y':
            print("What do you want to do:")
            print("1. List dirrectories")
            print("2. USER password")
            print("3. List of PIDs")
            print("4. Dublicate files")
            print("5. Dublicate choosen file")
            print("6. Delete all dublicate files from choosen directory")

            do = int(input("What you would choose: "))
            if do == 1:
                print(os.listdir())

            elif do == 2:
                sys_info()

            elif do == 3:
                print(psutil.pids())

            elif do == 4:
                fileList = os.listdir()
                i = 0
                while i < len(fileList):
                    duplicate_file(fileList[i])
                    i += 1

            elif do == 5:
                i = 0
                fileList = os.listdir()
                while i < len(fileList):
                    print('[' + str(i) + '] ' + fileList[i])
                    i += 1
                choosenFile = int(input("Choose number of file: "))
                shutil.copy(fileList[choosenFile], fileList[choosenFile] + '.duplicate')

            elif do == 6:
                directoryName = input("Please, set directory: ")
                print("Count of deleted files: " + str(del_duplicate(directoryName)))

            elif do == 7:
                directoryName = input("Please, set directory: ")
                fileList = os.listdir(directoryName);
                i = 0
                while i < len(fileList):
                    fullName = os.path.join(directoryName, fileList[i])
                    if fullName.endswith(".duplicate"):
                        os.remove(fullName)
                    i += 1
            else:
                pass
        elif answer == 'N':
            print("Bad job")
        else:
            print("Good bye!")

if __name__ == '__main__':
    main()