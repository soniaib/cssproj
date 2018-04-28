from app import app, menu_actions
from flask import render_template, flash, redirect
from app.forms import AddCandidateForm
from app.utils import get_results
from db import DatabaseController as DbC

@app.route('/')
@app.route('/index')
def index():
    actions = menu_actions.menu
    return render_template('index.html',
                           title='Student admission',
                           actions=actions)


@app.route('/add_candidate', methods=['GET', 'POST'])
def add_candidate():
    form = AddCandidateForm()
    actions = menu_actions.menu
    if form.validate_on_submit():
        new_candidate = DbC.Candidate()
        new_candidate.cnp = form.cnp.data
        new_candidate.first_name = form.first_name.data
        new_candidate.surname = form.surname.data
        new_candidate.email = form.email.data
        new_candidate.info_grade =  form.info_grade.data
        new_candidate.math_grade = form.math_grade.data
        new_candidate.high_school_avg_grade = form.high_school_avg_grade.data
        new_candidate.admission_grade = form.admission_grade.data
        new_candidate.first_option = form.first_option.data
        new_candidate.second_option = form.second_option.data
        DbC.save_candidate(new_candidate)
        flash('Candidate with CNP {} submitted.'.format(form.cnp.data))
        return redirect('/index')
    return render_template(
        'candidate_form.html',
        title='Add candidate',
        form=form,
        actions=actions)

@app.route('/admission_results')
def admission_results():
    actions = menu_actions.menu
    results = get_results()
    #results = [{'name': 'Sonia', 'status': 'Accepted'}, {'name': 'John Doe', 'status': 'Rejected'}]
    return render_template(
        'admission_results.html',
        title='Admission Results',
        actions=actions,
        results=results)
