import requests
import json
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
try:
    place = input("Enter the name of the place:\n")
    url = f"https://api.weatherapi.com/v1/current.json?key={Your_API_key}&q={place}"
    r = requests.get(url)
    dic = json.loads(r.text)
    temp = (dic["current"]["temp_c"])
    print(temp)
    engine.say(f"The current temperature is {temp} degree celsius")
    # Wait for the speech to finish
    engine.runAndWait()
except KeyError:
    print("Enter the correct place")


