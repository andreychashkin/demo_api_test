import PIL
import pytest

import requests
import time
import os

from api.libs.BaseApi import BaseApi
from . import TestData
from PIL import Image


class ConferencesApi(BaseApi):

    def create_conference(self, delay=0, **data):
        """Метод создает конференцию, на вход принимаются настройки конференции"""
        response = self.call_method('POST', 'api/v1/conferences', data)
        time.sleep(delay)
        return response

    def delete_conference(self, number):
        """Метод удаляет конференцию с сервера по ее номеру"""
        return self.call_method('DELETE', f'api/v1/conference/{number}', data=None)

    def delete_conferences(self, **numbers):
        """"Метод удаляет список конференций с сервера по номерам"""
        return self.call_method('POST', 'api/v1/delete_conferences', numbers)

    def get_conferences_list(self, **params):
        """Метод возвращается все конференции с параметрами предусмотренными api сервера"""
        return self.call_method('GET', 'api/v1/conferences', params)

    def start_conference(self, conference):
        """Метод включает конференцию"""
        return self.call_method('POST', 'api/v1/start_conference', data={'conference': conference})

    def stop_conference(self, conference):
        """Останавливаем конференцию"""
        return self.call_method('POST', 'api/v1/stop_conference', data={'conference': conference})

    def get_screen(self, conference, test_name, test_number='', delay=0):
        """Получение скриншота конференции через превью трансляции"""
        time.sleep(2)
        for i in range(2):
            url = f'https://{self.server_ip}/api/v1/stream/preview/{conference}'
            response = requests.get(
                url,
                headers=self.headers,
                verify=False
            )
            # записываем полученный скриншот в файл по указанному пути
            current_way = os.path.join(os.getcwd())
            current_way = os.path.join(f"{current_way}/screenshots_{TestData.screenshots}/{test_name}/current/")
            try:
                os.makedirs(current_way)
            except FileExistsError:
                print("Папка уже создана")
            finally:
                way = os.path.abspath(os.path.join(current_way, f'{test_name}{test_number}.png'))
                out = open(way, "wb")
                out.write(response.content)
                out.close()
                try:
                    Image.open(os.path.join(
                        current_way, f'{test_name}{test_number}.png'))
                    time.sleep(delay)
                    return response.status_code
                except PIL.UnidentifiedImageError:
                    print('Ошибка открытия скриншота')
                    continue
        return pytest.skip('Тест пропущен в связи с невозможностью считать полученный скрин')

