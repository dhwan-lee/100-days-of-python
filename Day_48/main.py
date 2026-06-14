from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
# driver.get("https://www.amazon.ca/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=pd_ci_mcx_mh_mcx_views_0_title?pd_rd_w=MN7OO&content-id=amzn1.sym.a6222432-b80a-416c-8131-3f90f9db32fd%3Aamzn1.symc.c3d5766d-b606-46b8-ab07-1d9d1da0638a&pf_rd_p=a6222432-b80a-416c-8131-3f90f9db32fd&pf_rd_r=PTGGFTCZAP2RM52HAT71&pd_rd_wg=Lehxy&pd_rd_r=3f9286ff-7145-4efd-8d31-91bacea348e9&pd_rd_i=B06Y1YD5W7&th=1")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# close just one particular tab
# driver.close()

# Challenge
every_elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li")
event_dict = {}

for i in range(len(every_elements)):
    event_time = every_elements[i].find_element(By.TAG_NAME, value="time").text
    event_name = every_elements[i].find_element(By.TAG_NAME, value="a").text

    event_dict[i] = {
        i: {
            "time": event_time,
            "name": event_name,
        }
    }

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(event_dict)

driver.quit()