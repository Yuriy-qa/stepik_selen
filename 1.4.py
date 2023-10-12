from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = " https://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    First_name = browser.find_element(By.CLASS_NAME, "form-control first")

    First_name.send_keys("Ivan")
    Last_name = browser.find_element(By.CLASS_NAME, "form-control second")
    Last_name.send_keys("Petrov")
    Email = browser.find_element(By.CLASS_NAME, "form-control third")
    Email.send_keys("Smolensk")
    # Phone = browser.find_element(By.CLASS_NAME, "form-group first_class")
    # Phone.send_keys("+375285555555")
    # Address= browser.find_element(By.CLASS_NAME, "form-group second_class")
    # Address.send_keys("pupkino")



    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3][text()='Submit']")
    print(button.text)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
