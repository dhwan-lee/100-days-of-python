from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_continue = True
is_sufficient = False

track_coffee = CoffeeMaker()
track_money = MoneyMachine()
track_menu = Menu()


while should_continue:
    choice = input(f"What would you like? ({track_menu.get_items()}): ").lower()

    if choice == "report":
        track_coffee.report()
        track_money.report()
    elif choice == "off":
        print("End this program. Hope to see you next time:)")
        should_continue = False
    else:
        drink = track_menu.find_drink(choice)
        
        if drink:
            is_sufficient = track_coffee.is_resource_sufficient(drink)
        
        if is_sufficient:
            track_money.make_payment(drink.cost)
            track_coffee.make_coffee(drink)

