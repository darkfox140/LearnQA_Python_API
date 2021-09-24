import requests


class TestCookies:
    def test_check_cookies(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookies = response.cookies
        print(dict(cookies))

        assert response.status_code == 200, "Wrong response code"
        assert "HomeWork" in cookies, "В cookies нет поля 'HomeWork'"

        expected_response_cookies_value = 'hw_value'
        actual_response_cookies_value = cookies['HomeWork']
        assert expected_response_cookies_value == actual_response_cookies_value, "Значения cookies не совпадают"
