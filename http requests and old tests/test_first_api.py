import requests
import pytest


class TestFirstAPI:
    names = [
        ("Vitalii"),
        ("Arseniy"),
        ("")
    ]

    @pytest.mark.parametrize("name", names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/ajax/api/hello"
        data = {"name": name}

        respons = requests.get(url, params=data)
        assert respons.status_code == 200, "Wrong response code"

        respons_dict = respons.json()
        assert "answer" in respons_dict, "Where is no field 'answer' in the response"

        if len(name) == 0:
            expected_respons_text = "Hello, someone"
        else:
            expected_respons_text = f"Hello, {name}"

        actual_respons_text = respons_dict["answer"]
        assert expected_respons_text == actual_respons_text, "Actual text in the response is not correct"
