import smtplib
import datetime as dt
import random

now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)

my_email = "dhwanyi@gmail.com"
password = "abcd1234()"

if day_of_week == 4:


    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=my_email, 
                            msg=f"Subject:Today's Motivation\n\n{quote}"
        )



