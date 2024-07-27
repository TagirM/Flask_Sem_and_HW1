# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.


from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def base():
    context = {
        'task': 'Задание 5'
    }
    return render_template('base5.html', **context)


@app.route('/calculator/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        number_1 = request.form.get('number_1')
        number_2 = request.form.get('number_2')
        operation = request.form.get('operation')
        match operation:
            case 'add':
                return f'Результат вычисления {int(number_1) + int(number_2)}'
            case 'subtract':
                return f'Результат вычисления {int(number_1) - int(number_2)}'
            case 'multiply':
                return f'Результат вычисления {int(number_1) * int(number_2)}'
            case 'divide':
                if number_2 == '0':
                    return 'Нельзя делить на 0'
                return f'Результат вычисления {int(number_1) / int(number_2)}'
    context = {
        'task': 'Задание 5'
    }
    return render_template('page_task5.html', **context)


if __name__ == '__main__':
    app.run(debug=True)