import calculator_art

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/".
operation_dictionaries = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(calculator_art.logo)
    
    should_accumulate = True
    num1 = float(input("What's the first number?: "))
    
    while should_accumulate:
        for symbol in operation_dictionaries:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operation_dictionaries[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() 
calculator()

# Another version!
# should_continue = True
# user_response = 'n'
# def find_chosen_operation(selected_operation):
#     if selected_operation == "+":
#         return add
#     elif selected_operation == "-":
#         return subtract
#     elif selected_operation == "*":
#         return multiply
#     elif selected_operation == "/":
#         return divide
#     else:
#         return "undefined"

# while should_continue:
#     if user_response == 'n':
#         print("\n"*5)
#         print(calculator_art.logo)
#         first_number = int(input("What's the first number?: "))
#     else:
#         first_number = calculated_result

#     picked_operation = input("+\n-\n*\n/\nPick an operation: ")
#     favorite_operation = find_chosen_operation(picked_operation)
#     second_number = int(input("What's the next number?: "))
#     if favorite_operation != "undefined":
#         calculated_result = favorite_operation(first_number, second_number)
#     else:
#         calculated_result = 0
#         picked_operation = "undefined"

#     print(f"{first_number} {picked_operation} {second_number} = {calculated_result}")
#     user_response = input(f"Type 'y' to continue calculating with {calculated_result}, or type 'n' to start a new calculation: ")

