#! -*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


# login form
class UserLoginForm(FlaskForm):
    username = StringField(id='username', validators=[DataRequired()])
    password = PasswordField(id='password', validators=[DataRequired()])


# register_person form
class RegisterPersonForm(FlaskForm):
    phone = StringField(id='phone', validators=[DataRequired()])
    name = StringField(id='name', validators=[DataRequired()])
    location = StringField(id='location', validators=[DataRequired()])
    card_type = StringField(id='card_type', validators=[DataRequired()])
    card_num = StringField(id='card_num', validators=[DataRequired()])
    address = StringField(id='address', validators=[DataRequired()])
    password = StringField(id='password', validators=[DataRequired()])
    email = StringField(id='email', validators=[DataRequired()])


# register_company form
class RegisterCompanyForm(FlaskForm):
    name = StringField(id='name', validators=[DataRequired()])
    card_type = StringField(id='card_type', validators=[DataRequired()])
    card_num = StringField(id='card_num', validators=[DataRequired()])
    location = StringField(id='location', validators=[DataRequired()])
    mail_code = StringField(id='mail_code', validators=[DataRequired()])
    password = StringField(id='password', validators=[DataRequired()])
    email = StringField(id='email', validators=[DataRequired()])
    per_phone = StringField(id='per_phone', validators=[DataRequired()])
    per_name = StringField(id='per_name', validators=[DataRequired()])
    address = StringField(id='address', validators=[DataRequired()])
