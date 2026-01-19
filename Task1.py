import random


def Handman():
    # variables which use in the program
    guess_limit = 6
    trial_no=0
    guees_words=[]
    print("<===== Welcome to Handman =====>\n")
    predefine_words=['python','java','cpp','c','ruby']
    word = random.choice(predefine_words)
    
    # show the hidden txt on the console
    display_screen=['_']*len(word)

    while trial_no < guess_limit:
        print("Word: ".join(display_screen))
        print(f'Trial Number: {trial_no}')
        print(f'Remaning Limit: {guess_limit}')

        user_input = input("Enter a words: ").lower()
        if len(user_input)!= 1 or user_input.isalpha()==False:
            print("Invalid Input! Please enter a single alphabetic character.")
            continue

        if user_input in guees_words:
            print("Error: Letter alread enter ")
            continue

        guees_words.append(user_input)
        if user_input in word:
            print("-> Correct letter Guess")
            for i in range(len(word)):
                if word[i] == user_input:
                    display_screen[i]=user_input
        else:
            print("Error: user input is invalid")
            trial_no = trial_no + 1

        if '_' not in display_screen:
            print("You are Won ")
            return
    print("You are loss")



Handman()