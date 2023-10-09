from api import *
import random
import pytest


@pytest.fixture(scope='module')
def api():
    return Api()


@pytest.fixture()
def created_accounts(api):
    """Фикстура создает абонента с паролем прописанным в TestData.py и возвращает номер"""
    number = random.randint(10000, 99999)
    api.create_account(description='demo_api_test',
                       password=TestData.password,
                       number=number)
    yield number
    api.delete_account(number)


@pytest.fixture()
def created_conferences(api):
    """Фикстура создает конференцию и возвращает номер конференции"""
    conf = random.randint(10000, 99999)
    api.create_conference(description='demo_test_conference', number=conf, active=True)
    yield conf
    api.delete_conference(conf)
