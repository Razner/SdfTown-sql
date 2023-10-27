import sqlite3
import os

def select_client():
    con = sqlite3.connect(os.path.join(os.getcwd(), 'SdfTown.sqlite'))
    cursor = con.cursor()
    cursor.execute("SELECT * FROM clients")
    result = cursor.fetchall()
    con.close()
    return result

def select_client_email(email):
    con = sqlite3.connect(os.path.join(os.getcwd(), 'SdfTown.sqlite'))
    cursor = con.cursor()
    cursor.execute("SELECT mdp FROM clients WHERE email = ?",(email,) )
    result = cursor.fetchall()
    con.close()
    return result

def select_produits():
    liste_produit = []
    con = sqlite3.connect(os.path.join(os.getcwd(), 'SdfTown.sqlite'))
    cursor = con.cursor()
    cursor.execute("SELECT * FROM produits")
    result = cursor.fetchall()
    con.close()
    for i in result:
        produit = {"nom":i[1],"ville":i[2],"adresse":i[3],"prix":i[4]}
        liste_produit.append(produit)
    return liste_produit