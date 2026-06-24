from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

SIMILAR_ACCOUNT = "chefsteps"   # the account whose followers you'll follow
USERNAME = "dhwanyi@gmail.com"       # your Share-a-Naan (or Instagram) username (your email)
PASSWORD = "3wpODg93Dw5tbuJD"   
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)  # keep the browser open
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(LOGIN_URL)

        sleep(2)

        username_input = self.driver.find_element(By.ID, value="username")
        username_input.send_keys(USERNAME)

        sleep(1)
        password_input = self.driver.find_element(By.ID, value="password")
        password_input.send_keys(PASSWORD, Keys.ENTER)

        try:
            login_info = self.driver.find_element(By.XPATH, value='//*[@id="popup-save-login"]/div/div[2]')
            login_info.click()
            print("Clicked 'Save Login Info'.")
        except Exception:
            print("Save Login Info pop-up not found, skipping.")

        sleep(1) # Brief pause between pop-ups

        # Handle "Turn off Notifications" Pop-up Safely
        try:
            turn_off_notification = self.driver.find_element(By.XPATH, value='//*[@id="popup-notifications"]/div/button[2]')
            turn_off_notification.click()
            print("Clicked 'Turn off Notifications'.")
        except Exception:
            print("Notifications pop-up not found, skipping.")

    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}/followers")
        sleep(2)

        modal = self.driver.find_element(By.CSS_SELECTOR, value=".followers-scroll")
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(1)

    def follow(self):
        all_btns = self.driver.find_elements(By.CSS_SELECTOR, value=".followers-scroll button")
        for button in all_btns:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                # An "Unfollow?" dialog opened (you already follow this account).
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()