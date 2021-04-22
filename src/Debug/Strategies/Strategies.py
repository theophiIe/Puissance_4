import numpy
import math

from Puissance_4.src.Debug.Gestion_de_jeu.Gestion_grille import *
from Puissance_4.src.Debug.Gestion_de_jeu.Gestion_joueur import *
from Puissance_4.src.Debug.Gestion_de_jeu.Gestion_jeton import *
from Puissance_4.src.Debug.Gestion_de_jeu.Partie import *


def evaluation_quadruplet(quadruplet, couleur_jeton): 
    """
    Cette fonction permet d'évaluer le score d'un quadruplet de jetons donné en paramètre.
    Le score qui est retourné est calculé pour la couleur précisée en paramètre.
    
    Paramètres : 
        quadruplet : tableau de taille 4 contenant des instances Jetons de la classe Jeton
        couleur_jeton : booléen qui défini la couleur des jetons qui est à vérifier
    
    Renvoie : 
        un entier qui correspond au score qui est calculé par la fonction du quadruplet donné  
    """
    score = 0

    for incr in len(quadruplet):
        if quadruplet[incr] == couleur_jeton:
            score += 1   

        else:
            if quadruplet[incr] != couleur_jeton and quadruplet[incr] != None:
                  return 0
    
    if score == 1:
        return 1

    elif score == 2:
        return 10

    else:
        return 1000
  
  
def evaluation_coup(grille, num_ligne, num_colonne, couleur_jeton):
    """
      Cette fonction permet d'obtenir la somme des scores des quadruplés autour d'un coup donné.
      Elle fait appel à la fonction evaluation_quadruplet au dessus.
    
      Paramètre : 
        grille : la grille de jeu sur laquelle on fait les calculs
        num_ligne : entier correspondant au numéro de la ligne dans la grille
        num_colonne : entier correspondant au numéro de la colonne dans la grille
        couleur_jeton : booléen correspondant à la couleur du jeton

      Renvoie :
        elle retourne un entier correspondant au score du coup joué
    """
    score = 0
    
    # Horizontal
    for colonne in num_colonne:
        quadruplet = (grille.grille[num_ligne][colonne], grille.grille[num_ligne][colonne+1], grille.grille[num_ligne][colonne+2], grille.grille[num_ligne][colonne+3])
        score += evaluation_quadruplet(quadruplet, couleur_jeton)

    # Vertical
    for ligne in num_ligne:
        quadruplet = (grille.grille[ligne][num_colonne], grille.grille[ligne+1][num_colonne], grille.grille[ligne+2][num_colonne], grille.grille[ligne+3][num_colonne])
        score += evaluation_quadruplet(quadruplet, couleur_jeton)

    # Diagonal gauche
    for colonne in num_colonne and num_colonne < 7:
        for ligne in num_ligne and num_ligne + 3 < 6:
            quadruplet = (grille.grille[num_ligne][colonne], grille.grille[num_ligne][colonne+1], grille.grille[num_ligne][colonne+2], grille.grille[num_ligne][colonne+3])
            score += evaluation_quadruplet(quadruplet, couleur_jeton)

    # Diagonal droite
    for colonne in num_colonne and num_colonne < 7:
        for ligne in num_ligne and num_ligne - 3 >= 0:
            quadruplet = (grille.grille[num_ligne][colonne], grille.grille[num_ligne][colonne], grille.grille[num_ligne][colonne], grille.grille[num_ligne][colonne])
            score += evaluation_quadruplet(quadruplet, couleur_jeton)

    return score

  
  
def fail_soft(cls_grille, joueur_actuel, joueur_suivant, profondeur, alpha, beta):
  """
    Cette fonction permet de faire des calculs sur la grille en prévoyant les coups à l'avance, 
    et ainsi nous donner la colonne qui serait la plus optimale de jouer.
    
    cls_grille : instance de la classe Grille
    joueur_actuel : instance de la classe Joueur correspondant à celui qui joue le coup actuel
    joueur_suivant : instance de la classe Grille correspondant à celui qui jouera le coup suivant
    profondeur : entier correspondant à la profondeur de recherche à laquelle on s'arrête lors des calculs
    alpha : entier correspondant à la valeur minimale
    beta : entier correspondant à la valeur maximale
    
    Renvoie : 
      - un entier correspondant au meilleur score 
      - un entier correspondant au numéro de la colonne du meilleur coup
  """
  pass
  
  
  
  
  