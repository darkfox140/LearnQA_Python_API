import requests
import json
import time


def longtime_job():
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
        print(respons_3.status_code)


longtime_job()


'''def check_http_methods():

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
                                      result.text == '{"success":"!"}'))


check_http_methods()'''