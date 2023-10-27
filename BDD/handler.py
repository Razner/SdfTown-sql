from selection import *
from Insertion import *
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
    nouveau_client(prénom,nom,mdp,email,tel)
    liste_produits = select_produits()
    return render_template('templates/page2.html',liste = liste_produits)

@app.route('/page2')
def page2():
    liste_produits = select_produits()
    return (render_template('templates/page2.html',liste = liste_produits))

@app.route('/connect',methods=['POST'])
def connect():
    mdp = request.form.get('mdp')
    email = request.form.get('email')
    result = select_client_email(email)
    if result[0][0] == mdp:
        liste_produits = select_produits()
        return (render_template('templates/page2.html',liste = liste_produits))
    else:
        return render_template('templates/home.html',message = 'votre identifiant ou mot de passe est incorrect')
    
    

if __name__ == "__main__":
    app.run(debug=True)