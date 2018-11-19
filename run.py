import os
from bottle import route, run, template, Bottle, redirect, request
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.orm import sessionmaker, Session
from User.user import User, UserAccount

engine = create_engine('mysql://root@localhost/lab3')

app = Bottle()
plugin = sqlalchemy.Plugin(engine, keyword='db')

app.install(plugin)
session = Session()

AvailableUser = 0
@app.get('/')
def home(db):
    if not AvailableUser :
        print(AvailableUser)
        return redirect('/login')
    else :
        return template('home')

@app.get('/login')
def otherLog():
    return template('login')

@app.get('/logout')
def otherLog():
    global AvailableUser
    AvailableUser = 0
    return redirect('/')

@app.post('/logining')
def createUser(db):
    table_data = db.query(User)
    results = []
    for user in table_data:
        global AvailableUser
        if user.name == request.forms.get('uname') and user.password == request.forms.get('psw'):
            AvailableUser = UserAccount(user.name, user.surname, "", user.money, user.bank)  
    return redirect('/')


app.run(host="127.0.0.1", port = 8000, debug=True, reloader=True)
