# import logo, game_data, random
import higher_lower_game_art
import game_data
import random

def format_data(account):
    """Takes the account data and returns a printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_followers(guess, a_follower, b_follower):
    """Checks followers against user's guess and returns True if they got it right."""
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'            

def play():
    score = 0
    game_should_continue = True

    account_b = random.choice(game_data.data)

    while game_should_continue:
        print(higher_lower_game_art.logo)
        
        if score > 0:
            print(f"You're right! Current score {score}")
        
        account_a = account_b

        while account_a == account_b:
            account_b = random.choice(game_data.data)

        print(f"Compare A: {format_data(account_a)}")
        print("\n" + higher_lower_game_art.vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers?: Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        game_should_continue = check_followers(guess, a_follower_count, b_follower_count)

        if game_should_continue:
            score += 1
        else:
            print("\n" * 20)
            print(higher_lower_game_art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")

play()
