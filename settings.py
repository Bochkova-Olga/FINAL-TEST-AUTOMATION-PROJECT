import secrets
import string

valid_email = "nufnuf@mail.ru"
valid_password = "12345"

not_valid_email = '223564nbnbn@1212.ru'
not_valid_password = 'sobaka'

not_valid_key = {
  "key": "111111111111111$%$&9gldkjglsdgjns24tuy6tgy##^^"
}

not_valid_id = "a13a7a4f-25d9-4761-bc13-166a02f3100c"


def generate_alphanum_crypt_string(length) -> str:
    """Функция генерирует строку из цифр и букв length=длина текста"""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(secrets.choice(letters_and_digits) for i in range(length))
