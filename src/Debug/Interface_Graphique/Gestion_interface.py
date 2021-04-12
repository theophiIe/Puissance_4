import pygame

MENU_PRINCIPAL = 0
MODE_DE_JEU = 1
CHARGEMENT = 2
CHOIX_DE_DIFFICULTE = 3
COMMENCER = 4
PARTIE = 5
SAUVEGARDE = 6
NOUVELLE_SAUVEGARDE = 7
VICTOIRE = 8
CONFIRMATION = 9
ERREUR = 10

def affichage_menu_principal(fenetre):
    """
        Cette fonction affiche le menu principal.
        Elle fait appel à la classe Bouton pour afficher les boutons du menu principal.
        
        Paramètre : 
            fenetre : la fenêtre de l'écran
   
        Renvoie : 
            quel_menu : entier correspondant à un numéro compris entre 0 et 10 (inclus)
            faisant référence à la destination du prochain affichage.
    """
    return quel_menu

def affichage_mode_de_jeu(fenetre):
    """
        Cette fonction affiche le menu mode de jeu.
        Ces modes de jeu seront représentés sous la forme de boutons.
        
        Paramètre : 
            fenetre : la fenêtre de l'écran
   
        Renvoie : 
            quel_menu : entier entre 0 et 10 correspondant au prochain affichage
            mode_de_jeu : entier 0 ou 1 correspondant respectivement aux modes 'Joueur vs Joueur' et 'Joueur vs Ordinateur'
            niveau_de_difficulte : entier qui peut prendre 4 cas :
                -1 : lorsque le mode de jeu correspond à Joueur vs Joueur
                0  : le niveau de difficulté facile
                1  : le niveau de difficulté intermédiaire
                2  : le niveau de difficulté difficile
            qui_commence : eniter 0 ou 1 correspondant l'ordre de passage. 
                0 : pour que le Joueur 1 commence
                1 : pour que le Joueur 2 commence
    """
    return quel_menu, mode_de_jeu, niveau_de_difficulte, qui_commence

def affichage_chargement(fenetre):
    """
        Cette fonction affiche le menu de chargement.
        Les différentes actions de chargement seront représenté sous forme de boutons.
        
        Paramètre : 
            fenetre : la fenêtre de l'écran
   
        Renvoie : 
            quel_menu : entier entre 0 et 10 correspondant au prochain affichage
            nom_fichier : chaîne de caractères correspondant à un nom de fichier
                - soit la chaîne est vide (pas de chargement)
                - soit la chaîne correspond à un nom de fichier sauvegardé
    """
    return quel_menu, nom_fichier

def affichage_choix_de_difficulte(fenetre):
    """
        Cette fonction affiche le menu de choix de difficulté.
        Le niveau de difficulté sera représenté par 3 boutons.
        
        Paramètre : 
            fenetre : la fenêtre de l'écran
   
        Renvoie : 
            resultat_du_retour : eniter 0 ou 1 correspondant l'ordre de passage. 
                0 : pour que le Joueur 1 commence
                1 : pour que le Joueur 2 commence
            niveau_de_difficulté : entier qui peut prendre 4 cas :
                -1 : lorsque le mode de jeu correspond à Joueur vs Joueur
                0  : le niveau de difficulté facile
                1  : le niveau de difficulté intermédiaire
                2  : le niveau de difficulté difficile
            quel_joueur_joue : boooléen qui détermine l'ordre de passage qui est retourné par affichage_commencer
    """
    return resultat_du_retour, niveau_de_difficulte, quel_joueur_joue

def affichage_commencer(fenetre):
   """
        Cette fonction affiche le menu de l'ordre de passage.
        Le Joueur 1 devra choisir s'il veut commencer la partie en premier ou non.
        
        Paramètre : 
            fenetre : la fenêtre de l'écran
   
        Renvoie : 
            resultat_du_retour : eniter 0 ou 1 correspondant l'ordre de passage 
                0 : pour que le Joueur 1 commence
                1 : pour que le Joueur 2 commence
            quel_joueur_joue : boooléen qui détermine l'ordre de passage
    """
    return resultat_du_retour, quel_joueur_joue

def affichage_partie(fenetre, grille, mode_de_jeu, qui_commence, niveau_de_difficulte):
    """
        Cette fonction affiche la partie.
        Elle initialise la grille de jeu ainsi que les différentes options sous forme de bouton.
                
        Paramètre : 
            fenetre : la fenêtre de l'écran
            grille : grille de jetons:
                - initialisée à vide si aucun chargement n'a pas été effectué
                - initialisée avec une configuration prédéfinie si un chargement à été effectué
            qui_commence : eniter 0 ou 1 correspondant l'ordre de passage. 
                0 : pour que le Joueur 1 commence
                1 : pour que le Joueur 2 commence
            niveau_de_difficulte : entier qui peut prendre 4 cas :
                -1 : lorsque le mode de jeu correspond à Joueur vs Joueur
                0  : le niveau de difficulté facile
                1  : le niveau de difficulté intermédiaire
                2  : le niveau de difficulté difficile
          
        Renvoie : 
            nom_gagnant : chaîne de caractères retennant le nom du vainqueur.  
    """
    return nom_gagnant

def affichage_sauvegarde(fenetre):
    pass

def affichage_nouvelle_sauvegarde(fenetre):
    pass

def affichage_victoire(fenetre):
    """
        Cette fonction affiche l'écran de victoire avec le nome du vainqueur.
                
        Paramètre : 
            fenetre : la fenêtre de l'écran
            
        Renvoie : 
            Un entier correspondant à un numéro compris entre 0 et 1
            faisant référence à la destination du prochain affichage.
    """
    return MENU_PRINCIPAL ou MODE_DE_JEU

def affichage_confirmation(fenetre, texte):
    return resultat

def affichage_erreur(fenetre, texte):
    pass

def affichage_aide(fenetre, grille):
    """
        Cette fonction affiche l'aide du système pour le Joueur.
        L'utilisateur peut re-appeller cette fonction pour effacer l'aide du système.
                
        Paramètres : 
            fenetre : la fenêtre de l'écran
            grille : grille de jetons
    """
    pass

def affichage_jeton(fenetre, grille, num_ligne, num_colonne):
    """
        Cette fonction affiche un jeton.
        Le jeton sera affiché sur la plus basse case non occupée d'une colonne choisie.
                
        Paramètres : 
            fenetre : la fenêtre de l'écran
            grille : grille de jetons
            num_ligne : entier indiquant le numéro de la ligne de la grille
            num_colonne : entier indiquant le numéro de la colonne de la grille
    """
    pass

def affichage_grille_jeton(fenetre, grille): 
    """
        Cette fonction affiche la grille contenant les jetons.
        
        Paramètres : 
            fenetre : la fenêtre de l'écran
            grille : grille de jetons
    """
    pass
    
def click_colonne_ou_pas(fenetre, event):
    return num_colonne


def lancer_affichage():
    pass


