import pandas
import datetime
import random
import smtplib

birthdays = pandas.read_csv("birthdays.csv")
birth_dict = birthdays.to_dict(orient="records")

dt = datetime.datetime
now = dt.now()
month = now.month
day = now.day
is_matched = False

for birth in birth_dict:
    if birth["month"] == month:
        if birth["day"] == day:
            name = birth["name"]
            email = birth["email"]
            is_matched = True

if is_matched:
    letters = []
    with open("letter_templates/letter_1.txt") as letter_file:
        letters.append(letter_file.read())
    
    with open("letter_templates/letter_2.txt") as letter_file:
        letters.append(letter_file.read())
    
    with open("letter_templates/letter_3.txt") as letter_file:
        letters.append(letter_file.read())

letter = random.choice(letters)
final_letter = letter.replace("[NAME]", name)


my_email = "dhwanyi@gmail.com"
my_password = "abcd1234()"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=email, 
                        msg=f"Subject: Happy Birthday!!!!!\n\n{final_letter}"
    )

