from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

from app.models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.', validators=[Required()])
    submit = SubmitField('Save')


class CreateBlog(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Blog Content', validators=[Required()])
    submit = SubmitField('Post')
