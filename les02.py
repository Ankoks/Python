# coding : utf-8
# Комментарий
print("Hello (Привет)")
name = input("Your name: ")
print("Hello,", name)

answer = input("Lets work? (Y/N):")

# PEP-8
if answer == 'Y':
	print("What do you want to do: \n1. Codding \n2. Testing")
elif answer == 'N':
	print("Bad job")
else:
	print("Repeat, please")