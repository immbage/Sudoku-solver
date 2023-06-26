from flask import Flask, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from solver import board, solve, print_board

app = Flask(__name__)

app.config['DEBUG'] = True
app.secret_key = "1"

toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    
    
    return render_template('index.html', board=board)

@app.route('/input', methods=['POST','GET'])
def input():
  
    if request.method == 'POST':
        pass
    return render_template('input.html', board=board)
        



if '__main__' == __name__:
    app.run()