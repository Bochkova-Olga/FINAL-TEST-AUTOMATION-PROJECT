import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')
    # # Вводим email
    # pytest.driver.find_element(By.ID, 'username').send_keys('bochkova69@mail.ru')
    # # Вводим пароль
    # pytest.driver.find_element(By.ID, 'password').send_keys('3NHG!5w@%D')
    # # Нажимаем на кнопку входа в аккаунт
    # pytest.driver.find_element(By.CSS_SELECTOR, 'button[id="kc-login"]').click()

    yield

    pytest.driver.quit()


def test_get_label_rt():
    time.sleep(10)
    pk_head = pytest.driver.find_element(By.TAG_NAME, 'h1')

    assert pk_head.text == "Авторизация"
