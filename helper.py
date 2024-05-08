import data


class ChangeTestDataHelper:
    @staticmethod
    def modify_create_courier_body(key, value):
        body = data.register_new_courier_and_return_login_password().copy()
        body[key] = value
        return body