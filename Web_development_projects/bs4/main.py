from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
# print(response.text)

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


article_upvote = soup.find_all(name="span", class_="score").getText()

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_number = article_upvotes.index(largest_number)

print(article_texts[largest_number])
print(article_links[largest_number])
# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# # heading = soup.find(name="h1", id="name")
# # print(heading)



# # company_url = soup.select_one(selector="p a")
# # print(company_url)

# # name = soup.select_one(selector="#name")
# # print(name)

# headings = soup.select(".heading")
# print(headings)
