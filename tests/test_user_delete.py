import allure
from lib.assertios import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import time


@allure.epic("Тест кейсы на удаление пользователя")
class TestUserRegister(BaseCase):

    @allure.description("Тест на удаление пользователя которого нельзя удалить ")
    def test_delete_user_by_id_2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        Assertions.assert_status_code(response1, 200)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                      headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response2, 400)
        Assertions.assert_text(response2, "Please, do not delete test users with ID 1, 2, 3, 4 or 5.")

    @allure.description("Тест на успешное удаления пользователя")
    def test_delete_some_user_by_id(self):
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_status_code(response1, 200)

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        login_data = {
            "email": email,
            "password": password,
        }

        response2 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_status_code(response2, 200)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_status_code(response3, 200)

        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response4, 404)
        Assertions.assert_text(response4, "User not found")

    @allure.description("Тест на удаление пользователя по id из под другого пользователя")
    def test_deleting_a_user_by_id_by_others_users(self):
        register_data_1 = self.prepare_registration_data()

        response_1 = MyRequests.post("/user/", data=register_data_1)
        Assertions.assert_status_code(response_1, 200)

        user_id1 = self.get_json_value(response_1, 'id')

        time.sleep(1)

        register_data_2 = self.prepare_registration_data()

        response2 = MyRequests.post("/user/", data=register_data_2)
        Assertions.assert_status_code(response2, 200)

        email = register_data_2['email']
        password = register_data_2['password']
        user_id2 = self.get_json_value(response2, 'id')


        login_data2 = {
            "email": email,
            "password": password,
        }

        response4 = MyRequests.post("/user/login", data=login_data2)
        Assertions.assert_status_code(response4, 200)

        auth_sid = self.get_cookie(response4, "auth_sid")
        token = self.get_header(response4, "x-csrf-token")

        response5 = MyRequests.delete(f"/user/{user_id1}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response5, 200)  # Здесь явный баг!!!

        response6 = MyRequests.get(f"/user/{user_id1}")
        Assertions.assert_status_code(response6, 200)
