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
    calculDonne = ""
    calculPose = ""
    valeurs = []
    couleurs = "Rouge Rouge"
    couleursid = ""
    #resultat = eval(calculPose)
    conn = sqlite3.connect('testbdd.db')
    curs = conn.cursor()
    request = "Select nom, prenom From identification Where couleurs = ?;"
    insert = "Insert Into eleve (nom, prenom, calculDonne, calculPose, resultat) Values (?,?,?,?,?)"
    data = ("Rouge Rouge")
    #curs.execute("Select nom, prenom From eleve where couleurs = ?",(couleurs))
    val = curs.execute(request, data)
    print(val)

    if(couleursid == couleurs):
        nom = valeur[0]
        prenom = valeur[1]

    print(couleursid)

    conn.commit()
    curs.close()
    conn.close()


if __name__ == '__main__':
    main()
    # Fin
