from allure import suite, title, description, tag
from description_conftest import DF
from api import *

@suite('Конференции')
@description(DF.description + DF.created_conferences)
@tag('autotest', 'api', 'super-admin')
@title('Удалить существующую конференции response = 200')
def test_delete_conference_200(created_conferences):
    response = BaseApi().api_test('DELETE', f'api/v1/conference/{created_conferences}')
    assert response.status_code == 200, f"{response.json()}"
