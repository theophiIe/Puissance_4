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
    while etat == true:
        for all_evenement:
            if(evenement == QUIT):

            if(evenement == MOUSEBUTTONDOWN):
                if(button == nouvelle_partie) renvoie = affichage_mode_de_jeu
                if()

    return MODE_DE_JEU ou CHARGEMENT

def affichage_mode_de_jeu(fenetre):
    return MENU_PRINCIPAL ou COMMENCER(MODE_DE_JEU) ou CHOIX_DE_DIFFICULTE

def affichage_chargement(fenetre):
    return MENU_PRINCIPAL ou CONFIRMATION

def affichage_choix_de_difficulte(fenetre):
    return MODE_DE_JEU ou COMMENCER(CHOIX_DE_DIFFICULTE)

def affichage_commencer(fenetre, texte, ancien_ou_es_tu):
    return (ancien_ou_es_tu = MODE_DE_JEU ou CHOIX_DE_DIFFICULTE) ou PARTIE

def affichage_partie(fenetre, grille):
    return SAUVEGARDE ou CONFIRMATION(PARTIE et VICTOIRE et (texte et nom_gagnant)) ou (VICTOIRE et nom_gagnant)

def affichage_sauvegarde(fenetre):
    return PARTIE ou NOUVELLE_SAUVEGARDE ou CONFIRMATION(PARTIE ou SAUVEGARDE et texte)

def affichage_nouvelle_sauvegarde(fenetre):
    return SAUVEGARDE ou PARTIE

def affichage_victoire(fenetre):
    return MENU_PRINCIPAL ou MODE_DE_JEU

def affichage_confirmation(fenetre, texte, ancien_ou_es_tu, nouveau_ou_es_tu, nom_gagnant=""):
    return (CHARGEMENT ou SAUVEGARDE ou PARTIE) ou (VICTOIRE(nom_gagnant) ou MODE_DE_JEU ou SAUVEGARDE)

def affichage_erreur(fenetre, texte, ancien_ou_es_tu):
    return ancien_ou_es_tu = CHARGEMENT ou SAUVEGARDE ou NOUVELLE_SAUVEGARDE



def affichage_aide(fenetre):

def lancer_affichage():
    ou_es_tu = 0
    grille = new Grille()
    while true:
        if(ou_es_tu == 0) ou_es_tu = affichage_menu_principal
        elif (ou_es_tu == 1) ou_es_tu = affichage_mode_de_jeu
        elif (ou_es_tu == 2) ou_es_tu = affichage_choix_de_difficulte
        elif (ou_es_tu == 3) ou_es_tu = affichage_partie
        elif (ou_es_tu == 4) ou_es_tu = affichage_sauvegarde
        elif (ou_es_tu == 5) ou_es_tu = affichage_chargement
        elif (ou_es_tu == 6):
            resultat = affichage_confirmation
            ou_es_tu = resultat[0]
            n_grille = resultat[1]
            if(ou_es_tu == MODE_DE_JEU) grille = n_grille 
        elif (ou_es_tu == 7) ou_es_tu = affichage_erreur

        resultat = affichage_confirmation
        ou_es_tu = resultat[0]
        n_grille = resultat[1]
        if(ou_es_tu == MODE_DE_JEU) grille = n_grille 

lancer_affichage()
