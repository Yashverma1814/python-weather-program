import requests
import json
city=input("Enter a city name and hit enter :- ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3b6724281d450616a446e06ff2e67a04"
response=requests.get(url)
python_json = json.loads(response.text)
if python_json["cod"]=='404':
    print("Please enter a valid city")
else:
    main = python_json["main"]
    weather = python_json["weather"]
    print(f"Temperature of {city} is {round(main["temp"]-273)}°C")
    print(f"More Weather Info about {city}")
    print(f"Humidity : {main["humidity"]}%")
    print(f"Description : {weather[0]["description"]}")
    print(f"Feels Like : {round(main["feels_like"]-273)}°C")
    print(f"Temprature Range : {round(main["temp_min"]-273)}°C-{round(main["temp_max"]-273)}°C")