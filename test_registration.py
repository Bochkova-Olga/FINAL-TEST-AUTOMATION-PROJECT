import random
import time
import pytest
from settings import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def test_registration():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')
    wait = WebDriverWait(pytest.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-right"]/div/div/h1')))
    # Нажимаем "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()

    yield

    pytest.driver.quit()


def test_002_registration_valid_user_data():
    # Проверка регистрации на сайте
    global first_name, last_name
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    length_name = random.choice(length_names)

    if length_name == 'Min':
        first_name = generate_alphanum_crypt_string(2, russian_letters_and_digits).capitalize()
        last_name = generate_alphanum_crypt_string(2, russian_letters_and_digits).capitalize()
    if length_name == 'Max':
        first_name = generate_alphanum_crypt_string(30, russian_letters_and_digits).capitalize()
        last_name = generate_alphanum_crypt_string(30, russian_letters_and_digits).capitalize()

    # Вводим случайные данные в поле "Имя"
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input').send_keys(
        first_name)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    # Вводим случайные данные в поле "Фамилия"
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input').send_keys(
        last_name)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with {first_name} and {last_name} ')

    assert len(class_error) == 0


def test_003_registration_empty_user_data():
    # Проверка регистрации на сайте
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # Поле "Имя" пустое
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input').send_keys('')
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    # Поле "Фамилия" пустое
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input').send_keys('')
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with empty strings ')

    assert len(class_error) == 0


def test_004_registration_valid_user_data_dash():
    # Проверка регистрации на сайте
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # Вводим случайные данные через тире"-" в поле "Имя"
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input').send_keys(
        first_name)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    # Вводим случайные данные через тире"-" в поле "Фамилия"
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input').send_keys(
        last_name)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with {first_name} and {last_name}')

    assert len(class_error) == 0


def test_005_registration_invalid_user_data():
    # Проверка регистрации на сайте
    global first_name, last_name
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    length_name = random.choice(length_names)

    if length_name == 'Min':
        first_name = generate_alphanum_crypt_string(1, latin_letters_and_digits).capitalize()
        last_name = generate_alphanum_crypt_string(1, latin_letters_and_digits).capitalize()
    if length_name == 'Max':
        first_name = generate_alphanum_crypt_string(31, latin_letters_and_digits).capitalize()
        last_name = generate_alphanum_crypt_string(31, latin_letters_and_digits).capitalize()

    # Вводим случайные данные в поле "Имя"
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input').send_keys(
        first_name)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    # Вводим случайные данные в поле "Фамилия"
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input').send_keys(
        last_name)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')
    if len(class_error) == 0:
        print('\ncount error: {len(class_error)}, with {first_name} and {last_name}')

    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert len(class_error) > 0


def test_006_registration_user_region():
    # Проверка выбора региона
    pytest.driver.implicitly_wait(10)

    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]').click()
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div').click()

    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.CLASS_NAME, 'rt-select__list-desc')

    list_regions = pytest.driver.find_elements(By.CLASS_NAME, 'rt-select__list-item')
    random_element = int(random.uniform(0, len(list_regions)))

    string_element = '//*[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/' \
                     'div[' + random_element.__str__() + '] '
    selected_item = pytest.driver.find_element(By.XPATH, string_element).text
    pytest.driver.find_element(By.XPATH, string_element).click()

    assert selected_item != ""


def test_007_registration_user_valid_email():
    # Проверка валидных данных для входа поля "E-mail или мобильный телефон"
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    random_email = random.choice(valid_email)

    # Вводим в поле valid email
    pytest.driver.find_element(By.XPATH, '//*[@id="address"]').send_keys(random_email)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with {random_email}')

    assert len(class_error) == 0


def test_008_registration_user_valid_phone():
    # Проверка валидных данных для входа поля "E-mail или мобильный телефон"
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    random_phone = random.choice(valid_phone)

    # Вводим в поле valid phone
    pytest.driver.find_element(By.XPATH, '//*[@id="address"]').send_keys(random_phone)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with {random_phone}')

    assert len(class_error) == 0


def test_009_registration_user_invalid_email():
    # Проверка валидных данных для входа поля "E-mail или мобильный телефон"
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    random_invalid_email = random.choice(invalid_email)

    # Вводим в поле valid invalid_email
    pytest.driver.find_element(By.XPATH, '//*[@id="address"]').send_keys(random_invalid_email)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with {random_invalid_email}')

    assert len(class_error) == 0


