from flask import Blueprint,request, render_template, abort

login=Blueprint('login', __name__)

@login.route('/signin')
def func():
    name=request.args['name']
    age=request.args['age']
    return (f'{name}, you are now logged in at {age} years')