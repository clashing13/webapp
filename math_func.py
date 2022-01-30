from flask import Blueprint, request, render_template, abort

math_func=Blueprint('math_func', __name__)

global a,b
a=0
b=0

@math_func.route('/')
def index():
    return('To access math functions type / add mul sub or div at the end of the url')
    
@math_func.route('/add')
def add():
    if validate():
        return (f'sum of {a} and {b} is {int(a)+int(b)}')
    else:
        return('invalid input')
    
@math_func.route('/sub')
def sub():
    if validate():
        return (f'difference of {a} and {b} is {int(a) - int(b)}')
    else:
        return(f'Invalid input {request.args}')
@math_func.route('/mul')
def mul():
    if validate():
        return (f'product of {a} and {b} is {int(a)*int(b)}')
    else:
        return('invalid input')
@math_func.route('/div')
def div():
    if validate():
        return (f'quotient of {a} and {b} is {int(a)/int(b)}')
    else:
        return('Invalid input')
 

def validate():
    try:
        a=request.args['a']
        b=request.args['b']
        int(a)
        int(b)
        return True
    except:
        return False
            