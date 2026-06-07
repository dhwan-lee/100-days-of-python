import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 177
AGE = 20

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/0f3c241dcb20e171108815d76343fcff/myWorkouts/sheet1"

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    #Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        auth=(
            USER_NAME, 
            PASSWORD,
        )
    )
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)