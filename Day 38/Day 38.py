import requests
from datetime import datetime
import api_keys


now = datetime.now()
formatted_now_date = now.strftime("%d/%m/%Y")
formatted_now_time = now.time().strftime("%H:%M:%S")
exercise_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/dd81a891f83891fcffdab1dcc7c5a53e/casualWorkoutTracking/workouts"



exercise_params = {
    "query": input("Tell me which exercises you did today: \n"),
    "gender": api_keys.GENDER,
    "weight_kg": api_keys.WEIGHT_KG,
    "height_cm": api_keys.HEIGHT_CM,
    "age": api_keys.AGE

}

exercise_response = requests.post(url=exercise_ep, headers=api_keys.header, json=exercise_params)
exercise_data = exercise_response.json()

headers = {
    "Authorization": f"Bearer {api_keys.BEARER_TOKEN}"
}

for exercise in exercise_data["exercises"]:
    print(exercise)
    print("==========================================")

    body = {
        "workout": {
            "date": formatted_now_date,
            "time": formatted_now_time,
            "exercise": exercise["name"],
            "calories": exercise["nf_calories"],
            "duration": exercise["duration_min"]
        }
    }
    sheety_response = requests.post(url=sheety_url, json=body, headers=headers)
    sheety_data = sheety_response.json()
    print(sheety_data)
