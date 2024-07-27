from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clothes/')
def clothes():
    clothes_list = [
        {'title': "Одежда 1",
         'image': "clothes1.jpg"},
        {'title': "Одежда 2",
         'image': "clothes2.jpg"},
        {'title': "Одежда 3",
         'image': "clothes3.jpg"}
    ]
    return render_template('clothes.html', clothes_list=clothes_list)


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {'title': "Обувь 1",
         'image': "shoes1.jpg"},
        {'title': "Обувь 2",
         'image': "shoes2.jpg"},
        {'title': "Обувь 3",
         'image': "shoes3.jpg"}
    ]
    return render_template('shoes.html', shoes_list=shoes_list)


@app.route('/jackets/')
def jackets():
    jackets_list = [
        {'title': "Куртка 1",
         'image': "jacket1.jpg"},
        {'title': "Куртка 2",
         'image': "jacket2.jpg"},
        {'title': "Куртка 3",
         'image': "jacket3.jpg"}
    ]
    return render_template('jackets.html', jackets_list=jackets_list)


if __name__ == '__main__':
    app.run()