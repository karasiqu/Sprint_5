import pytest
from selenium import webdriver

from data import BASE_URL, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from locators import MainPageLocators, AuthFormLocators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser
    browser.quit()


import time

import pytest
from selenium import webdriver

from data import BASE_URL, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from locators import MainPageLocators, AuthFormLocators


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

    time.sleep(2)
    return driver