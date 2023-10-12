import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100"))
print(price)

button_book = browser.find_element(By.ID, "book")
button_book.click()

# number = browser.find_element(By.ID, "input_value").text
#
# answer = browser.find_element(By.ID, "answer")
# answer.send_keys(str(math.log((abs(12*math.sin(int(number)))))))
#
# submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
#
# alert = browser.switch_to.alert


number = browser.find_element(By.ID, "input_value").text
print(number)
field = browser.find_element(By.ID, "answer")
field.send_keys(str(math.log((abs(12 * math.sin(float(number)))))))
submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(555)
