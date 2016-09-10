# shopping list with function

# instruction
print("Follow the short instruction: ")
print("enter a word SHOW, to show list")
print("enter a word HELP, to see how to use this apps")
print("enter a word DONE, to completely the list")
print("\n")
print("enter a new shopping list")

def mylist():
    shopping_list = []
    while True:
        items = input("> ")
        if items == "SHOW":
            if len(shopping_list) == 0:
                print("you have nothing in your list")
                mylist()
            elif len(shopping_list) != 0:
                for i in shopping_list:
                    print(i)
                mylist()
        elif items == "DONE":
            break
        elif items == "HELP":
            print("add one list at once a time.")
            print("type SHOW, to see full list")
            print("type DONE, to completely list")
            print("type HELP, to see how to use this app")
            mylist()
        else:
            shopping_list.append(items)
