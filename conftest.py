import pytest
import requests

from data.generators import *
from data.curl import *


@pytest.fixture
def courier_data_body():
    login = login_generator()
    password = password_generator()
    name = name_generator()
    courier_body_register = {
        'login': login,
        'password': password,
        'firstName': name,
    }
    courier_body_login = {
        'login': login,
        'password': password,
    }
    yield [courier_body_register, courier_body_login]
    login_courier = requests.post(f'{main_url}{courier_login}', json=courier_body_login)
    requests.delete(f'{main_url}{courier_delete}{login_courier.json()["id"]}')

@pytest.fixture
def courier_register_and_login():
    login = login_generator()
    password = password_generator()
    name = name_generator()
    courier_body_register = {
        'login': login,
        'password': password,
        'firstName': name,
    }
    courier_body_login = {
        'login': login,
        'password': password,
    }
    requests.post(f'{main_url}{courier_registration}', json=courier_body_register)
    login_courier = requests.post(f'{main_url}{courier_login}', json=courier_body_login)
    yield [courier_body_register, courier_body_login, login, password]
    requests.delete(f'{main_url}{courier_delete}{login_courier.json()["id"]}')
