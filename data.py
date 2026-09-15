import random
import string

BASE_URL = "https://qa-desk.education-services.ru/"

EXISTING_USER_EMAIL = "testqp@gmail.ru"
EXISTING_USER_PASSWORD = "qwerty"


def random_email():
    local = "".join(random.choices(string.ascii_lowercase, k=8))
    return f"{local}@gmail.ru"


def random_password():
    return "Pass" + "".join(random.choices(string.digits, k=5))


def random_ad_title():
    suffix = "".join(random.choices(string.ascii_lowercase, k=5))
    return f"Тестовое объявление {suffix}"