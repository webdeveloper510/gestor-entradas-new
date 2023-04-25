import secrets
from flask import Flask, jsonify, render_template, request, redirect, session, abort, flash, send_file
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    # discotecas = obtener_discotecas()
    return render_template('index1.html')
    #  discotecas=discotecas

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)




    

        