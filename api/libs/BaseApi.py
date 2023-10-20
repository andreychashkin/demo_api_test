from allure import  step
import requests
import json
import time
from . import TestData


class BaseApi:
    token = refresher_token = ''
    current_connections = 0
    headers:dict = {}
    second_ip_server = ''
    server_ip = ''
    fake_token = fake_refresher_token = ''

    def __init__(self, server_ip=TestData.ip_server, logins=TestData.login, passwords=TestData.password,
                 fake_token=False):
        self.server_ip = server_ip
        self.second_ip_server = TestData.second_ip
        self.sleep = TestData.sleep
        self.auth_jwt(server_ip, logins, passwords, fake_token)

    @step('Выполнить {method} запрос: {url}')
    def api_test(self, method: str, url: str, **data) -> requests.Response:
        if 'GET' in method:
            return requests.get(url=f'https://{self.server_ip}/{url}', params=data, verify=False,
                                    headers=self.headers)
        if 'POST' in method:
            return requests.post(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                     headers=self.headers)
        if 'PATCH' in method:
            return requests.patch(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                      headers=self.headers)
        if 'DELETE' in method:
            return requests.delete(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                       headers=self.headers)
        if 'PUT' in method:
            return requests.put(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                    headers=self.headers)
        time.sleep(self.sleep)
        return exit(1)

    @step('Выполнить {method} запрос: {url}')
    def call_method(self, method: str, url: str, data) -> requests.Response:
        if 'GET' in method:
            return  requests.get(url=f'https://{self.server_ip}/{url}', params=data, verify=False,
                                    headers=self.headers)
        if 'POST' in method:
            return requests.post(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                     headers=self.headers)
        if 'PATCH' in method:
            return requests.patch(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                      headers=self.headers)
        if 'DELETE' in method:
            return requests.delete(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                       headers=self.headers)
        if 'PUT' in method:
            return requests.put(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                    headers=self.headers)
        time.sleep(self.sleep)
        return exit(1)

    def auth_jwt(self, server_ip, logins='', passwords='', fake_token=False):
        url = f'https://{server_ip}/api/v1/auth/jwt'
        response = requests.post(
            url,
            data=json.dumps({"username": logins,
                             "password": passwords}),
            verify=False,
            headers = {'Content-Type': 'application/json'} 
        )
        # print(response.cookies.values()[0])
        if fake_token:
            self.token = response.json()
            self.refresher_token = response.json()
            self.server_ip = server_ip
            self.headers = {"Authorization": f"Bearer "}
        else:
            try:
                self.token = response.json()["data"]["token"]
                self.refresher_token = response.json()["data"]["refreshToken"]
                self.server_ip = server_ip
                self.headers = {"Authorization": "Bearer " + self.token,
                                'Content-Type': 'application/json'}
                return response
            except KeyError:
                return response

    @staticmethod
    def create_data(dict_2, dict_1=None):
        """Метод принимает на вход два словаря с параметрами запросов и формирует из двух словарей один
         Метод работает как склейка в случае если нужно к уже полученным настройкам или данным добавить недостающие"""
        if dict_1 is None:
            dict_1 = {}
        data = dict_1
        for setting, value in dict_2.items():
            data = {**data, **{setting: value}}
        return data
