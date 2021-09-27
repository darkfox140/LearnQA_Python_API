import requests
import pytest
import json


class TestUserAgent:
    test_data = [
        {
            "header": 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            "expected_result":
                {'platform': 'Mobile',
                 'browser': 'No',
                 'device': 'Android'}
            },
        {
            "header": 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
            "expected_result":
                {'platform': 'Mobile',
                 'browser': 'Chrome',
                 'device': 'iOS'}
            },
        {"header": 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
         "expected_result":
             {'platform': 'Googlebot',
              'browser': 'Unknown',
              'device': 'Unknown'}
         },
        {
            "header": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
            "expected_result":
                {'platform': 'Web',
                 'browser': 'Chrome',
                 'device': 'No'}
        },
        {
            "header": 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            "expected_result":
                {'platform': 'Mobile',
                 'browser': 'No',
                 'device': 'iPhone'}
        }
    ]

    @pytest.mark.parametrize('data', test_data)
    def test_check_user_agent(self, data):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response = requests.get(url, headers={"User-Agent": data["header"]})
        response_dict = response.json()
        expected_dict = data["expected_result"]

        assert response.status_code == 200, "Wrong response code"
        assert "platform" in response_dict, "Поля 'platform' нету в ответе"
        assert "browser" in response_dict, "Поля 'browser' нету в ответе"
        assert "device" in response_dict, "Поля 'device' нету в ответе"

        assert response_dict["platform"] == expected_dict["platform"], f"Для варианта {data['header']} \n Поле platform не соответствует ожидаемому результату"
        assert response_dict["browser"] == expected_dict["browser"], f"Для варианта {data['header']} \n Поле browser не соответствует ожидаемому результату"
        assert response_dict["device"] == expected_dict["device"], f"Для варианта {data['header']} \n Поле device не соответствует ожидаемому результату"
