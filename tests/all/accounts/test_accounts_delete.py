from allure import suite, title, description, tag
from description_conftest import DF
from api import *


@suite('Абоненты')
@description(DF.description + DF.created_accounts)
@tag('autotest', 'api', 'super-admin')
@title('Удалить абонента response = 200')
def test_delete_account_200(created_accounts):
    response = BaseApi().api_test('DELETE', f'api/v1/account/{created_accounts}')
    assert response.status_code == 200, f"{response.json()}"


@suite('Абоненты')
@tag('autotest', 'api', 'super-admin')
@title('Удалить несуществующего абонента response = 404')
def test_delete_account_404():
    response = BaseApi().api_test('DELETE', f'api/v1/account/{__name__}')
    assert response.status_code == 404, f"{response.json()}"


@suite('Абоненты')
@description(DF.description + DF.created_accounts)
@tag('autotest', 'api', 'super-admin')
@title('Удалить абонента без авторизации response = 401')
def test_delete_account_401(created_accounts):
    response = BaseApi(fake_token=True).api_test('DELETE', f'api/v1/account/{created_accounts}')
    assert response.status_code == 401, f"{response.json()}"

