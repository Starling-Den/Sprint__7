import pytest
import requests

from data.generators import *
from data.curl import *
from data.data import *


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

@pytest.fixture
def create_order_and_delete():
    order_data = DataCreateOrder.order_data
    response = requests.post(f'{main_url}{create_order}', json=order_data)
    yield response
    if response.status_code == 201:
        requests.put(f'{main_url}{order_cancel}{response.json()['track']}')
