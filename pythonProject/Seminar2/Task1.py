# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/next/')
def next_page():
    return 'Привет, Юзер!'


if __name__ == '__main__':
    app.run(debug=True)

    