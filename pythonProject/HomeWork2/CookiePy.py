# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет
# создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, redirect, render_template, request, url_for, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def authorization():
    context = {
        'title': 'Форма авторизации'
    }
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('hello')))
        response.set_cookie('username', name)
        response.set_cookie('email', email)
        return response
    return render_template('authorization.html', **context)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    context = {
        'title': 'Приветствие'
    }
    name = request.cookies.get('username')
    if request.method == 'POST':
        response = make_response(redirect(url_for('authorization')))
        response.delete_cookie('username')
        response.delete_cookie('email')
        return response
    return render_template('hello.html', **context, name=name)


if __name__ == '__main__':
    app.run(debug=True)

