

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = " https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    x_elem = str(math.log(abs(12*math.sin(int(x)))))

    field = browser.find_element(By.ID, "answer")
    field.send_keys(x_elem)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()