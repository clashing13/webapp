from flask import Blueprint,request, render_template, abort

login=Blueprint('login', __name__)

@login.route('/')
def index():
    return render_template("login.html")

@login.route('/signin')
def signin():
    name=request.args['name']
    age=request.args['age']
    return (f'{name}, you are now logged in at {age} years')
    