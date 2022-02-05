from flask import Blueprint, request, render_template, abort

math_func=Blueprint('math_func', __name__)

@math_func.route('/')
def index():
    return render_template("math.html")
    
@math_func.route('/add')
def add():
    if validate():
    # return (f'sum of {a} and {b} is {int(a)+int(b)}')
        result=int(a)+int(b)
        text='sum'
        return render_template("math.html", pg_a=a, pg_b=b, pg_result=result, pg_text=text, pg_error=False)
    else:
        text='Invalid input fields passed'
        return render_template("math.html", pg_a=a, pg_b=b, pg_error=True, pg_text=text)
    
@math_func.route('/sub')
def sub():
    if validate():
        result=int(a)-int(b)
        text='difference'
        return render_template("math.html", pg_a=a, pg_b=b, pg_result=result, pg_text=text, pg_error=False)
    else:
        text='Invalid input fields passed'
        return render_template("math.html", pg_a=a, pg_b=b,pg_error=True,pg_text=text )
@math_func.route('/mul')
def mul():
    if validate():
        result=int(a)*int(b)
        text='product'
        return render_template("math.html", pg_a=a, pg_b=b, pg_result=result, pg_text=text, pg_error=False)
    else:
        text='Invalid input fields passed'
        return render_template("math.html", pg_a=a, pg_b=b, pg_error=True, pg_text=text)
@math_func.route('/div')
def div():
    if validate():
        result=int(a)/int(b)
        text='quotient'
        return render_template("math.html", pg_a=a, pg_b=b,pg_result=result, pg_text=text, pg_error=False)
    else:
        text='Invalid input fields passed'
        return render_template("math.html", pg_a=a, pg_b=b, pg_result=result, pg_text=text, pg_error=False)
 

def validate():
    try:
        global a,b
        a=request.args['a']
        b=request.args['b']
        int(a)
        int(b)
        return True
    except:
        return False
            