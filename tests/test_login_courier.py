import pytest
import requests
import allure

from data.curl import *
from data.data import *


class TestCourierLogin:
    @allure.title('Тест логина курьера. Ручка: /api/v1/courier/login')
    def test_courier_login_true(self, courier_register_and_login):
        response = requests.post(f'{main_url}{courier_login}', json=courier_register_and_login[1])
        courier_id = response.json()
        assert response.status_code == 200 and courier_id !=''

    @allure.title('Тест логина курьера с незарегестированным логином. Ручка: /api/v1/courier/login')
    def test_courier_login_not_reg(self):
        data_login = DataCourierRegLogin.data_login[0]
        response = requests.post(f'{main_url}{courier_login}', json=data_login)
        assert response.status_code == 404 and response.json() == ResponseBodyCourier.courier_login_not_exist

    @allure.title('Тест логина курьера с пустым логином. Ручка: /api/v1/courier/login')
    def test_courier_login_without_login_error(self, courier_register_and_login):
        data_login = {'login':'', 'password':courier_register_and_login[3]}
        response = requests.post(f'{main_url}{courier_login}', json=data_login)
        assert response.status_code == 400 and response.json() == ResponseBodyCourier.courier_login_without_login_or_password

    @allure.title('Тест логина курьера с пустым паролем. Ручка: /api/v1/courier/login')
    def test_courier_login_without_password_error(self, courier_register_and_login):
        data_login = {'login': courier_register_and_login[2], 'password': ''}
        response = requests.post(f'{main_url}{courier_login}', json=data_login)
        assert response.status_code == 400 and response.json() == ResponseBodyCourier.courier_login_without_login_or_password
