import allure
import requests
import data
import helper
import scooter_api
import urls


class TestCreateCourier:                                # Тесты на endpoint «Создать курьера»
    @allure.title("Проверка успешного создания курьера")
    @allure.description("Создание шаблонного курьера, проверка статуса ответа и тела ответа")
    def test_success_create_courier(self, default_courier):
        create_courier_request = default_courier
        assert create_courier_request.status_code == 201 and create_courier_request.json()["ok"] == True


    @allure.title("Проверка появления ошибки при создании двух одинаковых курьеров")
    @allure.description("Создание двух одинаковых курьеров, проверка статуса ответа и тела ответа")
    def test_create_duplicate_courier(self):
        body = helper.new_courier_login_password()
        requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, body)               # создали первого курьера с body
        duplicate_courier_request = scooter_api.create_courier(body)                    # создали второго курьера с body
        login_body = body.copy()
        login_body.pop("firstName", None)
        id_courier = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=login_body).json().get("id")
        requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(id_courier))
        assert duplicate_courier_request.status_code == 409 and duplicate_courier_request.json()["message"] == data.ErrorMessages.ERROR_MESSAGE_FAIL_NAME


    @allure.title("Проверка появления ошибки при создании курьера с пустым полем 'login'")
    @allure.description("Создание курьера с пустым полем 'login', проверка статуса ответа и тела ответа")
    def test_empty_login_create_courier(self):
        body_login = helper.ChangeTestDataHelper.modify_create_courier_body("login", "")
        empty_login_courier_request = scooter_api.create_courier(body_login)
        assert empty_login_courier_request.status_code == 400 and empty_login_courier_request.json()["message"] == data.ErrorMessages.ERROR_NOT_ENOUGH_DATA


    @allure.title("Проверка появления ошибки при создании курьера с пустым полем 'password'")
    @allure.description("Создание курьера с пустым полем 'password', проверка статуса ответа и тела ответа")
    def test_empty_password_create_courier(self):
        body_pass = helper.ChangeTestDataHelper.modify_create_courier_body("password", "")
        empty_password_courier_request = scooter_api.create_courier(body_pass)
        assert empty_password_courier_request.status_code == 400 and empty_password_courier_request.json()[
            "message"] == data.ErrorMessages.ERROR_NOT_ENOUGH_DATA


    @allure.title("Проверка появления ошибки при создании курьера с пустым полем 'firstname'")
    @allure.description("Создание курьера с пустым полем 'firstname', проверка статуса ответа и тела ответа")
    def test_empty_firstname_create_courier(self):
        body_firstname = helper.ChangeTestDataHelper.modify_create_courier_body("firstname", "")
        empty_firstname_courier_request = scooter_api.create_courier(body_firstname)
        assert empty_firstname_courier_request.status_code == 400 and empty_firstname_courier_request.json()[
            "message"] == data.ErrorMessages.ERROR_NOT_ENOUGH_DATA
