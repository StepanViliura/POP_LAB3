import os
from bottle import route, run, template, Bottle, redirect, request
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.orm import sessionmaker, Session
from User.user import User, UserAccount
from Transactions.transactions import Transaction
import datetime

engine = create_engine('mysql://root@localhost/lab3')

app = Bottle()
plugin = sqlalchemy.Plugin(engine, keyword='db')

app.install(plugin)
session = Session()


AvailableUser = 0
def checkLogIn():
    global AvailableUser
    if not AvailableUser:
        return redirect('/')

@app.get('/')
def home(db):
    if not AvailableUser :
        print(AvailableUser)
        return redirect('/login')
    else :
        return template('home', user = AvailableUser)

@app.get('/login')
def login():
    return template('login')

@app.get('/newUser')

def newUser():
    global AvailableUser
    if AvailableUser:
        return redirect('/')
    return template('createNewUser')

@app.post('/newUserCreating')
def newUserCreating(db):
    global AvailableUser
    new_user = User(name=request.forms.get('uname'),
                        surname=request.forms.get('usurname'),
                        bank=request.forms.get('ubank'),
                        money=request.forms.get('umoney'),
                        password=request.forms.get('psw'))
    
    db.add(new_user)
    db.flush()
    return redirect('/login')

@app.get('/logout')
def logout():
    global AvailableUser
    AvailableUser = 0
    return redirect('/')

@app.get('/oldTransactions/<name>/<surname>')
def getOldTransactions(name, surname, db):
    global AvailableUser
    checkLogIn()
    if not AvailableUser.CompareInitials(name, surname):
        return redirect('/')
    table_data = db.query(Transaction)
    results = []
    for transaction in table_data:
        if (transaction.sender_r.name == AvailableUser.first_name and transaction.sender_r.surname == AvailableUser.last_name) or (transaction.receiver_r.name == AvailableUser.first_name and transaction.receiver_r.surname == AvailableUser.last_name):
            results.append(transaction)
    
    return template('previousTransactions', transactions=results, user=AvailableUser)

@app.get('/createTransaction/<name>/<surname>')
def createTransaction(name, surname, db):
    global AvailableUser
    checkLogIn()
    table_data = db.query(User)
    results = []
    for user in table_data:
        if user.name != AvailableUser.first_name and user.surname != AvailableUser.last_name:
            results.append(user)
    return template('createTransaction', users=results, currentUser=AvailableUser)

@app.post('/logining')
def createUser(db):
    global AvailableUser
    table_data = db.query(User)
    results = []
    for user in table_data:
        if user.name == request.forms.get('uname') and user.password == request.forms.get('psw'):
            AvailableUser = UserAccount(user.name, user.surname, user.money, user.bank, db)  
    return redirect('/')

@app.post('/sendMoney')
def createUser(db):
    global AvailableUser
    money = int(request.forms.get('umoney'))
    sender_id = -1
    receiver_id = -1
    table_data = db.query(User)
    for user in table_data:
        if user.name == request.forms.get('uname') and user.surname == request.forms.get('usurname'):
            user.money+=money
            receiver_id = user.id
            db.flush()
        if user.name == AvailableUser.first_name and user.surname == AvailableUser.last_name:
            user.money-=money
            sender_id = user.id
            db.flush()
    new_trunsaction = Transaction(sender=sender_id,
                            receiver=receiver_id,
                            ammount=money,
                            transaction_date=datetime.datetime.now().strftime("%Y-%m-%d"))
    
    db.add(new_trunsaction)
    db.flush()
    return redirect('/')


app.run(host="127.0.0.1", port = 8000, debug=True, reloader=True)
