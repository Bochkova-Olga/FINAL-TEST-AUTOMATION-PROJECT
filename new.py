import os
from api import PetFriends
from settings import *


pf = PetFriends()


def test_create_pet_simple(name='Барсик', animal_type='кот', age='15'):
    '''Проверяем добавление питомца с корректными данными'''

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.post_create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_create_pet_simple_empty_field():
    '''Проверяем добавление питомца с пустыми полями'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_create_pet_simple(auth_key, name='', animal_type='', age='')
    assert status == 200

# Это баг, по документации эти поля обязательные к заполнению, тест должен выдать  код 400



def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    '''Проверяем, что запрос api-key возвращает статус 200 и в результате содержит слово key'''

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашим ожиданием
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_not_valid_user(email=not_valid_email, password=not_valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_pets_with_valid_key(filter=''):
    """Проверяем, что запрос всех питомцев возвращает не пустой список.
    Мы сначала получаеи api-key и сохраняем переменную в auth_key.
    Используя этот ключ, запрвшиваем список всех питомцев.
    Проверяем, что список не пустой"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_get_api_pets_with_not_valid_key(filter=''):
    status, result = pf.get_list_of_pets(not_valid_key, filter)
    assert status == 403


def test_add_new_pet_with_negative_age(name='Silver', animal_type='main_kun', age='-1', pet_photo='images/cat1.jpg'):
    '''Проверяем добавление питомца с отрицательным возрастом'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
# Это баг,возраст не должен принимать отрицательные значения, тест должен быть провален,
# код 400 с описанием ошибки


def test_add_new_pet_with_float_age(name='Silver', animal_type='main_kun', age='192.168.1.1', pet_photo='images/cat1.jpg'):
    '''Проверяем добавление питомца с неправильным форматом возрастом'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
# Это баг,возраст должен принимать целые числа, тест должен быть провален,
# код 400 с описанием ошибки


def test_add_new_pet_photo_text(name='Silver', animal_type='main_kun', age='1', pet_photo='images/cat1.txt'):
    '''Проверяем добавление фото питомца с неправильным форматом файла'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
# Это баг, этот формат не должен поддерживаться, тест должен быть провален,
# код 400 с описанием ошибки


def test_add_new_pet_with_data(name='Silver', animal_type='main_kun', age='1', pet_photo='images/cat1.jpg'):
    '''Проверяем добавление питомца с корректными данными'''

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo

    # pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_pets_set_photo(pet_photo='images/cat3.jpg'):
        '''Проверяем добавление питомца с корректными данными'''

        # Запрашиваем ключ api и сохраняем в переменную auth_key
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Добавляем питомца
        pet_id = my_pets['pets'][1]['id']
        status, result = pf.post_pets_set_photo(auth_key, pet_id, pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        # assert result['name'] == name


def test_pets_set_photo_with_invalid_id(pet_id=not_valid_id, pet_photo='images/cat3.jpg'):
    '''Проверяем добавление фото к питомцу с not_valid_id'''

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.post_pets_set_photo(auth_key, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 500


def test_successful_delete_self_pet():
    '''Проверяем возможность удаления питомца '''

    # Получаем ключ auth_key и запрвшиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем список своих питомцев, если он пустой, то добавляем нового питомца
    # и запрашиваем список своих питомцев снова
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Silver", "main_kun", "1", "images/cat2.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берем id первого питомца и списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Запрашиваем своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем список своих питомцев, если он пустой, то добавляем нового питомца
    # и запрашиваем список своих питомцев снова
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Nyusha", "cat", "7", "images/cat2.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем статус ответа на 200 и id удаленного питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Рыжуля', animal_type='Кот', age=5):
    '''Проверяем возможность обновления информации о питомце '''

    # Получаем ключ auth_key  и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Список не пустой - обновляем имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем статус ответа 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_successful_delete_other_pet(pet_id=not_valid_id):
    '''Проверяем возможность удаления питомца по id '''

    # valid id
    # a13a7a4f-25d9-4761-bc13-166a02f3112c
    # ff1247b9-5349-4ca7-8158-554aad8de44d

    # not valid id
    # a13a7a4f-25d9-4761-bc13-166a02f3100c

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Проверяем статус ответа на 200 и id удаленного питомца
    assert status == 200
    assert pet_id not in my_pets.values()

# Баг, удаляется не существующий ID питомца

def test_create_simple_lines_too_long():
    """Ввод не ограниченное количество символов в полях инициализации карточки питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, _ = pf.post_create_pet_simple(auth_key,
                                               name=generate_alphanum_crypt_string(100500),
                                               animal_type=generate_alphanum_crypt_string(100500),
                                               age=generate_alphanum_crypt_string(100500))
    assert status == 200

# Баг, не ограничено число символов в полях инициализации, должен быть код ошибки  400


def test_successful_delete_pet_not_valid_key():
    '''Проверяем возможность удаления питомца c not_valid_key '''

    _, my_pets = pf.get_list_of_pets(not_valid_key, "my_pets")
    pet_id = not_valid_id
    status, _ = pf.delete_pet(not_valid_key, pet_id)

    assert status == 403
    # assert pet_id not in my_pets.values()


# def test_delete_all_my_pets():
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     status, result = pf.delete_all_my_pets(auth_key)
#     assert status == 200
#     assert result['pets'] == []
#