from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class EncryptForm(FlaskForm):
    enc_val = StringField('Encrypt', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Encrypt')
