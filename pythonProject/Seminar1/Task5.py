# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".


from flask import Flask

app = Flask(__name__)


@app.route('/first/')
def sum_num():
    return """<h1>Моя первая HTML страница</h1>\n
    <p>"Привет, мир!"</p>"""


if __name__ == '__main__':
    app.run()
