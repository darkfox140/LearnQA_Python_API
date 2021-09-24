import requests


class TestCheckCookie:
    def test_check_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        
        response = requests.get(url)

        assert response.status_code == 200, "Wrong response code"

        cookies = response.cookies
        print(dict(cookies))

        assert "HomeWork" in cookies, "Значение 'HomeWork' отсутствует в cookies"

        expected_response_cookies_value = 'hw_value'
        actual_response_cookies_value = cookies['HomeWork']
        assert expected_response_cookies_value == actual_response_cookies_value, "Значения cookies не совпадают"
