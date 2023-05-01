from flask import Flask, jsonify, render_template, request, redirect, session, abort, flash, send_file, session,url_for
from db import app,db
from models import User, Cliente, Discoteca
from passlib.apps import custom_app_context as pwd_context
from functools import wraps





def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            UserId = session['userid']
        except Exception as e:
            print(e)
            UserId = None
        
        if UserId is None :
            return redirect(url_for('login', next=request.url))
        else:
            return f(*args, **kwargs)
    return decorated_function


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
        passs="False"
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        try:
            passs = pwd_context.verify(password, user.password)
        except Exception as e:
            print(e)
        if passs == True:
            session['userid'] = user.id 
            session['firstname'] = user.firstname     
            session['role'] = user.role      
            
            return "Successfully"
        else:
            return "Incorrect email or password"    
    return render_template('login.html')



@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('index3.html')


@app.route('/logout')
def logout():
    session['userid']=None
    return redirect('/login')



def obtener_discotecas():
   discotecas = []
   try:
      consulta = Discoteca.query.all()
      print(consulta)
      
      for disco in consulta:
         id=disco.id
         nombre=disco.nombre
         lugar=disco.lugar
         aforo=disco.aforo
         desc=disco.descripcion
         discotecas.append({'id':id,'nombre':nombre,'lugar':lugar,'aforo':aforo,'descripcion':desc})
      # Cerramos el cursor y la conexión a la base de datos
     
   except ValueError as e:
      return -1
   return discotecas


@app.route('/discoteacachoices')
@login_required
def discotecachoices():
    discotecas = obtener_discotecas()
    return render_template('discotecachoices.html',discotecas=discotecas)



if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True,host="0.0.0.0",port=8080)






    

        