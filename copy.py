import random

from hangman_art import stages, logo

print(logo)


lives = len(stages)-1
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)
display = []

for l in chosen_word:
    display += '_'
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("you lost!!")
            print(chosen_word)
    print(f"You have {lives} lives left:")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = str(letter)

if '_' not in display:
    end_of_game = True
    print("you win")
