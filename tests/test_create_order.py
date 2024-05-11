import allure
import pytest
import requests
import scooter_api
import urls


class TestCreateOrder:                                # Тесты на endpoint «Создание заказа»
    @allure.title("Успешное создание заказа с разными самокатами")
    @allure.description("Проверка успешного создания заказа с разными самокатам: BLACK, GREY, BLACK и GREY, 'цвет не указан'. Проверка кода ответа и наличия в ответе номера заказа")
    @pytest.mark.parametrize("color", [
        pytest.param(["BLACK"]),
        pytest.param(["GREY"]),
        pytest.param(["BLACK","GREY"]),
        pytest.param([]),
    ])
    def test_choice_color_in_success_order(self, color):
        color_body = {"color": color}
        create_color_order = scooter_api.create_order(color_body)
        assert create_color_order.status_code == 201 and create_color_order.json()["track"] != None


class TestOrderList:                                # Тесты на endpoint «Получение списка заказа»
    @allure.title("Проверка получения списка заказов в тело ответа")
    @allure.description("Проверка получения списка заказов в тело ответа. Проверка кода ответа и наличия непустого массива с заказами")
    def test_return_list_order(self):
        order_list = requests.get(urls.BASE_URL + urls.ORDER_LIST_ENDPOINT)
        assert order_list.status_code == 200 and order_list.json()["orders"] != []
