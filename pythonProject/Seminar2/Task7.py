# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def base():
    context = {
        'task': 'Задание 7'
    }
    return render_template('base7.html', **context)


@app.route('/quadro/', methods=['GET', 'POST'])
def quadro():
    context = {
        'task': 'Задание 7'
    }
    if request.method == 'POST':
        number = request.form.get('number')
        return redirect(url_for('result', number=number, number_result=int(number) ** 2))
    return render_template('page_task7.html', **context)


@app.route('/result/<int:number>/<int:number_result>')
def result(number: int, number_result: int):
    return f'Число {number}. Квадрат числа {number_result}'


if __name__ == '__main__':
    app.run(debug=True)
