from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add():
    """Add a and b parameters."""
    a = request.args["a"]
    b = request.args["b"]
    return f"{add(a, b)}"

@app.route('/sub')
def sub():
    """Subtract a and b parameters."""
    a = request.args["a"]
    b = request.args["b"]
    return f"{sub(a, b)}"

@app.route('/mult')
def mult():
    """Multiply a and b parameters."""
    a = request.args["a"]
    b = request.args["b"]
    return f"{mult(a, b)}"

@app.route('/div')
def div():
    """Divide a and b parameters."""
    a = request.args["a"]
    b = request.args["b"]
    return f"{div(a, b)}"