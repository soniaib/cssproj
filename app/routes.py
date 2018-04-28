from app import app
from flask import render_template
from app.counter import count

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'test'}
    test_string = count.bar()
    return render_template('index.html', title = 'Student admission', user=user, teststr = test_string)