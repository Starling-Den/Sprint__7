import pytest
import requests
import allure

from data.curl import *
from data.data import *


class TestOrderList:
    @allure.title('Тест получения списка заказов. Ручка: /api/v1/orders')
    def test_get_list_order_true(self):
        response = requests.get(f'{main_url}{order_list}')
        assert response.status_code == 200 and get_list_order_true in response.json()
