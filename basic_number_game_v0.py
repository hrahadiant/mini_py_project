# basic number game
import random
# rules
# you must enter the integer
# for win this game, you must hit the secret number within 3 chances

print("Basic rules:")
print("You only have 3 chances to guess the number")
print("You can type the integer between 1-10 only")
print("You can choose play again when you lose")
print("Enjoy this game!")

guess_limit = 3


def play_again():
    play_more = input("Do you want to play again? y/n ")
    if play_more.lower() == "n":
        print("Bye!")
        exit()
    elif play_more.lower() == "y":
        main()


def check_number(number, hit):
    global guess_limit
    guess_limit -= 1

    number = int(number)

    if number == hit:
        print("You hit the number!")
        play_again()
    elif number > hit:
        print("Your guess is too high.")
        print("Try another number. Remaining number of guesses is {}".format(guess_limit))
    elif number < hit:
        print("Your guess is too low.")
        print("Try another number. Remaining number of guesses is {}". format(guess_limit))

    if guess_limit == 0:
        print("Sorry, you lose this game. My secret number is {}".format(hit))
        play_again()


def check_hit(number):
    try:
        int(number)
    except ValueError:
        print("Please input the integer between 1 - 10")
        main()


def main():
    hit_number = random.randint(1, 10)

    while True:
        guess_number = input("Guess the number (1 - 10)> ")
        check_hit(guess_number)
        check_number(guess_number, hit_number)

main()
