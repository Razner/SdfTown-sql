from selection import *
import sqlite3
import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__, template_folder=os.getcwd())

@app.route('/')
def index():
    return render_template('templates/home.html')

@app.route('/SignUp')
def SignUp():
    return render_template('templates/index.html')

@app.route('/savedata', methods=['POST'])
def savedata():
    prénom = request.form.get('prenom')
    nom = request.form.get('nom')
    mdp = request.form.get('mdp')
    email = request.form.get('email')
    tel = request.form.get('tel')
    con = sqlite3.connect(os.path.join(os.getcwd(), 'SdfTown.sqlite'))
    cursor = con.cursor()
    cursor.execute("INSERT INTO clients ('prénom', 'nom', 'mot de passe', 'email', 'téléphone') VALUES (?, ?, ?, ?, ?)", (prénom, nom, mdp, email, tel))
    con.commit()
    con.close()
    print(select_client())
    return render_template('templates/page2.html')

@app.route('/page2')
def page2():
    return (render_template('templates/page2.html'))

@app.route('/connect',methods=['POST'])
def connect():
    mdp = request.form.get('mdp')
    email = request.form.get('email')
    result = select_client_email(email)
    print(result)
    return render_template('templates/page2.html')
    
    

if __name__ == "__main__":
    app.run(debug=True)