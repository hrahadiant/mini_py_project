# basic of simple calculator
# you only calculate between two numbers

subtotal = 0
total = 0


def error_handling(int_type, float_type1, float_type2):
    # check if type of input is correct
    try:
        int(int_type)
        float(float_type1)
        float(float_type2)
    except ValueError:
        print("You enter characters or symbols or selected the wrong operation.\nPlease try again.")
        main()


def break_the_code():
    global subtotal, total
    total = subtotal
    print("Total calculation is {}.\nThanks for using this calculator.".format(total))
    exit()


def operation_list():
    print("Enter the two numbers first and then select the operation.")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. modulus")
    print("6. exit")


def additional_operation(x):
    print("Current total: {}".format(x))
    new_number = float(input("> "))
    if new_number == 6:
        break_the_code()
    else:
        operation_action(x, new_number)


def operation_action(number_one, number_two):
    operation = input("Select the operation: ")
    error_handling(operation, 0, 0)

    if operation == "1":
        add_numbers(number_one, number_two)
    elif operation == "2":
        subtract_numbers(number_one, number_two)
    elif operation == "3":
        multiply_numbers(number_one, number_two)
    elif operation == "4":
        divide_numbers(number_one, number_two)
    elif operation == "5":
        modulus_numbers(number_one, number_two)
    elif operation == "6":
        break_the_code()


def add_numbers(number_one, number_two):
    current = number_one + number_two
    global subtotal
    subtotal = current
    additional_operation(subtotal)


def subtract_numbers(number_one, number_two):
    current = number_one - number_two
    global subtotal
    subtotal = current
    additional_operation(subtotal)


def multiply_numbers(number_one, number_two):
    current = number_one * number_two
    global subtotal
    subtotal = current
    additional_operation(subtotal)


def divide_numbers(number_one, number_two):
    current = number_one / number_two
    global subtotal
    subtotal = current
    additional_operation(subtotal)


def modulus_numbers(number_one, number_two):
    current = number_one % number_two
    global subtotal
    subtotal = current
    additional_operation(subtotal)


def main():
    operation_list()

    number_one = input("> ")
    number_two = input("> ")
    error_handling(0, number_one, number_two)

    # convert the number to float
    number_one = float(number_one)
    number_two = float(number_two)

    operation_action(number_one, number_two)


main()
