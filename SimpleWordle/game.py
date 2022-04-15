import random

# Very simple version of Wordle
# Made because I couldn't sleep

attempt = 0

with open("valid-wordle-words.txt", "r") as f:
    words = [w for w in f]

wordle = random.choice(words)
print(wordle)
guesses = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-']
]
print(guesses)

print("Welcome to SimpleWordle!")
print("Capitalized letters = letter in correct spot")
print("You have 6 attempts! Have fun!")

while (attempt < 6):
    guess = input("Attempt #" + str(attempt) + ": ")
    guess += chr(10)
    if (len(guess) != 6 and guess not in words):
        print("Your guess is invalid! Try again")
        continue
    elif(str(guess).lower() == str(wordle).lower()):
        print(guess.upper())
        print("CORRECT!")
        break
    else:
        for i in range(5):
            if guess[i] == wordle[i]:
                guesses[attempt][i] = wordle[i].upper()
            else:
                for j in range(5):
                    if guess[j] == wordle[i]:
                        guesses[attempt][j] = wordle[i]
        print(guesses[attempt])
    attempt += 1

if (attempt >= 6):
    print("The Wordle was " + wordle.upper())
