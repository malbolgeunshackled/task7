import requests

API_KEY = "718510cd1af8c0ef15c6d5e9c7e2d721"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Ошибка запроса: {response.status_code}")
        print(response.text)
        return

    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"\nПогода в городе {city}:")
    print(f"Температура: {temperature} °C")
    print(f"Описание: {description}")
    print(f"Влажность: {humidity}%")
    print(f"Скорость ветра: {wind_speed} м/с")


def main():
    city = input("Введите название города: ")
    get_weather(city)


if __name__ == "__main__":
    main()