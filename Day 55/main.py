from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_func():
        return f"<b>{function()}</b>"
    return wrapper_func

def make_italic(function):
    def wrapper_func():
        return f"<em>{function()}</em>"
    return wrapper_func

def make_underline(function):
    def wrapper_func():
        return f"<u>{function()}</u>"
    return wrapper_func


@app.route("/")
def greetings():
    return "<h1 style='text-align:center'>greetings hello</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src = 'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2021/05/25082143/Alaskan-Malamute-puppy-laying-down-outdoors.jpg'>"


@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"hello {name}, you are {number} years old"


@app.route("/bye")
@make_bold
@make_italic
def say_bye():
    return "bye"


if __name__ == "__main__":
    app.run(debug=True)

greetings()
