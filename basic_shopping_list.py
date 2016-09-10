# basic shopping list with python
# put the new things into the list, one at a time
# enter the word DONE for quit the program
# once I quit, the app show me everything that's on my list

shopping_list = []

while True:

    # ask for input a new item
    new_item = input("> ")

    # quit the app if new item is "DONE"
    if new_item == "DONE":
        break

    # add a new item into the list
    shopping_list.append(new_item)

# print out all in my list
print("Here is my list:")
for shop_list in shopping_list:
    print(shop_list)
