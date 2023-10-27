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