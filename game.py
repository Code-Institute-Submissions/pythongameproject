# from byotest import *

# print("All tests pass")

print("Welcome to the Riddle game!")

guess = 0

while True:
    print("Enter your guess below! For a hint type 'hint', or, if you give up, type: 'I give up'")
    print("Which is the animal that walks with four legs in the morning, two in the afternoon and three at night")
    answer = input()
    guess += 1

    if "human" in answer:
        print("You win!")
        print("It took you " + str(guess) + " guesses.")
        sys.exit()
    
    elif answer == "hint":
        print("You are a...")

    elif answer.upper() == "I GIVE UP":
        print("The answer was human!")

    else:
        print("Sorry, keep trying")