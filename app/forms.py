from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddCandidateForm(FlaskForm):
    cnp = StringField('CNP', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    info_grade = FloatField('Info grade', validators=[DataRequired()])
    math_grade = FloatField('Math grade', validators=[DataRequired()])
    high_school_avg_grade = FloatField(
        'High school avg', validators=[
            DataRequired()])
    admission_grade = FloatField(
        'Admission grade', validators=[
            DataRequired()])
    first_option = IntegerField('First option', validators=[DataRequired()])
    second_option = IntegerField('Second option', validators=[DataRequired()])
    submit = SubmitField('Submit candidate')
