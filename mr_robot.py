# coding: utf-8
import os
import sys
import psutil
import shutil
import random


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


def double_files(directoryname):
    file_list = os.listdir(directoryname)
    i = 0
    while i < len(file_list):
        duplicate_file(file_list[i])
        i += 1


def random_delete(directoryname):
    file_list = os.listdir(directoryname)
    if file_list:
        position = random.randrange(0, len(file_list))
        print("file position for delete: " + str(position + 1) + ". file name for delete: " + file_list[position])
        fullname = os.path.join(directoryname, file_list[position])
        if os.path.isfile(fullname):
            os.remove(fullname)


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
            print("7. Delete random file")

            do = int(input("What you would choose: "))
            if do == 1:
                print(os.listdir())

            elif do == 2:
                sys_info()

            elif do == 3:
                print(psutil.pids())

            elif do == 4:
                print("Double file in current directory")
                double_files('.')

            elif do == 5:
                print("Copy file file")
                filename = input("Set file name: ")
                duplicate_file(filename)

            elif do == 6:
                directoryname = input("Please, set directory: ")
                print("Count of deleted files: " + str(del_duplicate(directoryname)))

            elif do == 7:
                directoryname = input("Please, set directory: ")
                random_delete(directoryname)

            elif do == 8:
                directoryname = input("Please, set directory: ")
                fileList = os.listdir(directoryname);
                i = 0
                while i < len(fileList):
                    fullName = os.path.join(directoryname, fileList[i])
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