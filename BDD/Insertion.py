import sqlite3
import os


def nouveau_client(prénom, nom, mdp, email, tel):
    con = sqlite3.connect(os.path.join(os.getcwd(), 'SdfTown.sqlite'))
    cursor = con.cursor()
    cursor.execute("INSERT INTO clients ('prénom', 'nom', 'mdp', 'email', 'téléphone') VALUES (?, ?, ?, ?, ?)", (prénom, nom, mdp, email, tel))
    con.commit()
    con.close()
    return True