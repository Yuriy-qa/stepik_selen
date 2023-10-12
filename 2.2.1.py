from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.ID, "num1").text
    number2 = browser.find_element(By.ID, "num2").text
    sum = int(number1) + int(number2)
    sum1 = str(sum)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum1)
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
