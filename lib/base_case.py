from requests import Response
import json.decoder
from datetime import datetime
import random
import string


class BaseCase:

    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Не удается найти файл cookie с именем {cookie_name} в последнем ответе"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Не удается найти header с именем {headers_name} в последнем ответе"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Ответ не в формате JSON. Текст ответа '{response.text}'"

        assert name in response_as_dict, f"В ответе JSON нет ключа '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email=None, first_name='firstName',
                                  last_name='learnqa', user_name='learnqa', password='123'):
        if email is None:
            base_part = "learnqa"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            domain = "example.com"
            email = f"{base_part}{random_part}@{domain}"
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if user_name:
            self.user_name = user_name
        if password:
            self.password = password

        return {
            'password': password,
            'username': user_name,
            'firstName': first_name,
            'lastName': last_name,
            'email': email
        }

    def random_string(self, length):
        return "".join([random.choice(string.ascii_lowercase) for e in range(length)])
