
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = """
    <html>
        <body>
            <h1>My Home Page</h1>
            <p>Welcome to my simple app!</p>
            <a href='/welcome'>Go to Welcome page</a>
        </body>
    </html>
    """
    return html

@app.route("/welcome")
def welcome_page():
    return "welcome"

@app.route("/welcome/home")
def welcome_home():
    return "welcome home"

@app.route("/welcome/back")
def welcome_back():
    return "welcome back"