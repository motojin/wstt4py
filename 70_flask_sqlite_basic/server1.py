import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
#
#def user_name():
#    user_name = input('What is your name?')
#def user_age():
#    user_age = input('What is your age?')
#def user_area():
#    user_area = input('Where are you living?')

@app.route('/value', methods=['GET', 'POST'])
def value():
    if request.method == 'GET':
        conn = sqlite3.connect('flask.sqlite')
        curs = conn.cursor()
        for row in curs.execute('select * from user'):
            print(row)
        res = request.args.get('get_value')
    elif request.method == 'POST':
        user_name = input('What is your name?')
        user_age = input('What is your age?')
        user_area = input('Where are you living?')
        user_number = 4
        conn = sqlite3.connect('flask.sqlite')
        curs = conn.cursor()
        curs.execute("insert into user values('user_number','user_name', 'user_age', 'user_area')")
        res = request.form['post_value']
    return res

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

