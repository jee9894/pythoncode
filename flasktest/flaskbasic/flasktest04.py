from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login/')
def login():
    pass


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next = '/', username = 'hong'))
