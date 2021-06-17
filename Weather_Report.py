<<<<<<< HEAD
import requests
import json

API_KEY = "API KEY"

user = "yes"
while user == "yes" or user == "y":
    city = input("Enter city name: ")
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(URL)
    json_data = json.loads(res.text)

    if json_data["cod"] != "404":
        weather = json_data["weather"][0]["description"]
        temperature = json_data["main"]["temp"]
        humidity = json_data["main"]["humidity"]
        wind_speed = json_data["wind"]["speed"]
        print(f"Weather:{weather}")
        print(f"Temperature:{temperature} Celsius")
        print(f"Humidity:{humidity}")
        print(f"Wind Speed:{wind_speed}")
    else:
        print("Invalid input or City not found")
    user = input("Search again? (yes/y): ")

=======
import requests
import json

API_KEY = "API KEY"

user = "yes"
while user == "yes" or user == "y":
    city = input("Enter city name: ")
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(URL)
    json_data = json.loads(res.text)

    if json_data["cod"] != "404":
        weather = json_data["weather"][0]["description"]
        temperature = json_data["main"]["temp"]
        humidity = json_data["main"]["humidity"]
        wind_speed = json_data["wind"]["speed"]
        print(f"Weather:{weather}")
        print(f"Temperature:{temperature} Celsius")
        print(f"Humidity:{humidity}")
        print(f"Wind Speed:{wind_speed}")
    else:
        print("City not found")
    user = input("Search again? (yes/y): ")

>>>>>>> origin/main
print("Program ended")