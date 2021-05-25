from Sauvegarde import *
import Gestion_grille

def lecture_fichier(nom_fichier):
    """
        Cette fonction va stocker le contenu du fichier passé en paramètre
        dans une chaîne de caractères.

        Paramètre :
            nom_fichier : chaîne de caractères

        Renvoie :
            une chaîne de caractères avec le contenu du fichier 
    """

    contenu_fichier = ""

    if(verifie_existence_fichier(nom_fichier)):
        fichier = open(nom_fichier, "r")
        contenu_fichier = fichier.read()

    return contenu_fichier

def test_corruption(contenu_fichier):
    """
        Cette fonction vérifie si la chaîne de caractères
        passée en paramètre est corrompue ou non. 
        On vérifie si le nombre de caractères correspond à la taille de la grille (42).
        On vérifie si chaque caractère de la chaîne de caractères correspond '0', '1', ou '2'.
        On regarde si les caractères correspondants à un jeton de la même couleur 
        correspond à une partie valide.
        On vérifie si les caractères correspondants à un jeton donne une position 
        valide dans la grille.

        Paramètre :
            contenu_fichier : chaîne de caractères contenant les positions des jetons dans la grille.

        Renvoie :
            un booléen
                True : si la chaîne de caractères est corrompu,
                False : si la chaîne de caractères est valide.
    """

    if(len(contenu_fichier) != 42):
        return True

    nb_jeton_rouge = 0
    nb_jeton_jaune = 0

    for caractere in contenu_fichier:
        if((ord(caractere) < 48) or (ord(caractere) > 50)):
            return True

        else:
            if caractere == '1':
                nb_jeton_rouge += 1
                
            elif caractere == '2':
                nb_jeton_jaune += 1
        
    if nb_jeton_rouge > nb_jeton_jaune+1 or nb_jeton_jaune > nb_jeton_rouge+1 or (nb_jeton_jaune == 21 and nb_jeton_rouge == 21):
        return True

    for i in range(35):
        if contenu_fichier[i] != '0' and contenu_fichier[i+7] == '0':
            return True

    return False

def chargement(nom_fichier):
    """
        Cette fonction permet de remplir la grille à partir du 
        contenu d'un fichier passé en paramètre préalablement.

        Paramètre :
            nom_fichier : chaîne de caractères faisant référence au nom d'un fichier.

        Renvoie :
            un booléen
                True : si le chargement c'est bien effectué
                False : si le chargement a échoué
            grille : renvoie la grille de jeu
    """

    nom_fichier = "data/Liste_sauvegardes/" + nom_fichier
    contenu_fichier = lecture_fichier(nom_fichier)
    
    if(test_corruption(contenu_fichier)):
        return False
        
    grille = Gestion_grille.Grille(6, 7)
    grille.remplir_grille(contenu_fichier)

    return True, grille
