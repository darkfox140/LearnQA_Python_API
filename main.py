import requests


def check_http_methods():

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


check_http_methods()
