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
    element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'h1')))
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
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div/h2')
    pk_head = pytest.driver.find_element(By.TAG_NAME, 'h2')

    assert pk_head.text == "Бочкова\nОльга"



