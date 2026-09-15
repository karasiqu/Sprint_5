from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from locators import MainPageLocators, AuthFormLocators


class TestLoginLogout:

    def test_login_user(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*AuthFormLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*AuthFormLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthFormLocators.LOGIN_BUTTON).click()

        assert driver.find_element(*MainPageLocators.USER_NAME).is_displayed()


    def test_logout_user(self, authorized_driver):
        authorized_driver.find_element(*MainPageLocators.LOGOUT_BUTTON).click()

        assert authorized_driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).is_displayed()
        assert len(authorized_driver.find_elements(*MainPageLocators.USER_NAME)) == 0