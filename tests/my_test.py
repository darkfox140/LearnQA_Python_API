import requests


class TestHeader:
    def test_check_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        headers = response.headers
        print(headers)

        assert response.status_code == 200, "Wrong response code"
        assert "x-secret-homework-header" in headers, "В headers нет поля 'x-secret-homework-header'"

        expected_response_headers_value = 'Some secret value'
        actual_response_headers_value = headers['x-secret-homework-header']
        assert expected_response_headers_value == actual_response_headers_value, "Значения headers не совпадают"
