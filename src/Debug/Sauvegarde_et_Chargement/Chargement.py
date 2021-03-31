def lecture_fichier(nom_fichier):
    """
        Cette fonction ouvre et lit le contenu du fichier passé en paramètre.

        Paramètre:
            nom_fichier : variable de type chaine de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie une chaine de caratère correspondant au contenu du fichier.
    """
    pass

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
    pass

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
    pass
