from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/aW03fmzbsWtnBB6ttyFoT6p0VylEKjTa"
FACEBARK_ID = "dddd@test.com"
FACEBARK_PASSWORD = "1111"

# Create ChromeOptions and pass the detach experimental option
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Pass the options into your driver initialization
driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDOG_URL)

sleep(2)
login_btn = driver.find_element(By.XPATH, value='/html/body/header/button')
login_btn.click()

sleep(1)
facebark_btn = driver.find_element(By.XPATH, value='//*[@id="login-modal"]/div/div/div/button[1]')
facebark_btn.click()

sleep(2)
base_window = driver.window_handles[0]
facebark_window = driver.window_handles[1]
driver.switch_to.window(facebark_window)
print(driver.title)

email = driver.find_element(By.ID, value="email")
password = driver.find_element(By.ID, value="pass")
email.send_keys(FACEBARK_ID)
password.send_keys(FACEBARK_PASSWORD)
password.send_keys(Keys.ENTER)

sleep(2)
driver.switch_to.window(base_window)
print(driver.title)

# sleep(1)
# allow_location = driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button')
# allow_location.click()

# sleep(1)
# not_interested = driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button[2]')
# not_interested.click()

# sleep(1)
# accept_cookies = driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button')
# accept_cookies.click()

sleep(3)
driver.find_element(By.XPATH, value='//button[text()="Allow"]').click()
sleep(1)
driver.find_element(By.XPATH, value='//button[text()="Not interested"]').click()
sleep(1)
driver.find_element(By.XPATH, value='//button[text()="I Accept"]').click()

for n in range(20):
    sleep(1)
    try:
        like_btn = driver.find_element(By.XPATH, value='//*[@id="like-button-container"]/form/button')
        like_btn.click()
    except ElementClickInterceptedException:
        # Match popup is in the way — dismiss it and continue
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        # Like button not loaded yet OR all dogs have been swiped — wait and retry
        sleep(2)

driver.quit()