from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f'Миссия Колонизация Марса'

@app.route('/index')
def index1():
    return f'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def index2():
    with open('templates/promotion.html', 'r', encoding='utf-8') as stream:
        return stream.read()

@app.route('/image_mars')
def index3():
    with open('templates/ogrizok.html', 'r', encoding='utf-8') as stream:
        return stream.read()

@app.route('/promotion_image')
def index4():
    with open('templates/koloniza.html', 'r', encoding='utf-8') as stream:
        return stream.read()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)