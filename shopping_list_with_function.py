# basic shopping list with function and clean code
# has 3 command in this apps
# SHOW, HELP, and DONE
# add new command to save the list to my_shopping_list.txt

print("enter a new list for you...")

shopping_list = []
file_name = "my_shopping_list.txt"


# function to show the help
def show_help():
    print("typing SHOW, to show the current list")
    print("typing HELP, to see how to use this apps")
    print("typing DONE, to print out your list")
    print("typing SAVE, to save your list to file")


# function for show the list
def show_list():
    print("Here is your list:")
    for item in shopping_list:
        print(item)


# function to add a new item into the list
def add_to_list(item):
    shopping_list.append(item)
    print("You just added {}. List now has {} items.".format(item, len(shopping_list)))


def save_to_file():
    file = open(file_name, "r")
    if len(file.readline()) == 0:
        write_to_file = open(file_name, "w")
        for n in shopping_list:
            write_to_file.write(n + '\n')
        write_to_file.close()
    else:
        append_to_file = open(file_name, "a")
        for n in shopping_list:
            append_to_file.write(n + '\n')
        append_to_file.close()
    file.close()
    print("New list already save to {}".format(file_name))

show_help()

while True:
    items = input("> ")
    if items == "SHOW":
        show_list()
        continue
    elif items == "DONE":
        read_file = open(file_name, "r")
        print("Your current shopping list:")
        for line in read_file:
            print(line)
        break
    elif items == "HELP":
        show_help()
        continue
    elif items == "SAVE":
        save_to_file()
        continue
    add_to_list(items)
