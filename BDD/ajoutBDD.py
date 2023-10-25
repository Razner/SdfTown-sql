import sqlite3
import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__, template_folder=os.getcwd())

def ajout():
    con = sqlite3.connect(os.path.join(os.getcwd(), 'SdfTown.sqlite'))
    cursor = con.cursor()
    cursor.execute("SELECT * FROM départements")
    result = cursor.fetchall()
    con.close()
    return result

@app.route('/')
def index():
    return render_template('index.html')

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
    print(prénom, nom, mdp, email, tel)
    return "Données enregistrées"

if __name__ == "__main__":
    app.run(debug=True)