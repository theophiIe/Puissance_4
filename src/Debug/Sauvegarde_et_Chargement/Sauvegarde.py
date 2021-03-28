import os
import time

def information_sauvegarde():
    """
        Cette fonction permet de récuperer le nom
        des fichiers correspondant aux sauvegardes
        des parties.

        Cette fonction renvoie un tableau contenant les 
        noms des fichiers de sauvegardes sous forme de 
        chaines de caractères.
    """
    pass

def verification_syntaxe_nom_fichier(nom_fichier):
    """
        Cette fonction permet de vérifier que le nom
        choisi pour le fichier de sauvegarde est syntaxiquement
        correcte.

        Paramètre:
            nom_fichier : variable de type chaine de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie un booléen :
            True  : si la syntaxe est correcte.
            False : si la syntaxe est incorrecte.
    """
    pass

def verifie_existance_fichier(nom_fichier):
    """
        Cette fonction permet de vérifier si le fichier 
        ayant pour nom le nom donné en argument existe déjà.

        Paramètre:
            nom_fichier : variable de type chaine de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie un booléen :
            True  : si la syntaxe est correcte.
            False : si la syntaxe est incorrecte.
    """
    pass

def supprimer_sauvegarde(nom_fichier):
    """
        Cette fonction permet de supprimer un fichier
        de sauvegarde qui a pour nom celui donné en argument.

        Paramètre:
            nom_fichier : variable de type chaine de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie un booléen :
            True  : si la suppression a été correctement effectué.
            False : si la suppression a rencontré un problème.
    """
    pass

def sauvegarde(grille, nom_fichier):
    """
        Cette fonction permet, à partir des informations de la grille passé en paramètre,
        de sauvegarder cette dernière dans un fichier texte qui à pour nom celui passé en paramètre,
        s'il n'existe pas déjà.

        Paramètres:
            grille : matrice de la classe Grilles.
            nom_fichier : variable de type chaine de caractères correspondant
                            au nom du fichier.

        Cette fonction renvoie un booléen :
            True  : si la sauvegarde a été correctement effectué.
            False : si la sauvegarde a rencontré un problème.
    """
    pass