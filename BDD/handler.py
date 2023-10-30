from selection import *
from Insertion import *
import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__, template_folder=os.getcwd())

@app.route('/')
def index():
    return render_template('templates/home.html')

@app.route('/BDD/templates/login.html')
def login():
    return render_template('templates/login.html')

@app.route('/register.html')
def register():
    return render_template('templates/register.html')

@app.route('/produits.html')
def produits():
    liste_produits = select_produits() 
    return render_template('templates/produits.html', liste=liste_produits)

@app.route('/about.html')
def about():
    return render_template('templates/about.html')

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

@app.route('/connect',methods=['POST'])
def connect():
    mdp = request.form.get('mdp')
    email = request.form.get('email')
    result = select_client_email(email)
    if result[0][0] == mdp:
        liste_produits = select_produits()
        return (render_template('templates/produits.html',liste = liste_produits))
    else:
        return render_template('templates/home.html',message = 'votre identifiant ou mot de passe est incorrect')

if __name__ == "__main__":
    app.run(debug=True)