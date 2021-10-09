import allure

from lib.assertios import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import time


@allure.epic("Тесты на запрос данных пользователя")
class TestUserGet(BaseCase):

    @allure.description("Тест на запрос User name будучи не авторизованным")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_status_code(response, 200)

        Assertions.assert_json_has_key(response, "username")
        expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response, expected_fields)

    @allure.description("Тест на получение данных будучи авторизованным этим пользователем")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        Assertions.assert_status_code(response1, 200)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_status_code(response2, 200)

        expected_fields = ["username", "email", "firstName", "lastName"]

        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.description("Тест запрос данных будучи авторизованным другим пользователем")
    def test_get_user_details_some_users(self):
        data_register1 = self.prepare_registration_data()
        time.sleep(1)
        data_register2 = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=data_register1)
        Assertions.assert_status_code(response1, 200)

        response2 = MyRequests.post("/user/", data=data_register2)
        Assertions.assert_status_code(response2, 200)

        email = data_register1['email']
        password = data_register1['password']
        user_name = data_register1['username']
        user_id = self.get_json_value(response2, 'id')

        new_login = {
            "email": email,
            "password": password,
        }

        response3 = MyRequests.post("/user/login", data=new_login)
        Assertions.assert_status_code(response3, 200)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["email", "firstName", "lastName", "password"]
        Assertions.assert_json_has_not_keys(response4, expected_fields)
        Assertions.assert_json_value_by_name(response4, "username", user_name, "имя пользователя не совпадает")
