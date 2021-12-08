import random

from hangman_art import stages, logo

print(logo)
end_of_game = False

lives = len(stages)-1
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length=len(chosen_word)
print(chosen_word)
display = []

for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("you lost!!")
            print(chosen_word)
    print(f"You have {lives} lives left:")


    if '_' not in display:
        end_of_game = True
        print("you win")
    print(stages[lives])