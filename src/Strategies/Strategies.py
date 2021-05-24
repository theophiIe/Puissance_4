import math

import Gestion_jeton
from Partie import *

def evaluation_quadruplet(quadruplet, couleur_jeton): 
    """
        Cette fonction permet d'évaluer un quadruplet donnée en paramètre
        par rapport à une couleur de jeton également passé en paramètre.

        Paramètres :
            quadruplet : tableau contenant soit None soit une couleur de jeton
            couleur_jeton : couleur d'un jeton
                1 : rouge
                2 : jaune

        Renvoie :
            un entier correspondant au score d'un quadruplet

    """

    nb_vide = 0
    nb_jeton = 0
    nb_jeton_adv = 0

    for incr in range(len(quadruplet)):
        if quadruplet[incr] is None:
            nb_vide += 1

        else:
            if quadruplet[incr] is not None and quadruplet[incr].couleur == couleur_jeton:
                nb_jeton += 1

            elif quadruplet[incr] is not None and quadruplet[incr].couleur != couleur_jeton :
                nb_jeton_adv += 1

    if nb_jeton == 0 and nb_jeton_adv == 0:
        return 0

    if nb_jeton > 0:
        # CAS 0
        if nb_jeton == 1 and nb_jeton_adv == 0:  
            return 2

        elif nb_jeton == 1 and nb_jeton_adv == 1:  
            return 1

        elif nb_jeton == 1 and nb_jeton_adv == 2:  
            return 1

        elif nb_jeton == 1 and nb_jeton_adv == 3:  
            return -8

        # CAS 1
        elif nb_jeton == 2 and nb_jeton_adv == 0:  
            return 6

        elif nb_jeton == 2 and nb_jeton_adv == 1:  
            return 4

        elif nb_jeton == 2 and nb_jeton_adv == 2:  
            return -10

        # CAS 2
        elif nb_jeton == 3 and nb_jeton_adv == 0:
            return 45
        
        elif nb_jeton == 3 and nb_jeton_adv == 1:
            return -15

        # CAS 3
        elif nb_jeton == 4:
            return 500000000000000

    else:
        if nb_jeton_adv == 1 and nb_jeton == 0:
            return -3

        elif nb_jeton_adv == 2 and nb_jeton == 0:
            if Gestion_jeton.Jeton.nombre_jeton % 2 == 1:
                return -20

            else:
                return -10

        elif nb_jeton_adv == 3 and nb_jeton == 0:
            return -35
        
        elif nb_jeton_adv == 3 and nb_jeton == 1: 
            return 0

    return 0
    
def evaluation_coup(cls_grille, couleur_jeton):
    """
        Cette fonction permet d'obetnir la somme des scores des quadruplés 
        possibles dans la grille.

        Paramètres :
            cls_grille : instance de la clase Grille
            couleur_jeton : entier qui définit la couleur des jetons
        
        Renvoie :
            un entier correspondant au score d'un quadruplet.
    """

    score = 0
    jeton = 0

    for ligne in range(cls_grille.ligne):
        jeton_centre = cls_grille.grille[ligne][3]
        
        if jeton_centre is not None and jeton_centre.couleur == couleur_jeton:
            jeton += 1

    score += jeton*15

    for ligne in range(cls_grille.ligne):
        for colonne in range(cls_grille.colonne-3):
            quadruplet = (cls_grille.grille[ligne][colonne], cls_grille.grille[ligne][colonne+1], 
                          cls_grille.grille[ligne][colonne+2], cls_grille.grille[ligne][colonne+3])

            score += evaluation_quadruplet(quadruplet, couleur_jeton)

    for ligne in range(cls_grille.ligne-3):
        for colonne in range(cls_grille.colonne):
            quadruplet = (cls_grille.grille[ligne][colonne], cls_grille.grille[ligne+1][colonne],
                          cls_grille.grille[ligne+2][colonne], cls_grille.grille[ligne+3][colonne])

            score += evaluation_quadruplet(quadruplet, couleur_jeton)

    for ligne in range(cls_grille.ligne-3):
        for colonne in range(cls_grille.colonne-3):
            quadruplet = (cls_grille.grille[ligne][colonne], cls_grille.grille[ligne+1][colonne+1],
                          cls_grille.grille[ligne+2][colonne+2], cls_grille.grille[ligne+3][colonne+3])

            score += evaluation_quadruplet(quadruplet, couleur_jeton)

    for ligne in range(3,cls_grille.ligne):
        for colonne in range(cls_grille.colonne-3):
            quadruplet = (cls_grille.grille[ligne][colonne], cls_grille.grille[ligne-1][colonne+1],
                          cls_grille.grille[ligne-2][colonne+2], cls_grille.grille[ligne-3][colonne+3])

            score += evaluation_quadruplet(quadruplet, couleur_jeton)

    return score

def fail_soft(cls_grille, joueur_actuel, joueur_suivant, profondeur, alpha, beta):
    """
        Cette fonction permet de faire des calculs sur la grille en prévoyant les coups à l'avance, 
        et ainsi nous donner la colonne qui serait la plus optimale de jouer.

        Paramètres :
            cls_grille : instance de la classe Grille
            joueur_actuel : instance de la classe Joueur ou Ordinateur
            joueur_suivant : instance de la classe Joueur ou Ordinateur
            profondeur : entier correspondant à la profondeur de l'arbre
            alpha : entier correspondant à la borne supérieure
            beta : entier correspondant à la borne inférieure

        Renvoie : 
            un score sous forme d'entier
            un numéro de colonne de type entier
    """

    fin_partie = (cls_grille.est_pleine() or cls_grille.coup_gagnant(1) or cls_grille.coup_gagnant(2))

    if profondeur == 0 or fin_partie:
        if fin_partie:
            if cls_grille.coup_gagnant((joueur_actuel.commence-1)%2 + 1):
                return (-500000000000000, None)

            elif cls_grille.coup_gagnant((joueur_suivant.commence-1)%2 + 1):
                return (50000000000000, None)

            else:
                return (0, None)

        else:
            return (-(2*evaluation_coup(cls_grille, (joueur_actuel.commence-1)%2 + 1)-3*evaluation_coup(cls_grille, (joueur_suivant.commence-1)%2 + 1)), None)

    courant = -math.inf
    meilleur_coup = 0

    for colonne in range(cls_grille.colonne):
        if cls_grille.coup_valide(colonne) == False:
            continue

        if profondeur%2 == 1:
            ligne = joueur_actuel.jouer_coup(cls_grille.grille, colonne)

        else:
            ligne = joueur_suivant.jouer_coup(cls_grille.grille, colonne)

        score = -fail_soft(cls_grille, joueur_actuel, joueur_suivant, profondeur-1, -beta, -alpha)[0]

        Gestion_jeton.Jeton.decremente_nombre_jeton()
        cls_grille.grille[ligne][colonne] = None

        if score > courant:
            courant = score
            meilleur_coup = colonne

        alpha = max(alpha, courant)

        if alpha >= beta:
            break

    return courant, meilleur_coup