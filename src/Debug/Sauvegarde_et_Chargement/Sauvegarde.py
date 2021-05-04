import os
import glob
import time
import Puissance_4/src/Debug/Gestion_de_jeu/Gestion_grille

def information_sauvegarde():
    """
        Cette fonction permet de récupérer le nom
        des fichiers correspondant aux sauvegardes
        des parties.

        Cette fonction renvoie un tableau contenant les 
        noms des fichiers de sauvegarde sous forme de 
        chaînes de caractères.
    """

    sauvegardes = glob.glob('*.txt')
    derniere_date_modification = []
    date_creation = []

    for x in sauvegardes:
        derniere_date_modification.append(time.ctime(os.path.getmtime(x)))
        date_creation.append(time.ctime(os.path.getctime(x)))

    return sauvegardes, derniere_date_modification, date_creation
    pass

def verification_syntaxe_nom_fichier(nom_fichier):
    """
        Cette fonction permet de vérifier que le nom
        choisi pour le fichier de sauvegarde est syntaxiquement
        correct.

        Paramètre:
            nom_fichier : variable de type chaine de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie un booléen :
            True  : si la syntaxe est correcte.
            False : si la syntaxe est incorrecte.
    """
    char_interdits = "/:\"?|<>*\\"

    for x in range (len(char_interdits)):
        if char_interdits[x] in nom_fichier:
            return False
    return True
    pass

def verifie_existance_fichier(nom_fichier):
    """
        Cette fonction permet de vérifier si le fichier 
        ayant pour nom le nom donné en argument existe déjà.

        Paramètre:
            nom_fichier : variable de type chaîne de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie un booléen :
            True  : si le nom de fichier est indisponible.
            False : si le nom de fichier est disponible.
    """

    if os.path.exists(nom_fichier):
        return True
    return False
    pass

def supprimer_sauvegarde(nom_fichier):
    """
        Cette fonction permet de supprimer un fichier
        de sauvegarde qui a pour nom celui donné en argument.

        Paramètre:
            nom_fichier : variable de type chaîne de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie un booléen :
            True  : si la suppression a été correctement effectuée.
            False : si la suppression a rencontré un problème.
    """

    if verifie_existance_fichier(nom_fichier):
        os.remove(nom_fichier)
        if verifie_existance_fichier(nom_fichier):
            return False
        else:
            return True
    else:
        print("The file does not exist")
        return False
    pass

def sauvegarde(grille, nom_fichier):
    """
        Cette fonction permet, à partir des informations de la grille passée en paramètre,
        de sauvegarder cette dernière dans un fichier texte qui a pour nom celui passé en paramètre,
        s'il n'existe pas déjà.

        Paramètres:
            grille : matrice de la classe Grille.
            nom_fichier : variable de type chaîne de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie un booléen :
            True  : si la sauvegarde a été correctement effectuée.
            False : si la sauvegarde a rencontré un problème.
    """
    f = open(nom_fichier, "w")

    for x in grille:
        if x != 0 and x != 1 and x != 2:
            return False
        f.write(x)
        f.write(", ")
    f.close()
    pass
