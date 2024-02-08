from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f'Миссия Колонизация Марса'

@app.route('/index')
def index1():
    return f'И на Марсе будут яблони цвести!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)