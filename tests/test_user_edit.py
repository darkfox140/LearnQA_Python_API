import allure

from lib.base_case import BaseCase
from lib.assertios import Assertions
from lib.my_requests import MyRequests


@allure.epic("Тесты на редактирования полей пользователя")
class TestUserEdit(BaseCase):

    @allure.description("Тест на редактирование имени будучи авторизованным")
    def test_edit_just_created_user(self):
        # Регистрация
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        firstName = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Логгин
        login_data = {
            'email': email,
            'password': password,
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Редактирование
        new_name = "Change Name Party"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_status_code(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Неверное имя пользователя после редактирования"
        )

    @allure.description("Тест на редактирование имени без авторизации")
    def test_edit_created_user_without_auth(self):
        # Регистрация
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Редактирование
        new_name = "Goblin"

        response2 = MyRequests.put(f"/user/{user_id}", data={'firstName': new_name})
        Assertions.assert_status_code(response2, 400)

        # Логгин
        login_data = {
            'email': email,
            'password': password,
        }

        response3 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid},)

        Assertions.assert_status_code(response2, 400)
        Assertions.assert_json_value_wrong_name(
            response4, "firstName", new_name, "Имя пользователя изменено без авторизации!!!")

    @allure.description("Тест на редактирование почты без @")
    def test_mail_changesby_an_autho_user(self):
        # Регистрация
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        firstName = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Логгин
        login_data = {
            'email': email,
            'password': password,
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Редактирование
        new_email = "394xample.com"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_status_code(response3, 400)
        assert response3.content.decode("utf-8") == "Invalid email format", f"Не ожидаемый ответ: {response.content}"

    @allure.description("Тест на редактирование имени на один символ")
    def test_name_changes_by_an_authorized_user(self):
        # Регистрация
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Логгин
        login_data = {
            'email': email,
            'password': password,
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Редактирование
        new_name = "a"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_status_code(response3, 400)
        Assertions.assert_json_value_by_name(response3, "error", "Too short value for field firstName",
                                             "Редактирование удалось, а не должно быть!!!")
