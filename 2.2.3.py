from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("popov")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("igoresha")

    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    email.send_keys("dfdfdf")


    file_path = os.path.join('/home/yura/PycharmProjects/SeleniumPodpis/', 'test.txt')  # добавляем к этому пути имя файла
    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()