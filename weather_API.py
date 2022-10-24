import requests

API_KEY = "9180dee0e4c1ab0ecbead8a2226bf2fa"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter the city to check: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data['main']['temp']-273)
    print(temperature)
else:
    print("ERROR!")