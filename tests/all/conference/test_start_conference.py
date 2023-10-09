from allure import feature, story, suite, title, description, tag, step
from description_conftest import DF
from api import *


@suite('Конференции')
@description(DF.description + DF.created_conferences)
@tag('autotest', 'api', 'super-admin')
@title('Включить конференцию с валидным номером response = 201')
def test_start_conference_201(created_conferences, api):
    api.stop_conference(created_conferences)
    response = BaseApi().api_test('POST', 'api/v1/start_conference', conference=created_conferences)
    assert response.status_code == 201, f"{response.json()}"


