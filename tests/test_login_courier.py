import allure
import requests
import data
import helper
import urls
import json


class TestLoginCourier:                                # Тесты на endpoint «Авторизация курьера»
    @allure.title("Проверка успешной авторизации курьера")
    @allure.description("Создание курьера и его авторизация, проверка статуса ответа и наличия id курьера в ответе")
    def test_success_login(self, default_courier):
        courier_body_dict = json.loads(default_courier.request.body.decode('utf-8'))
        courier_login = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=courier_body_dict)
        assert courier_login.status_code == 200 and courier_login.json()["id"] is not None


    @allure.title("Проверка появления ошибки при авторизации курьера с неверным полем login")
    @allure.description("Создание курьера и его авторизация с неверным полем login, проверка статуса ответа с ошибкой и теста ошибки в ответе")
    def test_fail_with_wrong_login(self, default_courier):
        default_courier_body = default_courier.request.body
        default_courier_body_dict = json.loads(default_courier_body)
        requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, default_courier_body)
        body_login = default_courier_body_dict.copy()
        body_login["login"] = "Courier"
        courier_login = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=body_login)
        assert courier_login.status_code == 404 and courier_login.json()["message"] == data.ErrorMessages.ERROR_NOT_FOUND


    @allure.title("Проверка появления ошибки при авторизации курьера с неверным полем password")
    @allure.description("Создание курьера и его авторизация с неверным полем password, проверка статуса ответа с ошибкой и теrста ошибки в ответе")
    def test_fail_with_wrong_password(self, default_courier):
        default_courier_body = default_courier.request.body
        courier_body_dict = json.loads(default_courier_body)
        requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, default_courier_body)
        courier_body_dict["password"] = "54321"
        courier_password = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=courier_body_dict)
        assert courier_password.status_code == 404 and courier_password.json()["message"] == data.ErrorMessages.ERROR_NOT_FOUND


    @allure.title("Проверка появления ошибки при авторизации курьера с пустым полем login")
    @allure.description("Создание курьера и его авторизация с пустым полем login, проверка статуса ответа с ошибкой и теста ошибки в ответе")
    def test_fail_with_empty_login(self, default_courier):
        default_courier_body = default_courier.request.body
        courier_body_dict = json.loads(default_courier_body)
        requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, default_courier_body)
        courier_body_dict["login"] = ""
        courier_login = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=courier_body_dict)
        assert courier_login.status_code == 400 and courier_login.json()["message"] == data.ErrorMessages.ERROR_NOT_ENOUGH_LOGIN_DATA


    @allure.title("Проверка появления ошибки при авторизации курьера с пустым полем password")
    @allure.description("Создание курьера и его авторизация с пустым полем password, проверка статуса ответа с ошибкой и теrста ошибки в ответе")
    def test_fail_with_empty_password(self, default_courier):
        courier_response = default_courier
        courier_body_dict = json.loads(courier_response.request.body)
        courier_body_dict["password"] = ""
        courier_password = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=courier_body_dict)
        assert courier_password.status_code == 400 and courier_password.json()["message"] == data.ErrorMessages.ERROR_NOT_ENOUGH_LOGIN_DATA


    @allure.title("Проверка невозможности авторизации несуществующего курьера")
    @allure.description("Авторизация несуществующего курьера, проверка статуса ответа и текста ошибки")
    def test_fail_nonexistent_courier_login(self):
        body = helper.new_courier_login_password()
        courier_login = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=body)
        assert courier_login.status_code == 404 and courier_login.json()["message"] == data.ErrorMessages.ERROR_NOT_FOUND