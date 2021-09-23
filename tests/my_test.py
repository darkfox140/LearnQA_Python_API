import requests


class TestShortPhraseTest:
    def test_check_phrase(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookies = response.cookies

        assert response.status_code == 200
        assert cookies == {'HomeWork': 'hw_value'}