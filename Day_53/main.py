import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

ZILLOW_CLONE_URL = "http://appbrewery.github.io/Zillow-Clone/"

header = {
    "User_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Accept_language": "en-US,en;q=0.5",
}

response = requests.get(ZILLOW_CLONE_URL, headers=header)
# print(response.raise_for_status())
data = response.text
# print(data)
soup = BeautifulSoup(data, "html.parser")
# print(soup)

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
# print(all_link_elements)
all_links = [link["href"] for link in all_link_elements]
# print(f"There are {len(all_links)} links to individual listings in total: \n")
# print(all_links)

# Create a list of all the addresses on the page using a CSS Selector
# Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
# print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
# print(all_addresses)

# Create a list of all the prices on the page using a CSS Selector
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
# print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
# print(all_prices)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf77l6DhQMkZkWAsLz9Ut-p6vq0-KmDIylVeZOMBp-CTGz2zw/viewform?usp=header")
    sleep(2)

    # Use the xpath to select the "short answer" fields in your Google Form. 
    # Note, your xpath might be different if you created a different form.
    address = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
    sleep(2)
    
    # Locate and click the "Submit another response" link to reset the form
    # Google Forms standard structure uses a specific anchor tag layout for this link
    another_response_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response_btn.click()
    
    # Wait for the fresh form fields to load before iterating next row
    sleep(2)