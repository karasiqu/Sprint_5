from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    PLACE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_NAME = (By.XPATH, "//*[contains(text(), 'User.')]")
    USER_AVATAR = (By.XPATH, "(//button[contains(@class,'circleSmall')])[2]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(), 'Выйти')]")


class AuthFormLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Войти')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Создать аккаунт')]")
    ERROR_TEXT = (By.XPATH, "//span[contains(@class,'input_span') and text()='Ошибка']")


class AdFormLocators:
    AUTH_REQUIRED_TITLE = (By.XPATH, "//*[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.NAME, "category")
    CITY_DROPDOWN = (By.NAME, "city")
    CONDITION_RADIO_NEW = (By.XPATH, "//label[contains(text(), 'Новый')]")
    CONDITION_RADIO_USED = (By.XPATH, "//label[contains(text(), 'Б/У')]")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    DROPDOWN_OPTION = (By.XPATH, "//button[contains(@class,'dropDownMenu_btn')]//span[text()='{value}']")


class ProfileLocators:
    MY_ADS_BLOCK_TITLE = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
    AD_CARD_BY_TITLE = (By.XPATH, "//div[contains(@class,'card')]//h2[contains(text(), '{title}')]")