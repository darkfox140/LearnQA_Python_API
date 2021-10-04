from lib.assertios import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

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

    def test_create_user_with_incorrect_email(self):
        email = 'red21example.com'
        data = self.prepare_registration_data(email=email)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", f"Не ожидаемый ответ: {response.content}"

    def test_creating_user_with_a_short_name(self):
        firstName = self.random_string()[1]
        data = self.prepare_registration_data(first_name=firstName)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too short", \
            f"Не ожидаемый ответ: {response.conten}"

    def test_creating_user_with_a_long_name(self):
        firstName = self.random_string()
        data = self.prepare_registration_data(first_name=firstName)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too long", \
            f"Не ожидаемый ответ: {response.conten}"
