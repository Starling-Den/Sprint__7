import pytest
import requests
import allure

from data.curl import *
from data.data import *

class TestCourierRegistration:
    @allure.title('Тест регистрации курьера. Ручка: /api/v1/courier')
    def test_registration_courier_true(self, courier_data_body):
        response = requests.post(f'{main_url}{courier_registration}', json=courier_data_body[0])
        assert response.status_code == 201 and response.json() == ResponseBodyCourier.courier_registration

    @allure.title('Тест регистрации курьера c уже зарегистрированным логином. Ручка: /api/v1/courier')
    def test_registration_courier_same_login_error(self, courier_register_and_login):
        response = requests.post(f'{main_url}{courier_registration}', json=courier_register_and_login[0])
        assert response.status_code == 409 and response.json() == ResponseBodyCourier.courier_registration_with_exist_login

    @allure.title('Тест регистрации курьера без логина или пароля. Ручка: /api/v1/courier')
    @pytest.mark.parametrize('data_reg', DataCourierRegLogin.data_deficit_reg)
    def test_registration_courier_data_deficit_error(self, data_reg):
        response = requests.post(f'{main_url}{courier_registration}', json=data_reg)
        assert response.status_code == 400 and response.json() == ResponseBodyCourier.courier_registration_without_login_or_password
