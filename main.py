from json.decoder import JSONDecodeError
import requests

payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("http://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response.text)
print(response.status_code)
print(dict(response.cookies))
print(response.headers)

