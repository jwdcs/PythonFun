import random

# Very simple version of Wordle
# Made because I couldn't sleep

attempt = 0

with open("valid-wordle-words.txt", "r") as f:
    words = [w for w in f]

wordle = random.choice(words)
# print(wordle)

print("Welcome to SimpleWordle!")
print("Capitalized letters = letter in correct spot")
print("Have fun!")

while (attempt <= 6):
    guess = input("Attempt #" + str(attempt) + ": ")
    if (len(guess) != 5):
        print("Your guess must be 5 characters! Try again")
        continue
    if(guess == wordle):
        print(guess.upper())
        print("CORRECT!")
        break
    else:
        result = ""
        for i in range(len(wordle) - 1):
            if(guess[i] == wordle[i]):
                result += guess[i].upper()
            else:
                result += guess[i]
        print(result)
    attempt += 1

if (attempt > 6):
    print("The Wordle was " + wordle.upper())
