from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'test'}
    return render_template('index.html', title = 'Student admission', user=user)