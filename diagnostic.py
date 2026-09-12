import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qa-desk.education-services.ru/")
driver.implicitly_wait(5)

# Логин
driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()
driver.find_element(By.NAME, "email").send_keys("testqp@gmail.ru")
driver.find_element(By.NAME, "password").send_keys("qwerty")
driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Войти')]").click()
time.sleep(3)

# Открываем форму создания
driver.find_element(By.XPATH, "//button[contains(text(), 'Разместить объявление')]").click()
time.sleep(2)

# Заполняем
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Диагностика")
driver.find_element(By.XPATH, "//textarea[@name='description']").send_keys("тест")
driver.find_element(By.NAME, "price").send_keys("1000")
driver.find_element(By.XPATH, "//label[contains(text(), 'Новый')]").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Опубликовать')]").click()
time.sleep(3)

# === ДИАГНОСТИКА ===
print("\n=== ДИАГНОСТИКА ===")
print(f"URL сейчас: {driver.current_url}")

avatars = driver.find_elements(By.XPATH, "//button[contains(@class, 'circleSmall')]")
print(f"Найдено кнопок circleSmall: {len(avatars)}")

for i, av in enumerate(avatars):
    print(f"\n[{i}] видна: {av.is_displayed()}")
    print(f"    включена: {av.is_enabled()}")
    print(f"    позиция: {av.location}")
    print(f"    размер: {av.size}")
    print(f"    класс: {av.get_attribute('class')}")
    print(f"    HTML: {av.get_attribute('outerHTML')[:200]}")

if avatars:
    print("\n=== ПРОБУЕМ КЛИКНУТЬ ===")
    try:
        avatars[0].click()
        time.sleep(3)
        print(f"Клик выполнен. URL после клика: {driver.current_url}")
    except Exception as e:
        print(f"ОШИБКА при клике: {type(e).__name__}: {e}")

input("\nНажми Enter для выхода...")
driver.quit()