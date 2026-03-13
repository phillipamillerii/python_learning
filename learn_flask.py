from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login", methods=['GET']):
def login():
    

if __name__ == '__main__':
    app.run(debug=True)

