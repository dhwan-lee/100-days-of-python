from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS selectors
# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[1]/a')
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

# # Find the element by Link Texxt
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# # Find the "Search" <input> by Name
# search = driver.find_element(By.NAME, value="search")

# # Sending keyboard input to Selenium
# search.send_keys("Python", Keys.ENTER)


# Challenge
# Navigate to the (fake) newsletter registration page
driver.get("https://appbrewery.github.io/fake-newsletter-signup/index.html")

# Find the first name, last name, and email fields
first_name = driver.find_element(By.NAME, value="fName")

last_name = driver.find_element(By.NAME, value="lName")

email_address = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Who")
last_name.send_keys("am I")
email_address.send_keys("whoamI@gmail.com")

# Locate the "Sign Up" button. Then, click on it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
# driver.quit()