# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/students/')
def students():
    head = {
        'firstname': 'Имя',
        'lastname': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл'
    }
    students_dict = [
        {'firstname': 'Иван',
         'lastname': 'Иванов',
         'age': 18,
         'rating': 4},
        {'firstname': 'Петр',
         'lastname': 'Петров',
         'age': 19,
         'rating': 4.5},
        {'firstname': 'Семен',
         'lastname': 'Семенов',
         'age': 20,
         'rating': 4.8}
    ]
    return render_template('students.html', **head, students_dict=students_dict)


if __name__ == '__main__':
    app.run()
