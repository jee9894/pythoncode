import pymysql, os
from flask import Flask, request, render_template, url_for, redirect, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def formTest():
    return render_template('form.html')

@app.route('/usersform', methods=['POST', 'GET'])
def userform():
    if request.method == 'GET':
        return render_template('usersform.html')
    else:
        userid = request.form['userid']
        userpw = request.form['userpw']
        username = request.form['username']
        userage = request.form['userage']
        useremail = request.form['useremail']
        useradd = request.form['useradd']
        usergender = request.form['usergender']
        usertel = request.form['usertel']

        try:
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='qwer1234',
                                         db='test',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

            with connection.cursor() as cursor:
                sql = '''
                    insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)
                '''
                data = (userid,userpw,username,userage,useremail,useradd,usergender,usertel)
                cursor.execute(sql,data)
                connection.commit()
        finally:
            connection.close()

    return redirect('/list')

@app.route('/list')
def list():
    connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = '''
                select * from users
            '''
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    
    return render_template('list.html', list = result)

@app.route('/content/<userid>')
def content(userid):
    connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = '''
                select * from users where userid = %s
            '''
            cursor.execute(sql, userid)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()
    
    return render_template('content.html', list = result)

@app.route('/updateform/<userid>', methods = ['GET'])
def updateformget(userid):
    connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = '''
                select * from users where userid = %s
            '''
            cursor.execute(sql, userid)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()
    
    return render_template('updateform.html', list = result)

@app.route('/updateform', methods = ['POST'])
def updateformpost():
    connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
    
    userid = request.form['userid']
    userpw = request.form['userpw']
    username = request.form['username']
    userage = request.form['userage']
    useremail = request.form['useremail']
    useradd = request.form['useradd']
    usergender = request.form['usergender']
    usertel = request.form['usertel']

    try:
        with connection.cursor() as cursor:
            sql = '''
                update users set
                userpw = %s,
                username = %s,
                userage = %s,
                usermail = %s,
                useradd = %s,
                usergender = %s,
                usertel = %s
                where userid = %s
            '''
            data = (userpw,username,userage,useremail,useradd,usergender,usertel,userid,)
            cursor.execute(sql, data)
            connection.commit()
    finally:
        connection.close()
    
    return redirect('/list')

@app.route('/deleteform/<userid>')
def deleteformget(userid):
    connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = '''
                DELETE FROM users WHERE userid = %s;
            '''
            cursor.execute(sql, userid)
            connection.commit()
    finally:
        connection.close()
    
    return redirect('/list')

@app.route('/ajaxlist', methods = ['GET'])
def ajaxlistget():
    connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = '''
                select * from users
            '''
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    
    return render_template('/ajaxlist.html', list = result)

@app.route('/ajaxlist', methods = ['POST'])
def ajaxlistpost():
    connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

    userid = request.form.get('userid')

    try:
        with connection.cursor() as cursor:
            sql = '''
                select * from users where userid like %s
            '''
            userid = "%" + userid + "%"
            cursor.execute(sql, userid)
            result = cursor.fetchall()
            print("커서 패치all 타입 :", type(result))
    finally:
        connection.close()
    
    return jsonify(result)

@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname = os.path.dirname(__file__) + "/static/img/"
    filenames = os.listdir(dirname)
    print(filenames)
    return render_template('imglist.html', filenames = filenames)

if __name__ == '__main__':
    app.run(debug=True)
