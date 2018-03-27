#! -*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class PeixunApplyForm(FlaskForm):
    username = StringField(id='username', validators=[DataRequired()])
    phone = StringField(id='', validators=[DataRequired()])
    card_num = StringField(id='', validators=[DataRequired()])
    address = StringField(id='', validators=[DataRequired()])
    date = StringField(id='', validators=[DataRequired()])
    reason = StringField(id='', validators=[DataRequired()])
    content = StringField(id='', validators=[DataRequired()])


class PatentApplyForm(FlaskForm):
    name = StringField(id='', validators=[DataRequired()])
    type = StringField(id='', validators=[DataRequired()])
    main_per_name = StringField(id='', validators=[DataRequired()])
    first_per_name = StringField(id='', validators=[DataRequired()])
    first_per_phone = StringField(id='', validators=[DataRequired()])
    first_per_card_num = StringField(id='', validators=[DataRequired()])
    first_per_address= StringField(id='', validators=[DataRequired()])
    date = StringField(id='', validators=[DataRequired()])
    priority = StringField(id='', validators=[DataRequired()])
    description = StringField(id='', validators=[DataRequired()])


class FeeApplyForm(FlaskForm):
    patent_id = StringField(id='', validators=[DataRequired()])
    name = StringField(id='', validators=[DataRequired()])
    phone = StringField(id='', validators=[DataRequired()])
    date = StringField(id='', validators=[DataRequired()])
    description = StringField(id='', validators=[DataRequired()])


class TradeApplyForm(FlaskForm):
    username = StringField(id='', validators=[DataRequired()])
    phone = StringField(id='', validators=[DataRequired()])
    date = StringField(id='', validators=[DataRequired()])
    patent_id = StringField(id='', validators=[DataRequired()])


class TradePerchaseForm(FlaskForm):
    username = StringField(id='', validators=[DataRequired()])
    phone = StringField(id='', validators=[DataRequired()])
    date = StringField(id='', validators=[DataRequired()])
    patent_id = StringField(id='', validators=[DataRequired()])

