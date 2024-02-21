# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

#TODO: More appropriate to use get instead of reguest.args[]
@app.get('/add')
def add_request():
    """Handles addition get request"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a,b))

@app.get('/sub')
def sub_request():
    """Handles subtraction get request"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a,b))

@app.get('/mult')
def mult_requestt():
    """Handles multiplication get request"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a,b))

@app.get('/div')
def div_request():
    """Handles division get request"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))
