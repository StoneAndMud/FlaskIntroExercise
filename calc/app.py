# Put your app in here.
from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def add(a, b):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = a + b
    return str(answer)


@app.route('/sub')
def sub(a, b):

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = a - b
    return str(answer)


@app.route('/mult')
def mult(a, b):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = a * b
    return str(answer)


@app.route('/div')
def div(a, b):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = a / b
    return str(answer)


@app.route('/math/<operation>')
def do_math(operation, a, b):
    """Returns string of a number, after completing the given operation"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = 0

    if operation == "add":
        answer = a + b
        return str(answer)
    elif operation == "sub":
        answer = a - b
        return str(answer)
    elif operation == "mult":
        answer = a * b
        return str(answer)
    elif operation == "div":
        answer = a / b
        return str(answer)
    else:
        return "this is not a correct operation"
