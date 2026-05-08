print("Welcome to the tip calculator!")
total = int(input("What was the total bill? $"))
percentage_of_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill_per_person =  total * (1 + percentage_of_tip/100) / number_of_people
print(f"Each person should pay: ${bill_per_person:.2f}")
