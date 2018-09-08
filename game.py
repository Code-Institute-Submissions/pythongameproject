# from byotest import *

# print("All tests pass")

print("Welcome to the Riddle game!")

guess = 0

while True:
    print("Enter your guess below! For a hint type 'hint', or, if you give up, type: 'I give up'")
    print("Your first question is: \n 'What creature walks on four legs in the morning, two legs in the afternoon, and three legs in the evening'")
    answer = input()
    guess += 1

    if "human" in answer:
        print("You win!")
        print("It took you " + str(guess) + " guesses.")
        sys.exit()
    
    elif answer == "hint":
        print("You are a...")

    elif answer.upper() == "I GIVE UP":
        print("The answer was 'human'!")

    else:
        print("Sorry, keep trying")
        
        
# There are 2 sisters: one gives birth to the other and she, in turn, gives birth to the first. Who are the two sisters? Day and Night