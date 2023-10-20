import requests
from .BaseApi import BaseApi


class AccountsApi(BaseApi):

    def create_account(self, **data) -> requests.Response:
        """Создание абонента на сервере"""
        return self.call_method('POST', 'api/v1/accounts', data)

    def delete_account(self, number) -> requests.Response:
        """Метод удаляет абонента на сервере (абонента) по его номеру"""
        return self.call_method('DELETE', f'api/v1/account/{number}', data=None)

