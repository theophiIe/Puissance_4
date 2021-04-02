import Puissance_4/src/Debug/Gestion_de_jeu/Gestion_grille 
import Puissance_4/src/Debug/Gestion_de_jeu/Gestion_joueur
import Puissance_4/src/Debug/Gestion_de_jeu/Gestion_jeton
import Puissance_4/src/Debug/Gestion_de_jeu/Partie
import numpy
import math



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
  pass
  
  
  
def evaluation_coup(grille, num_ligne, num_colonne, couleur_jeton)
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
  pass
  
  
def fail_soft(cls_grille, profondeur, aplha, beta) 
  """
    Cette fonction permet de faire des calculs sur la grille en prévoyant les coups à l'avance, 
    et ainsi nous donner la colonne qui serait la plus optimale de jouer.
    
    cls_grille : instance de la classe Grille
    profondeur : entier correspondant à la profondeur de recherche à laquelle on s'arrête lors des calculs
    alpha : entier correspondant à la valeur minimale
    beta : entier correspondant à la valeur maximale
    
    Renvoie : 
      - un entier correspondant au meilleur score 
      - un entier correspondant au numéro de la colonne du meilleur coup
  """
  pass
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
