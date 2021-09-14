import random

from flask import Flask

app = Flask(__name__)

x = random.randint(0, 9)
print(f"random number is {x}")


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper





@app.route("/")
@make_bold
def home_page():
    return "Guess a number between 0 and 9" \
           "<img src='https://media0.giphy.com/media/3o7TKRVBGOSdSODGJa/giphy.gif?cid=ecf05e47pticseupjr5ct1qv0t51smhe0f6h91ws98igc3zn&rid=giphy.gif&ct=g' width=200 height=200"


@app.route("/<int:number>")
def correct_number(number):
    if number == x:
        return "You have found the right number"
    elif number > x:
        return "Your guess is too big"
    else:
        return "Your guess is too small"


if __name__ == "server":
    app.run(debug=True)
