from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import ValidationError
from app.models import User


def validate_email(self, data_field):
    if User.query.filter_by(email=data_field.data).first():
        raise ValidationError(message="The Email has already been taken!")

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError(message="The username has already been taken")


class RegisterForm(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required(), Length(min=4, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    # username = StringField('username', validators=[Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Sign Up')
