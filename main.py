import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = list("_" * word_length)
end_of_game = False
lives = 6
previous_guesses = []

#print(f"Pssst, the solution is {chosen_word}.")
while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = ""

    while len(guess) != 1:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print(
                f"\nYou guessed {guess}, that is an invalid input, please try again.\n"
            )
            guess = ""
    # Clear screen between guesses
    clear()

    # if previous guesses dont take life.
    if guess in previous_guesses:
        print("You have already guessed this. - please try another letter.")

    elif guess not in chosen_word:
        if guess not in previous_guesses:
            previous_guesses.append(guess)
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You Lose")
    else:
        if guess not in previous_guesses:
            previous_guesses.append(guess)
        # check word for letters
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed Letter: {guess}")
            if letter == guess:
                display[position] = guess
    # winning conditions
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    ## output display
    print(f"{display}")
    print(stages[lives])
