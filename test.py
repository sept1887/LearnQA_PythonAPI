import requests

data = {"email": "hades1887@yandex.ru", "password": "V!ka1234"}
headers = {"content-type": "application/json"}
response = requests.post("https://stagingapi.worklib.io/auth/login", headers=headers, data=data)

print(response.json())