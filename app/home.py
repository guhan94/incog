from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from app.forms import EncryptForm
from app.utils import IncogWorkflow


bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def landing():
    form = EncryptForm()
    if request.method == 'POST':
        plain_text = form.enc_val.data
        url = IncogWorkflow().encrypt_user_data(plain_text)
        return redirect(url_for('home.result', encurl=url))
    return render_template('home/landing.html', title='Encrypt', form=form)


@bp.route('/result', methods=['GET'])
def result():
    encurl = request.args['encurl']
    return render_template('home/result.html', title='Secret Encrypted', encurl=f'{request.host_url}display/{encurl}')


@bp.route('/display/<uuid>', methods=['GET'])
def display(uuid):
    plain_text = IncogWorkflow().decrypt_user_data(uuid)
    if plain_text:
        return render_template('home/display.html', title='Secret', value=plain_text.split('\\n'))
    else:
        return render_template('home/nosecret.html', title='No Secret')
