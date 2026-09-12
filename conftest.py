import random
import string

import pytest
from selenium import webdriver

from locators import MainPageLocators, AuthFormLocators


BASE_URL = "https://qa-desk.education-services.ru/"

EXISTING_USER_EMAIL = "testqp@gmail.ru"
EXISTING_USER_PASSWORD = "qwerty"


def random_email():
    local = "".join(random.choices(string.ascii_lowercase, k=8))
    return f"{local}@mail.ru"


def random_password():
    return "Pass" + "".join(random.choices(string.digits, k=5))


def random_ad_title():
    return "Тестовое объявление"


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser
    browser.quit()


@pytest.fixture
def authorized_driver(driver):
    driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).click()
    driver.find_element(*AuthFormLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*AuthFormLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*AuthFormLocators.LOGIN_BUTTON).click()

    assert driver.find_element(*MainPageLocators.USER_NAME).is_displayed()
    return driver