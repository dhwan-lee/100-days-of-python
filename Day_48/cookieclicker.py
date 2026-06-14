from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://ozh.github.io/cookieclicker/")

# Wait for page to load just in case
sleep(3)

language = driver.find_element(By.ID, value="langSelect-EN")
print(language.text)
language.click()

# Wait for everything to settle
sleep(2)

# Set timers
seconds = 5
timeout = time() + seconds
end_time = time() + 60 * seconds

# Find the big cookie to click
cookie_button = driver.find_element(By.ID, value="bigCookie")

while True:
    cookie_button.click()

    if time() > timeout:
        cookie_elements = driver.find_element(By.ID, value="cookies")
        cookie_text = cookie_elements.text
        cookie_counts = int(cookie_text.split()[0].replace(",", ""))
        print(cookie_counts)

        # Find all available products in the store
        products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

        best_item = None

        for product in reversed(products):
            if "enabled" in product.get_attribute("class"):
                best_item = product
                break

        if best_item:
            best_item.click()
            print(f"Bought item: {best_item.get_attribute('id')}")

        timeout = time() + seconds

        if time() > end_time:
            try:
                cps = driver.find_element(By.XPATH, '//*[@id="cookiesPerSecond"]').text
                print(f"Final result: {cps}")
            except NoSuchElementException:
                print("Couldn't get final cookie count")
            break


driver.quit()