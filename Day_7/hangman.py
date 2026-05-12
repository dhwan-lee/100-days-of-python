import random
import hangman_words
#  from hangman_words import word_list
from hangman_arts import stages, logo

chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
 
print(placeholder)  
is_game_over = False

correct_letters = []
lives = 6

print(logo)

while not is_game_over:
    print(f"***********************{lives}/6 LIVES LEFT***********************")
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print("You've already guessed " + guess)
    display = ""

    for c in chosen_word:
        if guess == c:
            display += c
            correct_letters.append(c)
        elif c in correct_letters: 
            display += c
        else:
            display += "_"

    print(display)
    if guess not in display:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word, You lose a life.")
        if lives == 0:
            is_game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE***********************")


    if not "_" in display:
        is_game_over = True
        print("***********************YOU WIN***********************")

    print(stages[lives])