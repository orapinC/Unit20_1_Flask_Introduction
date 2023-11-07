from flask import Flask, request
from operations import add, sub, mult, div

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

@app.route("/add")
def get_add():
    """respond to https://host(127.0.0.1:5000)/add?a=3&b=6"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(add(a,b))
    return result

@app.route("/sub")
def get_sub():
    """respond to https://host(127.0.0.1:5000)/sub?a=3&b=6"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(sub(a,b))
    return result

@app.route("/mult")
def get_mult():
    """respond to https://host(127.0.0.1:5000)/mult?a=3&b=6"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(mult(a,b))
    return result

@app.route("/div")
def get_div():
    """respond to https://host(127.0.0.1:5000)/div?a=3&b=6"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(div(a,b))
    return result

operate = {
    "add" : add,
    "sub" : sub,
    "mult": mult,
    "div" : div,
}

@app.route("/math/<oprtn>")
def do_math(oprtn):
    """respond to /math/add(or sub, mult, div)?a=60&b=2"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(operate[oprtn](a,b))
    return result