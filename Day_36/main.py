import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_API_KEY = os.environ.get("OWN_MY_API_KEY")
MY_SECOND_API_KEY = os.environ.get("OWN_MY_SECOND_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": MY_API_KEY, 
}

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔻"
if difference > 0:
    up_down = "🔺"

diff_percentage = round(abs(difference) / float(yesterday_closing_price) * 100)

# if diff_percentage > 5:
#     print("Get News")

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_params = {
    "apiKey": MY_SECOND_API_KEY,
    "q": COMPANY_NAME,
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_response.raise_for_status()
articles = news_response.json()["articles"]
three_articles = articles[:3]

formatted_articles = [f"{STOCK}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
if diff_percentage > 1:
    print(formatted_articles)

