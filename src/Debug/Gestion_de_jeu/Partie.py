import Gestion_grille
import Gestion_joueur
import math

def fin_de_partie(cls_grille,num_colonne):
    """
        Cette fonction permet de vérifier la potentielle fin de partie
        match nul ou un gagnant (en appelant les méthodes coup_gagnant et est_pleine de la classe Grille).

        Paramètre : 
            cls_grille : instance de la classe Grille
            
        Cette fonction renvoie un entier.
        2 si un coup gagnant est joué, 1 si la grille est pleine sinon 0.
    """
    if cls_grille.coup_gagnant(num_colonne) == True:
         return 2
    if cls_grille.est_pleine() == True:
        return 1
    return 0

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
    if mode_de_jeu == True:
        joueur_actuel=Gestion_joueur.Joueur(True)
        joueur_suivant=Gestion_joueur.Joueur(False)
    else: 
        if qui_commence == True:
            joueur_actuel=Gestion_joueur.Joueur(True)
            joueur_suivant=Gestion_joueur.Ordinateur(False,niveau_de_difficulte)
        else: 
            joueur_actuel=Gestion_joueur.Ordinateur(True,niveau_de_difficulte)
            joueur_suivant=Gestion_joueur.Joueur(False)
    
    return joueur_actuel,joueur_suivant

def actions_coup_joueur(grille, num_colonne, joueur_actuel, joueur_suivant, niveau_de_difficulte):
    """
        Cette fonction permet de vérifier un coup, jouer un coup et modifie le joueur à qui c'est le tour de jouer.
        Paramètre : 
            grille : matrice de jeu
            num_colonne : numéro de la colonne où le jeton a été placé sur la colonne
            joueur_actuel : instance de la classe Joueur correspondant au joueur qui joue actuellement
            joueur_suivant : instance de la classe Joueur correspondant au joueur qui doit jouer le coup au tour d'après
            niveau_de\_difficulte : entier pour le niveau de difficulté de l'ordinateur, peut prendre 4 valeurs différents (-1, 0, 1, 2)
            
        Renvoie :
            num_ligne : entier compris entre 0 et 6 du numéro de la ligne où le jeton a été placé sur la grille
            num_colonne : entier compris entre 0 et 6 du numéro de la colonne où le jeton a été placé sur la colonne
            joueur_actuel : instance de la classe Joueur correspondant au joueur qui joue actuellement
            joueur_suivant : instance de la classe Joueur correspondant au joueur qui doit jouer le coup au tour d'après            
    """
    if type(joueur_actuel) == Gestion_joueur.Joueur: 
        if grille.coup_valide(num_colonne) == True:
            num_ligne = joueur_actuel.jouer_coup(grille,num_colonne)
            joueur_actuel,joueur_suivant = joueur_suivant,joueur_actuel
        else:
            num_colonne = -1
            num_ligne = -1
    else: 
        "num_colonne = fail_soft(grille,joueur_actuel,joueur_suivant,4,-math.inf,math.inf)"
        num_ligne = joueur_actuel.jouer_coup(grille,num_colonne)
        joueur_actuel,joueur_suivant = joueur_suivant,joueur_actuel
    
    return num_ligne, num_colonne, joueur_actuel, joueur_suivant
    

