import requests

url = "http://localhost:8000"

data = {"cart_value": 7.90, "delivery_distance": 2.235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("POST request successful!")
    print("Response:", response.text)
else:
    print(f"POST request failed with status code {response.status_code}")
