import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import random_ad_title
from locators import MainPageLocators, AdFormLocators, ProfileLocators


def test_create_ad_unauthorized(driver):
    driver.find_element(*MainPageLocators.PLACE_AD_BUTTON).click()

    assert driver.find_element(*AdFormLocators.AUTH_REQUIRED_TITLE).is_displayed()


def test_create_ad_authorized(authorized_driver):
    driver = authorized_driver
    wait = WebDriverWait(driver, 10)

    ad_title = random_ad_title()

    wait.until(
        EC.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)
    ).click()

    wait.until(
        EC.visibility_of_element_located(AdFormLocators.TITLE_INPUT)
    ).send_keys(ad_title)

    driver.find_element(*AdFormLocators.DESCRIPTION_INPUT).send_keys("Описание для автотеста")
    driver.find_element(*AdFormLocators.PRICE_INPUT).send_keys("1500")

    driver.find_element(*AdFormLocators.CONDITION_RADIO_NEW).click()

    wait.until(
        EC.element_to_be_clickable(AdFormLocators.PUBLISH_BUTTON)
    ).click()

    time.sleep(3)
    driver.get("https://qa-desk.education-services.ru/profile")

    wait.until(
        EC.presence_of_element_located(
            ProfileLocators.MY_ADS_BLOCK_TITLE
        )
    )

    assert driver.find_element(
        *ProfileLocators.AD_CARD_BY_TITLE[:1],
        ProfileLocators.AD_CARD_BY_TITLE[1].format(title=ad_title),
    ).is_displayed()