def test_010_registration_user_invalid_phone():
    # Проверка валидных данных для входа поля "E-mail или мобильный телефон"
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    random_invalid_phone = random.choice(invalid_phone)

    # Вводим в поле invalid_phone
    pytest.driver.find_element(By.XPATH, '//*[@id="address"]').send_keys(random_invalid_phone)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with {random_invalid_phone}')

    assert len(class_error) == 0


def test_011_registration_valid_pass_confirmation_pass_length():
    # Проверка пароля, подтверждение пароля
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    password = generate_alphabet_random_password(8, latin_letters_and_digits)
    confirmation_password = generate_alphabet_random_password(8, latin_letters_and_digits)

    # Вводим случайные данные в поле "Пароль"
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    # Вводим случайные данные в поле "Подтверждение пароля"
    pytest.driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys(confirmation_password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with {password} and {confirmation_password}')

    assert len(class_error) == 0


def test_012_registration_valid_pass_confirmation_pass_length():
    # Проверка пароля, подтверждение пароля
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    password = generate_alphabet_random_password(20, latin_letters_and_digits)
    confirmation_password = generate_alphabet_random_password(20, latin_letters_and_digits)

    # Вводим случайные данные в поле "Пароль"
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    # Вводим случайные данные в поле "Подтверждение пароля"
    pytest.driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys(confirmation_password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error')
    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with {password} and {confirmation_password}')

    assert len(class_error) == 0


def test_013_registration_valid_pass_confirmation_pass_length():
    # Проверка пароля, подтверждение пароля
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    password = generate_alphabet_random_password(21, latin_letters_and_digits)
    confirmation_password = generate_alphabet_random_password(21, latin_letters_and_digits)

    # Вводим случайные данные в поле "Пароль"
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    # Вводим случайные данные в поле "Подтверждение пароля"
    pytest.driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys(confirmation_password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')
    if len(class_error) == 0:
        print('\ncount error: {len(class_error)}, with {password} and {confirmation_password}')

    assert len(class_error) > 0

    if len(password) > 20 and len(confirmation_password) > 20:
        print("Длина пароля должна быть не более 20 символов")


def test_014_registration_invalid_pass_confirmation_pass():
    # Проверка пароля, подтверждение пароля
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    length_password = random.choice(length_passwords)
    length_confirmation_password = random.choice(length_confirmation_passwords)

    password = generate_alphanum_crypt_string(7, russian_letters_and_digits)
    confirmation_password = generate_alphanum_crypt_string(7, russian_letters_and_digits)

    # Вводим случайные данные в поле "Пароль"
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

    # Вводим случайные данные в поле "Подтверждение пароля"
    pytest.driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys(confirmation_password)

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')
    if len(class_error) == 0:
        print('\ncount error: {len(class_error)}, with {password} and {confirmation_password}')

    assert len(class_error) > 0

    if len(password) < 8 and len(confirmation_password) < 8:
        print("Длина пароля должна быть не менее 8 символов")


def test_015_registration_empty_pass_confirmation_pass():
    # Проверка пароля, подтверждение пароля на пустые значения
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # Поле "Пароль" пустое
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('')

    # поле "Подтверждение пароля" пустое
    pytest.driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('')

    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/button').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')
    if len(class_error) == 0:
        print('\ncount error: {len(class_error)}, with empty strings')

    assert len(class_error) > 0


def test_016_registration_different_pass_confirmation_pass():
    # Проверка пароля, подтверждение пароля
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    password = generate_alphabet_random_password(8, latin_letters_and_digits)
    confirmation_password = generate_alphabet_random_password(10, latin_letters_and_digits)

    # Вводим случайные данные в поле "Пароль"
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    # Вводим случайные данные в поле "Подтверждение пароля"
    pytest.driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys(confirmation_password)
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').click()

    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/button').click()

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')

    assert len(class_error) > 0

    if len(password) == 8 and len(confirmation_password) == 10:
        print('\ncount error: {len(class_error)}, with password: {len(password)} '
              'and confirm {len(confirmation_password)}')
        print("Пароли не совпадают")


def test_017_registration_agreement():
    # Проверка ссылки "Пользовательское соглашение"
    pytest.driver.implicitly_wait(10)
    myDynamicElement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    pytest.driver.find_element(By.CSS_SELECTOR, '#page-right > div > div > div > form > div.auth-policy > a').click()

    pytest.driver.get('https://b2c.passport.rt.ru/sso-static/agreement/agreement.html')

    class_error = pytest.driver.find_elements(By.CLASS_NAME, 'h1')

    if len(class_error) > 0:
        print('\ncount error: {len(class_error)}, with empty strings')

    assert len(class_error) == 0
    print('Публичная оферта о заключении Пользовательского соглашения /'
          'на использование Сервиса «Ростелеком ID')
