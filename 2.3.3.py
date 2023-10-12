from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    click_button = browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    # alert = browser.switch_to.alert
    # alert.accept()
    # browser.switch_to.window("http://suninjuly.github.io/redirect_page.html?")
    # time.sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = browser.find_element(By.ID, "input_value").text
    field = browser.find_element(By.ID, "answer")
    field.send_keys(str(math.log((abs(12*math.sin(int(number)))))))
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()