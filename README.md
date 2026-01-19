# CodeAlpha_Python
internship Python 
<h2> <--------------------- Task 1 ----------------------->  </h2>
# Hangman Game (Python)

A simple **text-based Hangman game** written in Python for beginners. The player guesses a word one letter at a time with a limited number of attempts.

---
## Features
* Uses **5 predefined words**
* Maximum **6 wrong attempts** allowed
* **Console-based** (no graphics or audio)
* Prevents **repeated letter guesses**
* Beginner-friendly logic

---
##  Concepts Used
* `random` module
* `while` loop
* `if-else` conditions
* Strings & Lists
* Basic input/output

---
##  How to Run

1. Make sure **Python 3** is installed on your system
2. Save the program as `hangman.py`
3. Open terminal / command prompt
4. Run the command:

   ```bash
   python hangman.py
   ```

---
## How the Game Works

* A random word is selected from the list
* The word is hidden using `_` characters
* Player enters **one letter at a time**
* Correct guesses reveal the letter
* Wrong guesses reduce remaining attempts
* Game ends when:

  *  All letters are guessed (Win)
  *  Attempts reach zero (Lose)

---

##  Example Output

```
Word: _ _ _ _ _
Trial Number: 0
Remaining Limit: 6
Enter a letter: a
-> Correct letter Guess
```

---

## 👤 Author

**Yawar Hussain**

Beginner Python Project

