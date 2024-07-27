# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base4.html')


@app.route('/counter/', methods=['GET', 'POST'])
def counter():
    if request.method == 'POST':
        text = request.form.get('text')
        return f"Количество слов {len(text.split())}"
    return render_template('page_task4.html')


if __name__ == '__main__':
    app.run(debug=True)
