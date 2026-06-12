import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.ca/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=sr_1_2?crid=2D9UUUXSRSUB9&dib=eyJ2IjoiMSJ9.y4LLAMvRXyF-GJBFF44YpgoQFm3qlOqvoway1SDbaoXUON6m4rUOGPNlp9k3fsWcTTtWWzPmr1qgqt8dul6Q-AUfqmiQNPMsoNUN6YZDIUkKX4fViMWic7nZk8nA8Czd4oM-HG4P1xg9zLQjYiDWGx1ylheEy9S8l57ty7h9MA58sn5mczGMv8oykJqkd6kbbITgRZKtj9CIREeT6vtzHu8VVmerSKGj0WeAPsQ7Uuy53jv8uOCNZwdWo9qxMLcP3K5Q-08WvF-T9sPUrVZTF5vXn2M-YiBg0epxL5H7GF8.Zui7neaeznb4puBRyO6C5llUN3m6n8qTdqwyPB4dvcM&dib_tag=se&keywords=Instant%2BPot%2BDuo%2BPlus%2B9-in-1%2BElectric%2BPressure%2BCooker%2C%2BSlow%2BCooker%2C%2BRice%2BCooker%2C%2BSteamer%2C%2BSaut%C3%A9%2C%2BYogurt%2BMaker%2C%2BWarmer%2B%26%2BSterilizer%2C%2BIncludes%2BApp%2BWith%2BOver%2B800%2BRecipes%2C%2BStainless%2BSteel%2C%2B3%2BQuart&qid=1781307629&sprefix=%2Caps%2C151&sr=8-2&th=1"

# Full headers
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Dnt": "1",
#     "Priority": "u=0, i",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "CCBot/2.0 (https://commoncrawl.org/faq/)",
# }

# A minimal header
header = {
    "User_agent": "CCBot/2.0 (https://commoncrawl.org/faq/)",
    "Accept_language": "en-US,en;q=0.5",
}
response = requests.get(URL, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
print(soup.prettify())

# Remove the dollar sign using split
price = soup.find(class_="aok-offscreen").get_text()
price_without_currency = price.split("$")[1]
print(price_without_currency)

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

# Email alert when the price is below preset value
title = soup.find(id="productTitle").get_text().strip()
BUY_PRICE = 100
if price_as_float <= BUY_PRICE:
    message = f"{title} is on sale for {price}!"
else:
    exit()

# print(title)
with smtplib.SMTP(os.environ["SMTP_ADDRESS"], 587) as connection:
    connection.starttls()
    result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
    connection.sendmail(
        from_addr=os.environ["EMAIL_ADDRESS"],
        to_addrs=os.environ["EMAIL_ADDRESS"],
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRACTICE_URL}".encode("utf-8")
    )
