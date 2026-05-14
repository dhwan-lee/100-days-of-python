import guess_number_art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

generated_number = random.randint(0, 100)
turns = 0

def greeting():
    print(guess_number_art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def check_answers(guessed_number, generated_number, turns):
    """Check the answer against guess, returns the number of turns reamining"""
    if guessed_number < generated_number:
        print("Too low.")
    elif guessed_number > generated_number:
        print("Too high.")
    elif guessed_number == generated_number:
        print(f"You got it! The answer was {generated_number}")

    return turns - 1

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def play_game():
    turns = set_difficulty()

    guessed_number = -1

    while generated_number != guessed_number:
        print(f"You have {turns} attempts remaining guess the number.")
        guessed_number = int(input("Make a guess: "))
        
        turns = check_answers(guessed_number, generated_number, turns)
        
        if generated_number != guessed_number:
            print("Guess again")
        
        if turns == 0:
            print("You've run out of guess. Refresh the page to run again.")
            return


greeting()
play_game()
