from flask import Flask, render_template
import random
import datetime
import requests



app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    age_params = {
        "name": name
    }
    age_response = requests.get(url="https://api.agify.io", params=age_params)
    age_data = age_response.json()
    age = age_data["age"]
    
    gender_params = {"name": name}
    gender_response = requests.get(url="https://api.genderize.io", params=gender_params)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    return render_template("guess.html", person_name=name, person_gender=gender, person_age=age)


if __name__ == '__main__':
    app.run(debug=True)
