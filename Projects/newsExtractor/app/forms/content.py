"""
  User: Liujianhan
  Time: 0:26
 """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

__author__ = 'liujianhan'


class ContentForm(FlaskForm):
    q = StringField('Input your content',
                    validators=[Length(min=1, max=50), DataRequired()])
    submit = SubmitField('Submit')
