from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length


class EncryptForm(FlaskForm):
    enc_val = StringField('Encrypt', validators=[DataRequired(),
                                                 Length(max=1000,
                                                        message='Your secret is too long, limit: 10000 chars')],
                          widget=TextArea())
    submit = SubmitField('Encrypt')
