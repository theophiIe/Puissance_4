import Gestion_joueur
import Gestion_jeton
from Strategies import *
import math

def fin_de_partie(cls_grille, couleur):
    """
        Cette fonction permet de vérifier la potentielle fin de partie, s'il y a eu
        match nul ou un gagnant (en appelant les méthodes coup_gagnant et est_pleine de la classe Grille).

        Paramètre : 
            cls_grille : instance de la classe Grille
            
        Cette fonction renvoie un entier :
            2 si un coup gagnant est joué,
            1 si la grille est pleine,
            0 sinon.
    """

    if cls_grille.coup_gagnant(couleur) == True:
         return 2

    if cls_grille.est_pleine() == True:
        return 1

    return 0

def attribution_des_joueurs(qui_commence, mode_de_jeu, niveau_de_difficulte):
    """
        Cette fontion permet d'attribuer pour chaque joueur son rôle (joueur ou ordinateur),
        s'il commence ou non et dans le cas d'un ordinateur, sa difficulté.
        
        Paramètres :
            qui_commence : booléen correspondant à l'ordre de passage
            mode_de_jeu : booléen correspondant au mode de jeu choisi
            niveau_de_difficulte : entier correspondant au niveau de difficulté de l'ordinateur
                -1 pour Joueur vs Joueur,
                 0 pour le mode facile,
                 1 pour le mode moyen,
                 2 pour le mode difficile.

        Cette fonction renvoie deux instances de la classe Joueur / Ordinateur (joueur_actuel, joueur_suivant)
    """

    if mode_de_jeu == True:
        if qui_commence == True:
            joueur_actuel = Gestion_joueur.Joueur(True)
            joueur_suivant = Gestion_joueur.Joueur(False)

        else:
            joueur_actuel = Gestion_joueur.Joueur(False)
            joueur_suivant = Gestion_joueur.Joueur(True)

    else: 
        if qui_commence == True:
            joueur_actuel = Gestion_joueur.Joueur(True)
            joueur_suivant = Gestion_joueur.Ordinateur(False, niveau_de_difficulte)

        else: 
            joueur_actuel = Gestion_joueur.Ordinateur(True, niveau_de_difficulte)
            joueur_suivant = Gestion_joueur.Joueur(False)
    
    return joueur_actuel, joueur_suivant

def actions_coup_joueur(grille, num_colonne, joueur_actuel, joueur_suivant, niveau_de_difficulte):
    """
        Cette fonction permet de vérifier un coup, jouer un coup et modifie le joueur à qui c'est le tour de jouer.

        Paramètres : 
            grille : matrice de jeu
            num_colonne : entier correspondant au numéro de la colonne où le jeton a été placé sur la colonne
            joueur_actuel : instance de la classe Joueur correspondant au joueur qui joue actuellement
            joueur_suivant : instance de la classe Joueur correspondant au joueur qui doit jouer le coup au tour d'après
            niveau_de_difficulte : entier pour le niveau de difficulté de l'ordinateur, peut prendre 4 valeurs différentes (-1, 0, 1, 2)
            
        Renvoie :
            num_ligne : entier compris entre 0 et 6 correspondant au numéro de la ligne où le jeton a été joué
            num_colonne : entier compris entre 0 et 6 correspondant au numéro de la colonne où le jeton a été joué
            joueur_actuel : instance de la classe Joueur correspondant au joueur qui joue actuellement
            joueur_suivant : instance de la classe Joueur correspondant au joueur qui doit jouer le coup au tour d'après            
    """

    if type(joueur_actuel) == Gestion_joueur.Joueur: 
        num_ligne = joueur_actuel.jouer_coup(grille.grille, num_colonne)
        joueur_actuel, joueur_suivant = joueur_suivant, joueur_actuel

    else:
        coup_joue = False

        for num_colonne in range(grille.colonne):
            if grille.coup_valide(num_colonne) != True:
                continue

            else:
                num_ligne = joueur_actuel.jouer_coup(grille.grille, num_colonne)
            
                if grille.coup_gagnant((joueur_actuel.commence - 1) % 2 + 1):
                    coup_joue = True
                    joueur_actuel, joueur_suivant = joueur_suivant, joueur_actuel
                    break

                else:
                    Gestion_jeton.Jeton.decremente_nombre_jeton()
                    grille.grille[num_ligne][num_colonne] = None

        if coup_joue == False:
            for num_colonne in range(grille.colonne):
                if grille.coup_valide(num_colonne) != True:
                    continue
            
                else:
                    num_ligne = joueur_suivant.jouer_coup(grille.grille, num_colonne)
            
                    if grille.coup_gagnant((joueur_suivant.commence - 1) % 2 + 1):
                        coup_joue = True
                        Gestion_jeton.Jeton.decremente_nombre_jeton()
                        grille.grille[num_ligne][num_colonne] = None
                        num_ligne = joueur_actuel.jouer_coup(grille.grille, num_colonne)
                        joueur_actuel, joueur_suivant = joueur_suivant, joueur_actuel
                        break
                    
                    else:
                        Gestion_jeton.Jeton.decremente_nombre_jeton()
                        grille.grille[num_ligne][num_colonne] = None

        if coup_joue == False:
            num_colonne = fail_soft(grille, joueur_actuel, joueur_suivant, (2*niveau_de_difficulte) + 1, -math.inf, math.inf)[1]
            num_ligne = joueur_actuel.jouer_coup(grille.grille, num_colonne)
            joueur_actuel, joueur_suivant = joueur_suivant, joueur_actuel
    
    return num_ligne, num_colonne, joueur_actuel, joueur_suivant
    

