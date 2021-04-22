import Puissance_4/src/Sauvegarde_et_Chargement/Sauvegarde
import Puissance_4/src/Gestion_de_Jeu/Gestion_grille

def lecture_fichier(nom_fichier):
    """
        Cette fonction ouvre et lit le contenu du fichier passé en paramètre.
        Paramètre:
            nom_fichier : variable de type chaine de caractères correspondant
                            au nom du fichier.
        Cette fonction renvoie une chaine de caratère correspondant au contenu du fichier.
    """
    contenu_fichier = ""
    existence_fichier = verifie_existence_fichier(nom_fichier)
    if(existence_fichier):
        fichier = open(nom_fichier, "r")
        contenu_fichier = fichier.read()

    return contenu_fichier

def test_corruption(contenu_fichier):
    """ 
        Cette fonction lit la chaîne de caractères passée en paramètre
        et s'assure que le nombre de caractères dans la chaîne de caractères 
        ainsi que le type de caractères sont valides et interprétables.
        
        Paramètre:
            contenu_fichier : variable de type chaine de caractères correspondant
                            au contenu du fichier de sauvegarde.
        Cette fonction renvoie un booléen.
            True  : si le contenu du fichier est incorrect et inutilisable,
            False : si le contenu du fichier est correct et utilisable pour générer la partie.
    """
    if(len(contenu_fichier) != 42):
        return True

    for caractere in contenu_fichier:
        if((ord(caractere) < 48) or (ord(caractere) > 50)):
            return True

    return False

def chargement(nom_fichier):
    """
        Cette fonction recupère les données d'une partie précédement sauvegardée.
        Paramètre:
            nom_fichier : variable de type chaine de caractères correspondant
                            au nom du fichier.
        Cette fonction renvoie un booléen dans les deux cas, et renvoie aussi la chaîne de caractères 
        contenant le contenu du fichier lu dans le cas True.
            True et la chaîne de caractères  : si le chargement s'est passé correctement,
            False : si une erreur est survenue lors du chargement.
    """
    contenu_fichier = lecture_fichier(nom_fichier)
    if(contenu_fichier == ""):
        return False
    
    if(test_corruption(contenu_fichier)):
        return False

    return True, contenu_fichier
