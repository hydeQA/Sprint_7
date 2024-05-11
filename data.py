class TestDataCreatingOrder:
    CREATE_ORDER_BODY = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

class ErrorMessages:
    ERROR_MESSAGE_FAIL_NAME = "Этот логин уже используется"
    ERROR_NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"
    ERROR_NOT_FOUND = "Учетная запись не найдена"
    ERROR_NOT_ENOUGH_LOGIN_DATA = "Недостаточно данных для входа"