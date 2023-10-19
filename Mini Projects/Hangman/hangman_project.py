import random
from hangman_words import word_list
import hangman_art
from hangman_art import logo
from hangman_art import stages
print(logo)

game_word = random.choice(word_list)
word_length = len(game_word)
end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in game_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if guess in display:
        print(f"You've already guessed {guess}")
        continue

    for position in range(word_length):
        letter = game_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
