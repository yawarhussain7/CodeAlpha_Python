import random
# variables which use in the program
guess_limit = 6
trial_no=0
guees_words=[]

def Handman():
    predefine_words=['Python','Java','Cpp','C','Ruby']
    word = random.choice(predefine_words)
    print(word)



Handman()