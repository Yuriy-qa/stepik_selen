from cmath import sin

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    image_box = browser.find_element(By.ID, "treasure")
    image_attribute = image_box.get_attribute("valuex")
    number_elem = str(math.log(abs(12 * math.sin(int(image_attribute)))))

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(number_elem)
    check_box = browser.find_element(By.ID, "robotCheckbox").click()
    radio = browser.find_element(By.ID, "robotsRule").click()
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()



    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    #
    # assert robots_checked is None
    # print("nety")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()