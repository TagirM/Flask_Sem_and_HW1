# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

import logging

from flask import Flask, render_template, request, abort

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def base():
    context = {
        'task': 'Задание 6'
    }
    return render_template('base6.html')


@app.errorhandler(403)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Доступ запрещен по возрасту',
        'url': request.base_url,
}
    return render_template('403.html', **context), 403


@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    MIN_AGE = 18
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if MIN_AGE < int(age):
            return f'{name}, вы вошли'
        abort(403)
    context = {
        'task': 'Задание 6'
    }
    return render_template('page_task6.html', **context)


if __name__ == '__main__':
    app.run(debug=True)