from data import (
    random_email,
    random_password,
    EXISTING_USER_EMAIL,
    EXISTING_USER_PASSWORD,
)
from locators import MainPageLocators, AuthFormLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*AuthFormLocators.NO_ACCOUNT_BUTTON).click()

        email = random_email()
        password = random_password()

        driver.find_element(*AuthFormLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthFormLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthFormLocators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthFormLocators.CREATE_ACCOUNT_BUTTON).click()

        assert driver.find_element(*MainPageLocators.USER_NAME).is_displayed()


    def test_registration_invalid_email(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*AuthFormLocators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*AuthFormLocators.EMAIL_INPUT).send_keys("invalid_email")
        driver.find_element(*AuthFormLocators.CREATE_ACCOUNT_BUTTON).click()

        assert driver.find_element(*AuthFormLocators.ERROR_TEXT).is_displayed()


    def test_registration_existing_user(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*AuthFormLocators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*AuthFormLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*AuthFormLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthFormLocators.SUBMIT_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthFormLocators.CREATE_ACCOUNT_BUTTON).click()

        assert driver.find_element(*AuthFormLocators.ERROR_TEXT).is_displayed()