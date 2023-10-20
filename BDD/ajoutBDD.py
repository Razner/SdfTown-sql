import sqlite3

def ajout():
    con = sqlite3.connect('SdfTown.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM départements")
    result = cursor.fetchall()
    print(result)

ajout()