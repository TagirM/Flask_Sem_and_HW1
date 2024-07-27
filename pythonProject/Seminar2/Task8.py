# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)

app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def base():
    context = {
        'task': 'Задание 8'
    }
    return render_template('base8.html', **context)


# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         # Обработка данных формы
#         flash('Форма успешно отправлена!', 'success')
#         return redirect(url_for('form'))
#     return render_template('form.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    context = {
        'task': 'Задание 8'
    }
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('page_task8.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

