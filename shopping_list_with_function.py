# basic shopping list with function and clean code
# has 3 command in this apps
# SHOW, HELP, and DONE

print("enter a new list for you...")

shopping_list = []

# function to show the help
def show_help():
    print("typing SHOW, to show the current list")
    print("typing HELP, to see how to use this apps")
    print("typing DONE, to print out your list")

# function for show the list
def show_list():
    print("Here is your list:")
    for item in shopping_list:
        print(item)

# function to add a new item into the list
def add_to_list(item):
    shopping_list.append(item)
    print("You just added {}. List now has {} items.".format(item, len(shopping_list)))

show_help()

while True:
    items = input("> ")
    if items == "SHOW":
        show_list()
        continue
    elif items == "DONE":
        break
    elif items == "HELP":
        show_help()
        continue
    add_to_list(items)
