from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number = int(browser.find_element(By.ID, "input_value").text)

    respons = str(math.log((abs(12*math.sin(number)))))


    field_input = browser.find_element(By.ID, "answer")
    field_input.send_keys(respons)

    Check_box = browser.find_element(By.ID, "robotCheckbox").click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()