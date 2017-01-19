# coding : utf-8
import os
import psutil

# Комментарий
print("Hello (Привет)")
name = input("Your name: ")
print("Hello,", name)

answer = input("Lets work? (Y/N):")

# PEP-8
if answer == 'Y':
	print("What do you want to do:")
	print("1. List dirrectories")
	print("2. Testing")
	print("3. List of PIDs")
	
	do = int(input("What you would choose: "))
	if do == 1:
		print(os.listdir())
	elif do == 2:
		pass
	elif do == 3:
		print(psutil.pids())
	else:
		pass
	
elif answer == 'N':
	print("Bad job")
else:
	print("Repeat, please")