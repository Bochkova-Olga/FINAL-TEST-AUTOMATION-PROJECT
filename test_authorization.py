import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def test_authorization():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')
    wait = WebDriverWait(pytest.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-right"]/div/div/h1')))
    # Вводим email
    pytest.driver.find_element(By.ID, 'username').send_keys('bochkova69@mail.ru')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('3NHG!5w@%D')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

    yield

    pytest.driver.quit()


def test_001_authorization():
    # Проверка авторизации на сайте

    pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]')

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'h3')

    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with empty strings')

    assert len(class_error) == 0
    print('Учетные данные')

