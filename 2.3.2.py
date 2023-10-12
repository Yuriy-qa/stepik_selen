from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    click_button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    number = browser.find_element(By.ID, "input_value").text
    respons_number = str(math.log(abs(12*math.sin(int(number)))))
    field_input = browser.find_element(By.ID, "answer").send_keys(respons_number)
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    new_window = browser.window_handles[1]
    print(new_window)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()