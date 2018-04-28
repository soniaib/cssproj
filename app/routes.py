from app import app, menu_actions
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    actions = menu_actions.frontpage
    return render_template('index.html',
                           title = 'Student admission',
                           actions = actions)