import random
# variables which use in the program
guess_limit = 6
trial_no=0
guees_words=[]

def Handman():
    print("<===== Welcome to Handman =====>\n")
    predefine_words=['Python','Java','Cpp','C','Ruby']
    word = random.choice(predefine_words)
    
    # show the hidden txt on the console
    display_screen=['_']*len(word)

    while trial_no >= guess_limit:

        print("Word: ".join(display_screen))
        print(f'Trial Number: {trial_no}')
        print(f'Remaning Limit: {guess_limit}')

        user_input = input("Enter a words").capitalize()

        if len(user_input)!= 1 or user_input.isalpha()==False:
            print("Invalid Input! Please enter a single alphabetic character.")
            continue
        


    

    



Handman()