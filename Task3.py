# TASK 4: Basic Chatbot 
# Goal: Build a simple rule-based chatbot. 
# Scope: 
# ● Input from user like: "hello", "how are you", "bye". 
# ● Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!". 
# Key Concepts Used: if-elif, functions, loops, input/output.

def ChatBot(user):
    print(f"Welcome: {user}")

    while True:
        prompt=input("Enter your message:> ").lower()

        if(prompt == 'hi'):
            print(f"ChatBot: Hello {user}")
        elif(prompt == 'how are you'):
            print("ChatBot: I am Good Thank you \nWhat about yout")
        elif(prompt == 'bey'):
            print(f"ChatBot: Good Bey {user} see you again")
            break
        else:
            print("Thinking....")




username=input("Enter your name : ")
ChatBot(username)