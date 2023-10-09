from allure import feature, story, suite, title, description, tag, step
from description_conftest import DF
from api import *
import pytest
import random


@title('Конференции')
@pytest.fixture()
def number(api):
    """Генерируем рандомный номер конференции и удаляем ее после прохождения теста"""
    number = random.randint(10000, 99999)
    yield number
    api.delete_conference(number)


@suite('Конференции')
@tag('autotest', 'api', 'super-admin')
@title('Создать конференцию с изменением настройки {test_data[0]} '
              'на {test_data[1]} response = test_data[2]')
@pytest.mark.parametrize('test_data', [
    ['description', "TestName", 201],
    ['description', "test_", 201],
    ['description', "test_123", 201],
    ['description', "10300", 201],
    ['description', "name.name", 201],
    ['description', "тест.тест", 201],
    ['description', "тест123", 201],
    ['description', "тест тест", 201],
    ['description', "тест_", 201],
    ['description', "Тест", 201],
    ['description', False, 422],

    ['pin', 2, 201],
    ['pin', 1000, 201],
    ['pin', 124567891765422, 201],
    ['pin', "13", 201],
    ['pin', '"0001"', 422],
    ['pin', False, 422],
    ['pin', True, 422],
    ['pin', "01", 422],
    ['pin', "0", 422],
    ['pin', "1245612456124561122", 422],
    ['pin', "3", 201],
    ['pin', "text", 422],
    ['pin', '"-1"', 422],
    ['pin', "'", 422],

])
def test_created_conference_pin_description(number, test_data):
    param, value, rez = test_data
    response = BaseApi().call_method(
        'POST', 'api/v1/conferences',
        data={
            'description': __name__,
            'number': number,
            param: value,
        }
    )
    assert response.status_code == rez, f"{response.json()}"

    
@suite('Конференции')
@tag('autotest', 'api', 'super-admin')
@title('Создать конференции без авторизаци response = 401')
@description(DF.description + DF.created_accounts)
def test_created_conference_401(number, created_accounts):
    response = BaseApi(logins=created_accounts).call_method(
        'POST', 'api/v1/conferences', data={'description': __name__, 'number': number})
    assert response.status_code == 401, f"{response.json()}"
    
