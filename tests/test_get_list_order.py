import pytest
import requests
import allure

from data.curl import *
from data.data import *


class TestOrderList:
    @allure.title('Тест получения списка заказов. Ручка: /api/v1/orders')
    def test_get_list_order_true(self):
        with allure.step('1. POST /api/v1/orders: Получение списка заказов'):
            response = requests.get(f'{main_url}{order_list}')
        with allure.step('2. Проверка ответа'):
            assert response.status_code == 200 and get_list_order_true in response.json()
