import sqlite3
import os
from flask import Flask, request, render_template, redirect

def ajout():
    con = sqlite3.connect('SdfTown.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM départements")
    result = cursor.fetchall()
    print(result)

app = Flask(__name__, template_folder=os.getcwd())
@app.route('/savedata', methods=['POST'])
def savedata():
    prénom = request.form.get('prenom')
    nom = request.form.get('nom')
    mdp = request.form.get('mdp')
    email = request.form.get('email')
    tel = request.form.get('tel')
    con = sqlite3.connect('SdfTown.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO clients (prénom, nom, mdp, email, tel) VALUES (?, ?, ?, ?, ?)", (prénom, nom, mdp, email, tel))
    con.commit()
    con.close()
    print(prénom, nom, mdp, email, tel)

if __name__ == "__main__":
    app.run(debug=True)