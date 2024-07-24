# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/news/')
def news():
    news_block = [
        {'title': 'Новость 1',
         'description': 'Описание новости 1',
         'date_creation': datetime.now().strftime('%d.%m.%Y года')},
        {'title': 'Новость 2',
         'description': 'Описание новости 2',
         'date_creation': datetime.now().strftime('%d.%m.%Y года')},
        {'title': 'Новость 1',
         'description': 'Описание новости 3',
         'date_creation': datetime.now().strftime('%d.%m.%Y года')},
    ]
    return render_template('news.html', news_block=news_block)


if __name__ == '__main__':
    app.run()
