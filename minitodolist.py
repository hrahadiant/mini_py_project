import os

# initialize a list
task = []
# check current python file path
currentpath = os.path.dirname(os.path.realpath(__file__))
# set name of the file
filename = "my_todo.txt"
# set directory to save the file
filepath = os.path.join(currentpath, filename)


# function for check the file is exist and is empty or not
def open_list():
	if os.path.isfile(filepath) == True:
		file = open(filepath, 'r')
		if os.stat(filepath).st_size > 0:
			print("Here's your current todo in your file.")
			with file as f:
				for line in f:
					print(line)
		else:
			print("Your current todo is empty.")
	else:
		file = open(filepath, 'w+')
		print("File is successfully created on {}.".format(currentpath))
	file.close()
	save_message()


def save_message():
	print("Save another list..")


# function for clear the screen
def clear():
	if os.system == "cls":
		os.system('cls')
	else:
		os.system('clear')


# function for show current todo
def show_task():
	if len(task) == 0:
		print("Your current list is empty.")
	else:	
		print("Here's your current list.")
		for listing in task:
			print("- {}".format(listing))


def close():
	print("Thank you for use this apps.")
	exit_question = input("Are you sure? (y/n) ")
	if exit_question == "y" :
		exit()
	elif exit_question == "n":
		pass
	else:
		print("Sorry, your typing is wrong.")


def show_help():
	print("Here's a command for using the apps.")
	print("type show, to show your current list.")
	print("type help, to see this message.")
	print("type remove, to remove your selected list.")
	print("type save, to save current list into file.")
	print("type quit or q, to close the apps")


def welcome_msg():
	welcome = print("Welcome to to-do list. Just type and save!")
	notif = input("Press enter to continue or q to quit, or help to get help. ")
	if notif.lower() == "q":
		exit()
	elif notif.lower() == "help":
		show_help()
	else:
		open_list()

welcome_msg()

while True:
	todo = input("> ")

	if todo == "show":
		clear()
		show_task()
	elif todo == "q" or todo == "quit":
		close()
	elif todo == "help":
		clear()
		show_help()
		continue
	elif todo == "remove":
		clear()
		show_task()
		item_to_remove = input("Choose one item you want to remove from the list. ")
		idx = int(item_to_remove) - 1
	
		try:
			int(item_to_remove)
		except TypeError:
			print("Only type a number, please.")
		except IndexError:
			print("the list of index is out of range")
		else:
			print("{} has been removed from current list.".format(task[idx]))
			del task[idx]
			continue
	elif todo == "save":
		pass
	else:
		task.append(todo)
