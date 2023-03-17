from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=3, max=12)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=3, max=12)])
    birthday  = DateField('Birthdate',format='%Y-%m-%d')
    gender = RadioField("Gender", choices=[("Male", 'Male'), ("Female", "Female")], default="Male", validators=[DataRequired()])
    email_address = StringField("Email Address", validators=[DataRequired(), Email(), ])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=12)])
    confirm_password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=12), EqualTo('password')])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email_address = StringField("Email Address", validators=[DataRequired(), Email() ])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=12)])
    submit = SubmitField("Login")
