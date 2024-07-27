# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.


from pathlib import PurePath, Path

from flask import Flask, render_template, request
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base3.html')


@app.route('/login/', methods=['GET', 'POST'])
def authorization():
    login = {
        'auth_email': '1@mail.ru',
        'auth_pass': '123'
    }
    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pass = request.form.get('auth_pass')
        if auth_email == login['auth_email'] and auth_pass == login['auth_pass']:
            return f"Вход с почты {escape(auth_email)} выполнен"
        else:
            return 'Ошибка входа'

    return render_template('base3.html')


if __name__ == '__main__':
    app.run(debug=True)