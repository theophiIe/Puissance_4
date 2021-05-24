from Sauvegarde import *
import Gestion_grille

def lecture_fichier(nom_fichier):
    contenu_fichier = ""
    if(verifie_existence_fichier(nom_fichier)):
        fichier = open(nom_fichier, "r")
        contenu_fichier = fichier.read()

    return contenu_fichier

def test_corruption(contenu_fichier):
    if(len(contenu_fichier) != 42):
        return True

    for caractere in contenu_fichier:
        if((ord(caractere) < 48) or (ord(caractere) > 50)):
            return True
        
    if nb_jeton_rouge > nb_jeton_jaune+1 or nb_jeton_jaune > nb_jeton_rouge+1:
        return True

    for i in range(35):
        if contenu_fichier[i] != '0' and contenu_fichier[i+7] == '0':
            return True

    return False

def chargement(nom_fichier):
    nom_fichier = "data/Liste_sauvegardes/" + nom_fichier
    contenu_fichier = lecture_fichier(nom_fichier)
    
    if(test_corruption(contenu_fichier)):
        return False
        
    grille = Gestion_grille.Grille(6,7)
    grille.remplir_grille(contenu_fichier)
    return True, grille
