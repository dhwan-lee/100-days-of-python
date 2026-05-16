MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}

a = "ingredients"
b = "water"
c = "milk"
d = "coffee"


# Print report that shows the current resource values
def resources_statement():
    s = ""
    for key in resources:
        unit = "ml"
        if key == "coffee":
            unit = "g"
        
        s += key.title() + ": " + str(resources[key]) + unit + "\n"

    s += "Money: $" + str(money["value"])
    
    return s

def get_coins():
    print("Please insert coins: ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


def check_resource_sufficient(coffee):
    """Checks if there are enough ingredients and prints which one is missing."""
    # if coffee == "espresso":
    #     if MENU[coffee][a][b] <= resources[b] and MENU[coffee][a][d] <= resources[d]:
    #         return True
    # else:
    #     if MENU[coffee][a][b] <= resources[b] and MENU[coffee][a][c] <= resources[c] and MENU[coffee][a][d] <= resources[d]:
    #         return True 

    # return False
    recipe = MENU[coffee]["ingredients"]
    for item in recipe:
        if recipe[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def check_coins(coin, coffee):
    if coin >= MENU[coffee]["cost"]:
        return True
    
    return False

def refund(coin, coffee):
    """Returns the total calculated from coins inserted"""
    if coin > MENU[coffee]["cost"]:
        rest = coin - MENU[coffee]["cost"]
    
    print(f"Here is ${rest:.2f} in change.")

def make_coffee(coffee):
    """Deduct the requried ingredients from the resources"""
    if coffee == "espresso":
        resources[b] -= MENU[coffee][a][b]
        resources[d] -= MENU[coffee][a][d]
            
    else:
       resources[b] -= MENU[coffee][a][b] 
       resources[c] -= MENU[coffee][a][c]
       resources[d] -= MENU[coffee][a][d]


def coffee_machine():
    should_continue = True
    is_sufficient = True
    enough_money = False

    while should_continue: 
        # Prompt user by asking “What would you like? (espresso/latte/cappuccino)
        user_response = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_response == "report":
            print(resources_statement())
        elif user_response == "off":
            print("End this program. Hope to see you next time:)")
            should_continue = False
        else:
            
            is_sufficient = check_resource_sufficient(user_response)
            
            if is_sufficient:
                coins = get_coins()
                enough_money = check_coins(coins, user_response)

                if not enough_money:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    money["value"] += MENU[user_response]["cost"]
                    refund(coins, user_response)
                    make_coffee(user_response)
                    print(f"Here is your {user_response} ☕️ Enjoy!")

coffee_machine()