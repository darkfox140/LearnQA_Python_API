import allure

from lib.assertios import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import pytest


@allure.epic("Тесты на создание пользователей")
class TestUserRegister(BaseCase):

    test_params = [
        ({'password': 'qwerty', 'username': 'qwerty', 'firstName': 'qwerty', 'lastName': 'qwerty'}, 'email'),
        ({'username': 'qwerty', 'firstName': 'qwerty', 'lastName': 'qwerty', 'email': 'test@example.com'}, 'password'),
        ({'password': 'qwerty', 'firstName': 'qwerty', 'lastName': 'qwerty', 'email': 'test@example.com'}, 'username'),
        ({'password': 'qwerty', 'username': 'qwerty', 'lastName': 'qwerty', 'email': 'test@example.com'}, 'firstName'),
        ({'password': 'qwerty', 'username': 'qwert', 'firstName': 'qwerty', 'email': 'test@example.com'}, 'lastName')
    ]

    @allure.description("Успешный тест на создание пользователя")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data(first_name='firstName')

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email=email)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Не ожидаемый ответ: {response.content}"

    @allure.description("Негативный тест на создание пользователя с не коректной почтой")
    def test_create_user_with_incorrect_email(self):
        email = 'red21example.com'
        data = self.prepare_registration_data(email=email)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", f"Не ожидаемый ответ: {response.content}"

    @allure.description("Негативный тесты на не передачу данных без одного обязательного параметра")
    @pytest.mark.parametrize('test', test_params)
    def test_creating_user_with_an_empty_field(self, test):
        data, empty_key = test

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {empty_key}", \
            f"Не ожидаемый ответ: {response.conten}"

    @allure.description("Негативный тест на передачу имени в один симфол")
    def test_creating_user_with_a_short_name(self):
        firstName = self.random_string(1)
        data = self.prepare_registration_data(first_name=firstName)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too short", \
            f"Не ожидаемый ответ: {response.conten}"

    @allure.description("Негативный тест на передачу очень большого имени больше 251 символа")
    def test_creating_user_with_a_long_name(self):
        first_name = self.random_string(251)
        data = self.prepare_registration_data(first_name=first_name)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too long", \
            f"Не ожидаемый ответ: {response.conten}"
