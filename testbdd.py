# coding: UTF-8 
""" 
Script: test_capteur/testbdd
Création: admin, le 04/05/2021
"""


# Imports 
import sqlite3
# Fonctions 

# Programme principal 
def main():
    nom = "Pablo"
    prenom = "Emilio"
    calculDonne = "12/6"
    calculPose = "12/6"
    resultat = eval(calculPose)
    conn = sqlite3.connect('testbdd.db')
    curs = conn.cursor()

    insert = "Insert Into eleve (nom, prenom, calculDonne, calculPose, resultat) Values (?,?,?,?,?)"

    curs.execute("Insert Into eleve (nom, prenom, calculDonne, calculPose, resultat) Values (?,?,?,?,?)", (nom, prenom, calculDonne, calculPose, resultat))
    conn.commit()
    curs.close()
    conn.close()


if __name__ == '__main__':
    main()
    # Fin
