import math
import Gestion_jeton
from Partie import *


def evaluation_quadruplet(quadruplet, couleur_jeton): 
    nb_jeton = 0
    nb_jeton_adv = 0

    for incr in range(len(quadruplet)):
        if quadruplet[incr] is not None and quadruplet[incr].couleur == couleur_jeton:
            nb_jeton += 1

        elif quadruplet[incr] is not None and quadruplet[incr].couleur != couleur_jeton :
            nb_jeton_adv += 1
    
    if nb_jeton > 0 and nb_jeton_adv > 0:
        return 0

    if nb_jeton > 0:
        if nb_jeton == 2:
            return 10
        
        elif nb_jeton == 3:
            return 25
        
        elif nb_jeton == 4:
            return 500
    else:
        if nb_jeton_adv == 3:
            return -20

    return 0

def evaluation_coup(cls_grille, couleur_jeton):
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

def fail_soft(cls_grille, profondeur, alpha, beta, joueur_actuel, joueur_suivant):
    fin_partie = (cls_grille.est_pleine() or cls_grille.coup_gagnant(1) or cls_grille.coup_gagnant(2))
    if profondeur == 0 or fin_partie:
        if fin_partie:
            if cls_grille.coup_gagnant((joueur_actuel.commence-1)%2 + 1):
                return (50000, None)
            
            elif cls_grille.coup_gagnant((joueur_suivant.commence-1)%2 + 1):
                return (-5000, None)
            
            else:
                return (0, None)
        
        else:
            return (-evaluation_coup(cls_grille, (joueur_actuel.commence-1)%2 + 1), None)

    courant = -math.inf
    meilleur_coup = 0

    for colonne in range(cls_grille.colonne):
        if cls_grille.coup_valide(colonne) == False:
            continue

        if profondeur%2 == 1:
            ligne = joueur_actuel.jouer_coup(cls_grille.grille, colonne)
        
        else:
            ligne = joueur_suivant.jouer_coup(cls_grille.grille, colonne)

        score = -fail_soft(cls_grille, profondeur-1, -beta, -alpha, joueur_actuel, joueur_suivant)[0]

        Gestion_jeton.Jeton.decremente_nombre_jeton()
        cls_grille.grille[ligne][colonne] = None
        
        if score > courant:
            courant = score
            meilleur_coup = colonne
        
        alpha = max(alpha, courant)
        
        if alpha >= beta:
            break

    return courant, meilleur_coup