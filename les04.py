# coding : utf-8
import os
import sys
import psutil
import shutil
import multiprocessing

# Комментарий
print("Hello (Привет)")
#name = input("Your name: ")
#print("Hello,", name)

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
		
		do = int(input("What you would choose: "))
		if do == 1:
			print(os.listdir())
		elif do == 2:
			print("Current directory name:", os.getcwd())
			print("Current os platform:", sys.platform)
			print("Current file system encoding:", sys.getfilesystemencoding())
			print("Current user login:", os.getlogin())
			print("Count CPU:", psutil.cpu_count())
		elif do == 3:
			print(psutil.pids())
		elif do == 4:
			fileList = os.listdir()
			i = 0
			while i < len(fileList):
				newFileName = fileList[i] + '.dublicate'
				shutil.copy(fileList[i], newFileName)
				i += 1
		else:
			pass
	elif answer == 'N':
		print("Bad job")
	else:
		print("Good bye!")