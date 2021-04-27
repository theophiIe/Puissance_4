import numpy as ny
import math
import sys
#sys.path.append('/home/t/Documents/Cours/Puissance_4/Puissance_4/src/Debug/Gestion_de_jeu')
#print(sys.path)

sys.path.append('../Gestion_de_jeu')

from Gestion_grille import *
from Gestion_joueur import *
from Gestion_jeton import *
from Partie import *


"""
import Puissance_4.src.Debug.Gestion_de_jeu.Gestion_grille
import Puissance_4.src.Debug.Gestion_de_jeu.Gestion_joueur
import Puissance_4.src.Debug.Gestion_de_jeu.Gestion_jeton
import Puissance_4.src.Debug.Gestion_de_jeu.Partie
"""


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

    for incr in range(len(quadruplet)):
        if quadruplet[incr] != None and quadruplet[incr].couleur == couleur_jeton:
            score += 1   

        else:
            if quadruplet[incr] != None and quadruplet[incr].couleur != couleur_jeton :
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
    
    for ligne, colonne in zip(range(num_ligne-3, num_ligne+1), range(num_colonne-3, num_colonne+1)):
        if colonne >= 0 and colonne + 3 <= 6:
            quadruplet = (grille.grille[num_ligne][colonne], grille.grille[num_ligne][colonne+1], grille.grille[num_ligne][colonne+2], grille.grille[num_ligne][colonne+3])
            score += evaluation_quadruplet(quadruplet, couleur_jeton)

        if ligne >= 0 and ligne + 3 <= 5:
            quadruplet = (grille.grille[ligne][num_colonne], grille.grille[ligne+1][num_colonne], grille.grille[ligne+2][num_colonne], grille.grille[ligne+3][num_colonne])
            score += evaluation_quadruplet(quadruplet, couleur_jeton)

        if (ligne >= 0 and ligne + 3 <= 5) and (colonne >= 0 and colonne + 3 <= 6):
            quadruplet = (grille.grille[ligne][colonne], grille.grille[ligne+1][colonne+1], grille.grille[ligne+2][colonne+2], grille.grille[ligne+3][colonne+3])
            score += evaluation_quadruplet(quadruplet, couleur_jeton)

        ligne_inverse = num_ligne - (ligne - num_ligne)
        if (ligne_inverse >= 0 and ligne_inverse + 3 <= 5) and (colonne >= 0 and colonne + 3 <= 6):
            quadruplet = (grille.grille[ligne_inverse][colonne], grille.grille[ligne_inverse+1][colonne+1], grille.grille[ligne_inverse+2][colonne+2], grille.grille[ligne_inverse+3][colonne+3])
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
    # modifier la fonction fin de partie pour qu'elle verifie toute la grille
  # et pas que la zone autour du dernier coup joué
  
  if fin_de_partie(cls_grille, 0) != 0:
    return 1000 #score_victoire
  else :
    if(profondeur <= 0):
      return evaluation_coup(cls_grille, 0, num_ligne, couleur_jeton)

  courant = -math.inf

  """
  creer nouvelle grille temporaire
  a revoir
  tmp = Grille(6,7)
  tmp = cls_grille
  """

  while (cls_grille.coup_valide(cls_grille, num_colonne)) == True:
    joueur_actuel.jouer_coup(cls_grille, num_colonne)
    score = - fail_soft(cls_grille, joueur_suivant, joueur_actuel, profondeur-1, -beta, -alpha) 

    #annuler le dernier coup à remplacer

    if score >= courant :
      courant = score;
      meilleur_coup = num_colonne
      if score >= alpha :
        alpha = score
        meilleur_coup = num_colonne
        #if score >= beta :
        #  break;

  return courant, meilleur_coup;
    
#Faire une copie de la grille de base qu'on garde en tete
#la reutiliser pour toutes les 7 possibilités de jeu si ya de la place dans toutes les colonnes
#appeler failsoft avec l ajout du coup à une copie de cette grille
#faire ca pour tous les coups possibles
