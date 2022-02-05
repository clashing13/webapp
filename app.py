from flask import Flask, render_template
from login import login
from math_func import math_func
from tictactoe import tictactoe

app = Flask(__name__) 
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(math_func, url_prefix='/math')
app.register_blueprint(tictactoe, url_prefix='/tictactoe')


@app.route('/')
def index():
    return render_template("app.html")
    
