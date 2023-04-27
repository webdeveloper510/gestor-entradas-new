from flask import Flask, jsonify, render_template, request, redirect, session, abort, flash, send_file, session
from db import app,db
from models import User, Cliente
from passlib.apps import custom_app_context as pwd_context



@app.route('/')
def index():
    # discotecas = obtener_discotecas()
    return render_template('index1.html')
    #  discotecas=discotecas



@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        password = request.form['password']
        conpassword = request.form['conpassword']
        email = request.form['email']
        role = request.form['owners']

        user = User.query.filter_by(email=email).first()
        if user is None:
            if password == conpassword :
                password_hash = pwd_context.encrypt(password)
                user = User(firstname=firstname,lastname=lastname,password=password_hash,email=email,role=role)
                db.session.add(user)
                db.session.commit()
                return "User registered successfully"
            else:
                return "Your password and confirmation password do not match."
        else:
            return "Your email is already exists"
    return render_template('signup.html')



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        passs = pwd_context.verify(password, user.password)
        if passs == True:
            print(user.id)
            session['userid'] = user.id 
            print("session id", session.get('userid'))
            return redirect('/dashboard')
            
        
    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
   return render_template('index3.html')



if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True,host="0.0.0.0",port=8080)






    

        