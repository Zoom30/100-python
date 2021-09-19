import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


@app.route('/blog')
def blog():
    url = "https://api.npoint.io/e4ca8b2293da79c313ea"
    response = requests.get(url=url)
    data = response.json()
    return render_template("blog.html", posts=data)

if __name__ == '__main__':
    app.run(debug=True)