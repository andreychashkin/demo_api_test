from allure import feature, story, suite, title, description, tag, step
from description_conftest import DF
import pytest
import random
from api import *


@title('Номер')
@pytest.fixture()
def number(api):
    number = random.randint(10000, 99999)
    yield number
    api.delete_account(number)


@suite('Абоненты')
@tag('autotest', 'api', 'super-admin')
@title('Создать абонента SIP и сравнить настройки с дефолтными response = 201')
def test_created_account_compare_with_default_sip_201(number):
    response = BaseApi().api_test('POST',
                                  'api/v1/accounts',
                                  number=number,
                                  type="SIP",
                                  password='123').json()
    default_acc = {'account': {'addressBookContact': None,
                               'description': str(number),
                               'number': str(number),
                               'type': "SIP",
                               'password': '123',
                               'email': '',
                               'source': 'local',
                               'tenant': None,
                               'group': None,
                               'groups': [],
                               'settings':
                                   {'bandwidth': 1536,
                                    'resolutionP2P': '720p',
                                    'behindNat': 'no',
                                    'ip': 'dynamic',
                                    'port': 5060,
                                    'transport': 'UDP',
                                    'insecure': 'port',
                                    'qualify': True,
                                    'codecs': ['g7221', 'ulaw', 'h265', 'h264'],
                                    'h264HighProfile': False,
                                    'h239sendContentInMainStream': False,
                                    'mediaStreams': False,
                                    'dtmf': 'rfc2833',
                                    'bfcpType': 'UDP',
                                    'mediaEncryption': False,
                                    'skype4b': False,
                                    'h4601': True,
                                    'h239': True,
                                    'h224': False,
                                    'crypto': True,
                                    'defaultResolution': '720p',
                                    'ignore': False,
                                    'allowGroupCall': False,
                                    'interpreter': False,
                                    'privateAudioChannel': 10,
                                    'serveGateway': 'auto',
                                    'protectRTP': True,
                                    'panasonicFEC': False},
                               'avatar': None,
                               'status': {'connected': False,
                                          'address': ''}}}
    assert response['data'] == default_acc,\
        f"Настройки абонента отличаются от эталона {number}"


@suite('Абоненты')
@tag('autotest', 'api', 'super-admin')
@title('Создать абонента H323 и сравнение настройки с дефолтными response = 201')
def test_created_account_compare_with_default_h323_201(number):
    response = BaseApi().api_test('POST',
                                  'api/v1/accounts',
                                  number=number,
                                  type="H323",
                                  password='123').json()
    default_acc = {'account': {'addressBookContact': None,
                               'description': str(number),
                               'number': str(number),
                               'type': "H323",
                               'password': '123',
                               'email': '',
                               'source': 'local',
                               'tenant': None,
                               'group': None,
                               'groups': [],
                               'settings':
                                   {'bandwidth': 1536,
                                    'resolutionP2P': '720p',
                                    'behindNat': 'no',
                                    'ip': 'dynamic',
                                    'port': 1720,
                                    'transport': 'TCP',
                                    'insecure': 'port',
                                    'qualify': True,
                                    'codecs': ['g7221', 'h264', 'h263'],
                                    'h264HighProfile': False,
                                    'h239sendContentInMainStream': False,
                                    'mediaStreams': False,
                                    'dtmf': 'rfc2833',
                                    'bfcpType': 'UDP',
                                    'mediaEncryption': False,
                                    'skype4b': False,
                                    'h4601': True,
                                    'h239': True,
                                    'h224': False,
                                    'crypto': True,
                                    'defaultResolution': '720p',
                                    'ignore': False,
                                    'allowGroupCall': False,
                                    'interpreter': False,
                                    'privateAudioChannel': 10,
                                    'serveGateway': 'auto',
                                    'protectRTP': True,
                                    'panasonicFEC': False},
                               'avatar': None,
                               'status': {'address': '',
                                          'connected': False}}}
    assert response['data'] == default_acc,\
        f"Настройки абонента отличаются от эталона {number}"


@suite('Абоненты')
@tag('autotest', 'api', 'super-admin')
@title('Создать абонента WS и сравнение настройки с дефолтными response = 201')
def test_created_account_compare_with_default_ws_201(number):
    response = BaseApi().api_test('POST', 
                                  'api/v1/accounts',
                                  number=number,
                                  type="WS",
                                  password='123').json()
    default_acc = {'account': {'addressBookContact': None,
                               'description': str(number),
                               'number': str(number),
                               'type': "WS",
                               'password': '123',
                               'email': '',
                               'source': 'local',
                               'tenant': None,
                               'group': None,
                               'groups': [],
                               'settings':
                                   {'bandwidth': 1536,
                                    'resolutionP2P': '720p',
                                    'behindNat': 'no',
                                    'ip': 'dynamic',
                                    'port': 5060,
                                    'transport': 'UDP',
                                    'insecure': 'port',
                                    'qualify': True,
                                    'codecs': ['opus', 'h264', 'vp8'],
                                    'h264HighProfile': False,
                                    'h239sendContentInMainStream': False,
                                    'mediaStreams': False, 'dtmf': 'rfc2833',
                                    'bfcpType': 'UDP',
                                    'mediaEncryption': False,
                                    'skype4b': False,
                                    'h4601': True,
                                    'h239': True,
                                    'h224': False,
                                    'crypto': True,
                                    'defaultResolution': '720p',
                                    'ignore': False,
                                    'allowGroupCall': False,
                                    'interpreter': False,
                                    'privateAudioChannel': 10,
                                    'serveGateway': 'auto',
                                    'protectRTP': True,
                                    'panasonicFEC': False},
                               'avatar': None,
                               'status': {'connected': False,
                                          'address': ''}}}
    assert response['data'] == default_acc,\
        f"Настройки абонента отличаются от эталона {number}"
