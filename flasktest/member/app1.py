import pymysql
import os
import cx_Oracle
import json
from flask import Flask, request, render_template, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://HR:HR@localhost:1521/xe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwer1234@localhost/test'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    userid = db.Column(db.String(20), primary_key=True)
    userpw = db.Column(db.String(20))
    username = db.Column(db.String(20))
    userage = db.Column(db.Integer)
    usermail = db.Column(db.String(20))
    useradd = db.Column(db.String(20))
    usergender = db.Column(db.String(20))
    usertel = db.Column(db.String(20))

    def __repr__(self):
        return '<userid : %r, userpw : %r, username : %r, userage : %r, usermail : %r, useradd : %r, usergender : %r, usertel : %r>' % (self.userid, self.userpw, self.username, self.userage, self.usermail, self.useradd, self.usergender, self.usertel)

    def __init__(self, userid, userpw, username, userage, useremail, useradd, usergender, usertel):
        self.userid = userid
        self.userpw = userpw
        self.username = username
        self.userage = userage
        self.usermail = useremail
        self.useradd = useradd
        self.usergender = usergender
        self.usertel = usertel
    
    def serialize(self):
        return {
            'userid':self.userid,
            'userpw': self.userpw,
            'username': self.username,
            'userage':self.userage,
            'usermail':self.usermail,
            'useradd':self.useradd,
            'usergender':self.usergender,
            'usertel':self.usertel
        }

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


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

        my_user = User(userid, userpw, username, userage, useremail, useradd, usergender, usertel)
        db.session.add(my_user)
        db.session.commit()

    return redirect('/list')


@app.route('/list')
def list():
    all_data = User.query.all()
    return render_template('list.html', list=all_data)


@app.route('/content/<userid>')
def content(userid):
    result = User.query.filter_by(userid = userid).one()
    return render_template('content.html', list=result)


@app.route('/updateform/<userid>', methods=['GET'])
def updateformget(userid):
    result = User.query.filter_by(userid = userid).one()
    return render_template('updateform.html', list=result)


@app.route('/updateform', methods=['POST'])
def updateformpost():
    my_user = User.query.get(request.form.get('userid'))

    my_user.userid = request.form['userid']
    my_user.userpw = request.form['userpw']
    my_user.username = request.form['username']
    my_user.userage = request.form['userage']
    my_user.useremail = request.form['useremail']
    my_user.useradd = request.form['useradd']
    my_user.usergender = request.form['usergender']
    my_user.usertel = request.form['usertel']

    db.session.commit()

    return redirect('/list')


@app.route('/deleteform/<userid>')
def deleteformget(userid):
    data = User.query.get(userid)
    db.session.delete(data)
    db.session.commit()
    return redirect('/list')


@app.route('/ajaxlist', methods=['GET'])
def ajaxlistget():
    all_data = User.query.all()
    return render_template('/ajaxlist.html', list=all_data)


@app.route('/ajaxlist', methods=['POST'])
def ajaxlistpost():
    userid = request.form.get('userid')
    result = User.query.filter(User.userid.like('%'+userid+'%')).all()
    print("쿼리 all 타입 :", type(result))
    print(result)
    print([i.serialize() for i in result])
    return jsonify([i.serialize() for i in result])


@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname = os.path.dirname(__file__) + "/static/img/"
    filenames = os.listdir(dirname)
    print(filenames)
    return render_template('imglist.html', filenames=filenames)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
