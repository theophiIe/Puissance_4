import Gestion_grille
import Gestion_joueur

def fin_de_partie():
    """
        Cette fonction permet de vérifier la potentielle fin de partie
        match nul ou un gagnant (en appelant les méthodes coup_gagnant et est_pleine de la classe Grille).

        Cette fonction renvoie un entier.
        2 si un coup gagnant est joué, 1 si la grille est pleine sinon 0.
    """
    pass

def initialiser_partie(mode_de_jeu, difficulte_ordi = -1):
    """
        Cette fonction fait appel au constructeur de la classe :    Grille
                                                                    Joueur
                                                                    Ordinateur (si un mode de jeu avec un ordinateur est selectionné).

        Paramètre :
            mode_de_jeu : entier pouvant être 0, 1 ou 2
            difficulte_ordi : paramètre optionel, on l'utilise uniquement si on est dans un mode jeu avec un ordinateur

        Cette fonction ne renvoie rien
    """
    pass
