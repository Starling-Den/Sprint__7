import pytest
import requests
import allure

from data.curl import *
from data.data import *

class TestOrderCreate:
    @allure.title('Тест создания заказов с разными цветами самоката. Ручка: /api/v1/orders')
    @pytest.mark.parametrize('scooter_color', DataCreateOrder.scooter_color)
    def test_create_order_with_different_colors(self, scooter_color):
        order_data = DataCreateOrder.order_data
        order_data['color'] = scooter_color
        new_order = requests.post(f'{main_url}{create_order}', json=order_data)
        assert new_order.status_code == 201 and create_order_true in new_order.json()
        requests.put(f'{main_url}{order_cancel}{new_order.json()['track']}')
