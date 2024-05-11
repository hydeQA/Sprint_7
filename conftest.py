import allure
import pytest

import helper
import scooter_api
import urls
import requests


@allure.step("Создание шаблонного курьера")
@pytest.fixture(scope='function')
def default_courier():
    body = helper.new_courier_login_password()
    courier_response = scooter_api.create_courier(body)
    login_body = body.copy()
    login_body.pop("firstName", None)
    id_courier = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=login_body).json().get("id")
    yield courier_response
    requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(id_courier))