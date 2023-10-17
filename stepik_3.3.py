import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbc(unittest.TestCase):

    def test_1(self):
        link = "https://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        First_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        First_name.send_keys("Ivan")
        Last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        Last_name.send_keys("Petrov")
        Email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        Email.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals("Congratulations! You have successfully registered!" == welcome_text)
