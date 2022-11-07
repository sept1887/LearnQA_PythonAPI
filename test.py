import requests
import json

params = {"buildingIds[]": 121}
headers = {"content-type": "application/json"}
response = requests.get("https://qa-api.worklib.io/buildings/details", headers=headers, params=params)

print(response.status_code)
print(response.raise_for_status())
print(response.url)
print(response.json())



