from allure import feature, story, suite, title, description, tag, step
from description_conftest import DF
from api import *


@suite('Конференции')
@description(DF.description + DF.created_conferences)
@tag('autotest', 'api', 'super-admin')
@title('Отключить конференцию response = 201')
def test_stop_conf_201(created_conferences):
    response = BaseApi().api_test('POST', 'api/v1/stop_conference', conference=created_conferences)
    assert response.status_code == 201, "Не удалось остановить конференцию на сервере"

