from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TimeField, DateField
from wtforms.validators import DataRequired
from datetime import datetime, date


class LoginForm(FlaskForm):
    username = StringField('Task', validators=[DataRequired()])
    description = StringField('Task Description', validators=[DataRequired()])
    start = DateField('Start', default=datetime.today)
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Rememeber Me')
    submit = SubmitField('Sing In')
