import random

# get_guess
# -----
# Repeatedly asks the user for a guess until they
# enter a valid lowercase letter. Returns the guess.
def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        else:
            return guess

# update_dashes
# -----
# This function takes the word, the current state of
# dashes, and the user's last guess. It returns a version
# of dashes with all instances of the guess exposed.
def update_dashes(word, dashes, guess):
    for i in range(len(word)):
        if word[i] == guess:
            dashes = dashes[:i] + guess + dashes[i + 1:]
    return dashes

# List of words
words = ["eggplant", "hello", "turtle"]

# Store word
secret_word = random.choice(words)

# Store dashes
dashes = "-" * len(secret_word)

# Guesses left
guesses_left = 10

# Repeatedly ask for guesses
while guesses_left > 0 and dashes != secret_word:
    print(dashes)
    print(str(guesses_left) + " incorrect guesses left.")

    # Get guess, update game state
    guess = get_guess()
    dashes = update_dashes(secret_word, dashes, guess)
    if guess in secret_word:
        print("That letter is in the secret word!")
    else:
        print("That letter is not in the secret word.")
        guesses_left = guesses_left - 1

# Print result
if guesses_left == 0:
    print("You lose. The word was: " + secret_word)
else:
    print("Congrats! You win. The word was: " + secret_word)