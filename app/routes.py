from app import app, menu_actions
from flask import render_template, flash, redirect
from app.forms import AddCandidateForm


@app.route('/')
@app.route('/index')
def index():
    actions = menu_actions.menu
    return render_template('index.html',
                           title='Student admission',
                           actions=actions)


@app.route('/add_candidate', methods=['GET', ' POST'])
def add_candidate():
    form = AddCandidateForm()
    actions = menu_actions.menu
    if form.validate_on_submit():
        flash('Candidate with CNP {} submitted.'.format(form.cnp.data))
        return redirect('/index')
    return render_template(
        'candidate_form.html',
        title='Add candidate',
        form=form,
        actions=actions)
