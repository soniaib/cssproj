from app import app, menu_actions
from flask import render_template, flash, redirect
from app.forms import AddCandidateForm
from db import DatabaseController as DbC
from app.utils import set_results, get_results

@app.route('/')
@app.route('/index')
def index():
    actions = menu_actions.menu
    return render_template('index.html',
                           title='UAIC Student Admission System',
                           actions=actions)

@app.route('/candidates')
def candidates():
    actions = menu_actions.menu
    candidates = DbC.get_all_candidates(1)
    return render_template('candidates_list.html',
                           title='Candidates List',
                           actions=actions,
						   candidates=candidates)

@app.route('/specializations')
def specializations():
    actions = menu_actions.menu
    specializations = DbC.get_all_specializations()
    return render_template('specializations_list.html',
                           title='Specializations List',
                           actions=actions,
						   specializations=specializations)
						   
@app.route('/add_candidate', methods=['GET', 'POST'])
def add_candidate():
    form = AddCandidateForm()
    actions = menu_actions.menu
    if form.validate_on_submit():
        DbC.save_form_data(form)
        flash('Candidate with CNP {} submitted.'.format(form.cnp.data))
        return redirect('/index')
    return render_template(
        'candidate_form.html',
        title='Add Candidate',
        form=form,
        actions=actions)

@app.route('/admission_results')
def admission_results():
    actions = menu_actions.menu
    set_results()
    results = get_results()
    return render_template(
        'admission_results.html',
        title='Admission Results',
        actions=actions,
        results=results)
