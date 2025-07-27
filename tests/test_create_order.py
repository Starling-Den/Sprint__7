import pytest
import requests
import allure

from conftest import create_order_and_delete
from data.curl import *
from data.data import *

class TestOrderCreate:
    @allure.title('Тест создания заказов с разными цветами самоката. Ручка: /api/v1/orders')
    @pytest.mark.parametrize('scooter_color', DataCreateOrder.scooter_color)
    def test_create_order_with_different_colors(self, scooter_color, create_order_and_delete):
        with allure.step('1. Подготовка тестовых данных'):
            order_data = DataCreateOrder.order_data
            order_data['color'] = scooter_color
        with allure.step('2. POST /api/v1/order: Создание заказа'):
            new_order = requests.post(f'{main_url}{create_order}', json=order_data)
        with allure.step('3. Проверка ответа'):
            assert new_order.status_code == 201 and create_order_true in new_order.json()
