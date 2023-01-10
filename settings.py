import secrets
import string


latin_letters_and_digits = string.ascii_letters + string.digits + string.punctuation
russian_letters_and_digits = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

length_names = [
    'Min',
    'Max'
]

length_confirmation_passwords = [
    'Min',
    'Max'
]

length_passwords = [
    'Min',
    'Max'
]

first_name = 'Анна-Мария'
last_name = 'Римский-Корсаков'

valid_email = [
    'o@outlook.com',
    'hr6zdl@yandex.ru',
    'aft93x@outlook.com',
    'dcu@yandex.ru',
    'a5h@mail.ru',
    '281av0@gmail.com',
    '8edmfh@outlook.com',
    'sfn13i@mail.ru',
    'g0orc3x1@outlook.com',
    'rv7bp@gmail.com'
]


valid_phone = [
    '+7(495)714-28-06',
    '+7(903)543-61-15',
    '+7(916)295-34-72',
    '+7(226)117-48-86',
    '+7(991)034-57-93',
    '+7(905)978-72-65',
    '+7(499)694-16-34',
    '+7(985)452-41-18'
]


invalid_email = [
    'o@outlook.com',
    'hr6zdl.yandex.ru',
    'aft93x.outlook.com',
    'dcuyandex.ru',
]


invalid_phone = [
    '495-714-28-06',
    '903-543-61-15',
]


def generate_alphanum_crypt_string(length, in_letters) -> str:
    """Функция генерирует строку из цифр и букв length=длина текста"""
    return ''.join(secrets.choice(in_letters) for i in range(length))


def generate_alphabet_random_password(length, in_letters) -> str:
    while True:
        pwd = ''
        for i in range(length):
            pwd += ''.join(secrets.choice(in_letters))

        if (any(char in string.punctuation for char in pwd) and
                sum(char in string.digits for char in pwd) >= 2):
            break

    return pwd
