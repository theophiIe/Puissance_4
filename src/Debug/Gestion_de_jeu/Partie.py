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
            qui_commence : booléen correspondant à l'ordre de passage
            mode_de_jeu : booléen correspondant au mode de jeu choisi
            niveau_de_difficulte : entier correspondant au niveau de difficulté de l'ordinateur
            (-1, 0, 1, 2 pour Joueur vs Joueur / facile / intermédiaire / difficile)

        Cette fonction renvoie deux joueurs (joueur_actuel, joueur_suivant)
    """
    pass

def valider_jouer_coup_joueur(grille, num_colonne, joueur_actuel, joueur_suivant, niveau_de_difficulte):
    """
        Cette fonction permet de vérifier un coup, jouer un coup et modifie le joueur à qui c'est le tour de jouer.
        Paramètre : 
            grille : matrice de jeu
            num_colonne : numéro de la colonne où le jeton a été placé sur la colonne
            joueur_actuel : booléen correspondant au joueur qui joue actuellement
            joueur_suivant : booléen correspondant au joueur qui doit jouer le coup au tour d'après
            niveau_de\_difficulte : entier pour le niveau de difficulté de l'ordinateur, peut prendre 4 valeurs différents (-1, 0, 1, 2)
            
        Renvoie :
            num_ligne : entier compris entre 0 et 6 du numéro de la ligne où le jeton a été placé sur la grille
            num_colonne : entier compris entre 0 et 6 du numéro de la colonne où le jeton a été placé sur la colonne
            joueur_actuel : booléen correspondant au joueur qui joue actuellement
            joueur_suivant : booléen correspondant au joueur qui doit jouer le coup au tour d'après            
    """
    
    return num_ligne, num_colonne, joueur_actuel, joueur_suivant
