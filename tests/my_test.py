import requests


class TestShortPhraseTest:
    def test_check_phrase(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        data = {'HomeWork': 'hw_value'}
        response = requests.get(url, params=data)
        cookies = response.cookies

        assert response.status_code == 200
        assert cookies == {'HomeWork': 'hw_value'}