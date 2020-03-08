from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms.validators import DataRequired
from wtforms.validators import Email
# from wtforms.validators import Password
from wtforms.validators import Length
from wtforms.validators import EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[ DataRequired(), Length(min=2, max=20)  ])
    email = StringField('Email', validators=[ DataRequired(), Email(), Length(min=6)  ])
    password = PasswordField('Password', validators=[ DataRequired(), Length(min=8)  ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[ DataRequired(), Email(), Length(min=6) ])
    password = PasswordField('Password', validators=[ DataRequired(), Length(min=8)  ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



