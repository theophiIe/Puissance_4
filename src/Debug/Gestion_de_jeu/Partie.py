import Gestion_grille
import Gestion_joueur

def fin_de_partie(cls_grille):
    """
        Cette fonction permet de vérifier la potentielle fin de partie
        match nul ou un gagnant (en appelant les méthodes coup_gagnant et est_pleine de la classe Grille).

        Paramètre : 
            cls_grille : instance de la classe Grille
            
        Cette fonction renvoie un entier.
        2 si un coup gagnant est joué, 1 si la grille est pleine sinon 0.
    """
    pass

def attribution_des_joueurs(qui_commence, mode_de_jeu, niveau_de_difficulte):
    """
        Cette fontion permet d'attribuer pour chaque chaque joueur son rôle (joueur ou ordinateur),
        si il commence ou non et dans le cas d'un ordinateur, sa difficulté.
        Paramètre :
            qui_commence :
            mode_de_jeu :
            niveau_de_difficulte :

        Cette fonction renvoie deux joueurs (joueur_actuel, joueur_suivant)
    """
    pass

def valider_jouer_coup_joueur(grille, num_colonne, joueur_actuel, joueur_suivant, niveau_de_difficulte):
    """
        Cette fonction permet de : verifier_coup puis jouer_coup puis change l'ordre de passage des joueurs.
    """
    return num_ligne, num_colonne, joueur_actuel, joueur_suivant
