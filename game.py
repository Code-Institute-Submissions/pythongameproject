# from byotest import *

# print("All tests pass")
def show_menu():
    print("1. Play the Riddle Game!")
    print("2. Add your Riddle")
    print("3. Quit")
    
    option = input("Enter option number: ")
    return option
    
def ask_riddles():
    riddles = []
    answers = []
    
    with open("riddles.txt", "r") as file:
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines):
        if i%2 == 0:
            riddles.append(text)
        else:
            answers.append(text)
    
    number_of_riddles = len(riddles)
    riddles_and_answers = zip(riddles, answers)
    
    score = 0
            
    for riddle, answer in riddles_and_answers:
        guess = input(riddle + "> ")
        if answer in guess:
            score += 1
            print("That's right! Well done!")
            print(score)
        else:
            if (sum([i[0] != ' '  for i in difflib.ndiff(guess, answer)]) / 2) <= 2:
                print(sum([i[0] != ' '  for i in difflib.ndiff(guess, answer)]))
                print("Spelling needs checking, but we'll accept it!")
                score += 1
                print(score)
            else:
                print("Sorry, mate, that's not right...")
    
    print("You got {0} correct out of {1}. Thank you for playing!".format(score, number_of_riddles))

def add_riddle():
    print(" ")
    riddle = input("Enter your Riddle \n> ")

    print(" ")
    print("Thank you! What is the answer? \n> ")
    answer = input("{0}\n> ".format(riddle))
    
    file = open("riddles.txt","a")
    file.write(riddle + "\n")
    file.write(answer + "\n")
    file.close()


#print("Welcome to the Riddle game!")
#guess = 0

def game_loop():   
    while True:
        option = show_menu()
        if option == "1":
            ask_riddles()
        elif option == "2":
            add_riddle()
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")
        
game_loop()
       
#        print("Enter your guess below! For a hint type 'hint', or, if you give up, type: 'I give up'")
#        print("Your first riddle is: \n 'What creature walks on four legs in the morning, two legs in the afternoon, and three legs in the evening'")
#        answer = input()
#        guess += 1
#
#        if "human" in answer:
#            print("You win!")
#            print("It took you " + str(guess) + " guesses.")
#            sys.exit()
    
#        elif answer == "hint":
#            print("You are a...")

#        elif answer.upper() == "I GIVE UP":
#            print("The answer was 'human'!")

#        else:
#            print("Sorry, keep trying")
        
        
# There are 2 sisters: one gives birth to the other and she, in turn, gives birth to the first. Who are the two sisters? Day and Night