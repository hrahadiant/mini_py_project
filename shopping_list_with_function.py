# shopping list with function

print("enter a new list for you...")

shopping_list = []


def show_help():
    print("typing SHOW, to show the current list")
    print("typing HELP, to see how to use this apps")
    print("typing DONE, to print out your list")


def show_list():
    print("Here is your list:")
    for item in shopping_list:
        print(item)


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
