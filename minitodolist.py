import os
task = []


def clear():
	if os.system == "cls":
		os.system('cls')
	else:
		os.system('clear')


def show_task():
	if len(task) == 0:
		print("Your current list is empty.")
	else:	
		num = 1
		print("Here's your current list.")
		for listing in task:
			print("{}: {}".format(num, listing))
			num += 1


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
	print("type quit or q, to close the apps")


def welcome_msg():
	welcome = print("Welcome to to-do list. Just type and save!")
	notif = input("Press enter to continue or q to quit, or help to get help. ")
	if notif.lower() == "q":
		exit()
	elif notif.lower() == "help":
		show_help()

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
	else:
		task.append(todo)
