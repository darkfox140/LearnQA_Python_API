import requests
import json


class TestShortPhraseTest:
    def test_check_phrase(self):
        url = "https://playground.learnqa.ru/api/homework_header"

        response = requests.get(url)
        assert response.status_code == 200, "Wrong response code"

        actual_response_text = response.headers['x-secret-homework-header']
        expected_response_text = 'Some secret value'

        assert 'x-secret-homework-header' in response.headers
        assert expected_response_text == actual_response_text
