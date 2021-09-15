import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = response.history[0]
second_response = response.history[1]
finally_response = response.history[2]

print(first_response.url)
print(second_response.url)
print("Конечный URL", finally_response.url)
