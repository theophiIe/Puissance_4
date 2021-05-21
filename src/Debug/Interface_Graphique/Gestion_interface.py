import Gestion_bouton
import Gestion_grille
import Gestion_joueur
import Gestion_jeton
from Partie import *
from Sauvegarde import *
from Chargement import *
from Strategies import *

import pygame
import math

import os # pour lire des sauvegardes dans des fichiers à retirer peut-être

SIZE = 0 # taille de la fenetre

MENU_PRINCIPAL = 0
MODE_DE_JEU = 1
CHARGEMENT = 2
CHOIX_DE_DIFFICULTE = 3
COMMENCER = 4
PARTIE = 5
SAUVEGARDE = 6
NOUVELLE_SAUVEGARDE = 7
FIN_DE_PARTIE = 8
CONFIRMATION = 9
ERREUR = 10

# Mettre une variable globale pour le son avec une condition à chaque fois
pygame.mixer.init()

def afficher_grille(grille):
    for i in range(6):
        aff = ''
        for j in range(7):
            if(grille[i][j] is None):
                aff += ' 0'
            elif(grille[i][j].couleur == 1):
                aff += ' 1'
            else:
                aff+= ' 2'
        print(aff)
    print()

def affichage_menu_principal(fenetre):
    
    background = pygame.image.load("Interface_Graphique/Sprites/Backgroundv5.png") 
    fenetre.blit(background, (0, 0))

    b_titre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Titre_blue.png", "Interface_Graphique/Sprites/Titre_blue.png", SIZE/10, SIZE/10, SIZE*8/10, SIZE*2.5/10)
    b_titre.affichage_bouton(fenetre)

    b_jouer = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_jouer.png", "Interface_Graphique/Sprites/Bouton_jouer2.png", SIZE/3, SIZE/2, SIZE/3, SIZE/10)
    b_jouer.affichage_bouton(fenetre)

    b_charger = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_charger.png", "Interface_Graphique/Sprites/Bouton_charger2.png", SIZE/3, SIZE*6.5/10, SIZE/3, SIZE/10)
    b_charger.affichage_bouton(fenetre)

    b_quitter = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_quitter.png", "Interface_Graphique/Sprites/Bouton_quitter2.png", SIZE/3, SIZE*4/5, SIZE/3, SIZE/10)
    b_quitter.affichage_bouton(fenetre)

    pygame.display.flip()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and b_jouer.rectangle.collidepoint(event.pos):
                    pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play()
                    running = False
                    quel_menu = MODE_DE_JEU
                    break

                if event.button == 1 and b_charger.rectangle.collidepoint(event.pos):
                    pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play()
                    running = False
                    quel_menu = CHARGEMENT
                    break

                if event.button == 1 and b_quitter.rectangle.collidepoint(event.pos):
                    pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play()
                    running = False
                    quel_menu = -1
                    break

        if running == False:
            break

        point = pygame.mouse.get_pos()
        b_jouer.collision_bouton(fenetre, point)
        b_charger.collision_bouton(fenetre, point)
        b_quitter.collision_bouton(fenetre, point)

        pygame.display.flip()

    return quel_menu

def affichage_mode_de_jeu(fenetre):
    background = pygame.image.load("Interface_Graphique/Sprites/Backgroundv5.png") 
    fenetre.blit(background, (0, 0))

    b_titre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Titre_choix_mode_jeu.png", "Interface_Graphique/Sprites/Titre_choix_mode_jeu.png", SIZE*0.5/10, SIZE/10, SIZE*9/10, SIZE/6)
    b_titre.affichage_bouton(fenetre)

    b_jvj = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_jvsj.png", "Interface_Graphique/Sprites/Bouton_jvsj2.png", SIZE/3, SIZE * 2/5, SIZE/3, SIZE/10)
    b_jvj.affichage_bouton(fenetre)

    b_jvo = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_jvso.png", "Interface_Graphique/Sprites/Bouton_jvso2.png", SIZE/3, SIZE*3/5, SIZE/3, SIZE/10)
    b_jvo.affichage_bouton(fenetre)

    b_retour = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_retour.png", "Interface_Graphique/Sprites/Bouton_retour2.png", SIZE/3, SIZE*4/5, SIZE/3, SIZE/10)
    b_retour.affichage_bouton(fenetre)

    pygame.display.flip()

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if event.button == 1 and b_jvj.rectangle.collidepoint(event.pos):
                    qui_commence = -1
                    retour, qui_commence = affichage_commencer(fenetre)
                    if retour == False:
                        running = False
                        mode_de_jeu = True
                        niveau_de_difficulte = -1
                        quel_menu = PARTIE
                        break

                elif event.button == 1 and b_jvo.rectangle.collidepoint(event.pos):
                    niveau_de_difficulte, qui_commence = affichage_choix_de_difficulte(fenetre)
                    if niveau_de_difficulte != -1:
                        running = False
                        mode_de_jeu = False
                        quel_menu = PARTIE
                        break
                
                elif event.button == 1 and b_retour.rectangle.collidepoint(event.pos):
                    running = False
                    quel_menu = MENU_PRINCIPAL
                    mode_de_jeu = -1
                    niveau_de_difficulte = -2
                    qui_commence = -1
                    break

        if running == False:
            break
        
        fenetre.blit(background, (0, 0))
        b_titre.affichage_bouton(fenetre)
        point = pygame.mouse.get_pos()
        b_jvj.collision_bouton(fenetre, point)
        b_jvo.collision_bouton(fenetre, point)
        b_retour.collision_bouton(fenetre, point)
        pygame.display.flip()

    return quel_menu, mode_de_jeu, qui_commence, niveau_de_difficulte

def affichage_chargement(fenetre):
    background = pygame.image.load("Interface_Graphique/Sprites/Backgroundv5.png") 
    fenetre.blit(background, (0, 0))

    b_titre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Menu_chargement.png", "Interface_Graphique/Sprites/Menu_chargement.png", SIZE*0.5/10, SIZE/10, SIZE*9/10, SIZE/6)
    b_titre.affichage_bouton(fenetre)
    
    b_charger = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_charger.png", "Interface_Graphique/Sprites/Bouton_charger2.png", SIZE*6.75/10, SIZE*4/5, SIZE/4, SIZE/10)
    b_charger.affichage_bouton(fenetre)

    b_supprimer = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_supprimer.png", "Interface_Graphique/Sprites/Bouton_supprimer2.png", SIZE*3.75/10, SIZE*4/5, SIZE/4, SIZE/10)
    b_supprimer.affichage_bouton(fenetre)

    b_retour = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_retour.png", "Interface_Graphique/Sprites/Bouton_retour2.png", SIZE*0.75/10, SIZE*4/5, SIZE/4, SIZE/10)
    b_retour.affichage_bouton(fenetre)

    pygame.display.flip()

    # ============== DEB MENU DEROULANT + LISTES SAUVERGARDES ==============
    # nombre de sauvegardes
    nb_sauv = 0

    # init sauvegardes
    tab_sauvegarde = []
    nom_sauvegarde = []
    text_sauvegardes = []
    text_sauvegardes_rect = []
    sauvegarde_choisie = -1

    # récupérer les fichiers .txt
    path = r'Liste_sauvegardes'
    tmp = []
    for files in os.walk(path):
        for filename in files:
            tmp.append(filename)
    
    for j in range (len (tmp[2])):
        if tmp[2][j].endswith('.txt'):
            nb_sauv += 1
            nom_sauvegarde.append(tmp[2][j])

    # menu déroulant    
    if nb_sauv > 3:
        menu = pygame.Surface( ( int(SIZE*4/5) , int(nb_sauv * SIZE/10) + 5 ) )
        area = pygame.Rect(0, 0, SIZE*4/5, SIZE*2/5 +5)
    else:
        menu = pygame.Surface( ( int(SIZE*4/5) , int(nb_sauv * SIZE/10) + 5 ) )
        area = pygame.Rect(0, 0, SIZE*4/5, SIZE*nb_sauv/10 +5)

    background_deroulant = pygame.image.load("Interface_Graphique/Sprites/Backgroundv4.png") 
    menu.blit( background_deroulant, (0, 0) )
    menu_rect = menu.get_rect()

    menu_subsurface = menu.subsurface(area)

    #point de la zone déroulante 
    pos = (SIZE/10, SIZE*3/10)
    # vitesse de déroulement
    pos_change = 20
    # zone menu_déroulant
    cx1 = SIZE/10
    cx2 = SIZE/10 + SIZE*4/5
    cy1 = SIZE*3/10
    cy2 = SIZE*3/10 + SIZE*2/5 +5

    
    for i in range(nb_sauv):
        sauv = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_vide.png", "Interface_Graphique/Sprites/Bouton_vide2.png", 5, 5 + i*SIZE/10, SIZE*4/5 - 10, SIZE/10 - 5)
        sauv.affichage_bouton(menu)
        tab_sauvegarde.append(sauv)
        if len(nom_sauvegarde[i]) < 30:
            font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int(SIZE / 15))
        else:
            font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int(SIZE / (len(nom_sauvegarde[i])/2) ))
        tmp_text = font.render(nom_sauvegarde[i], True, "white")
        tmp_text_rect = tmp_text.get_rect(center = (SIZE*4/10, SIZE/20+i*SIZE/10) )
        text_sauvegardes.append(tmp_text)
        text_sauvegardes_rect.append(tmp_text_rect)
        menu.blit(tmp_text, tmp_text_rect)

    # ============== FIN MENU DEROULANT + LISTES SAUVERGARDES ==============

    running = True
    while running:
                
        point = pygame.mouse.get_pos()
        x_point_menu , y_point_menu = point
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if event.button == 1 and b_charger.rectangle.collidepoint(event.pos):
                    if sauvegarde_choisie != -1:
                        running = False
                        quel_menu = MODE_DE_JEU
                        nom_fichier = nom_sauvegarde[sauvegarde_choisie]
                        break
                    else:
                        affichage_erreur(fenetre, "Aucune sauvegarde sélectionnée !")

                elif event.button == 1 and b_supprimer.rectangle.collidepoint(event.pos):

                    if sauvegarde_choisie != -1:
                        
                        confirmation = affichage_confirmation(fenetre, "Supprimer la sauvegarde ?")

                        if confirmation == True:

                            verif_supprimer = supprimer_sauvegarde(nom_sauvegarde[sauvegarde_choisie])
                            if verif_supprimer == False:
                                affichage_erreur(fenetre, "Erreur lors de la suppression")
                            else:
                                # ======= MODIF DEB MENU DEROULANT + LISTES SAUVERGARDES =======
                                # nombre de sauvegardes
                                nb_sauv -= 1
                                tab_sauvegarde.remove( tab_sauvegarde[sauvegarde_choisie] )
                                nom_sauvegarde.remove( nom_sauvegarde[sauvegarde_choisie] )
                                text_sauvegardes.remove( text_sauvegardes[sauvegarde_choisie] )
                                text_sauvegardes_rect.remove( text_sauvegardes_rect[sauvegarde_choisie] )
                                #modification des coordonnées
                                for i in range(nb_sauv):
                                    tab_sauvegarde[i].changement_taille_bouton(5, 5 + i*SIZE/10, SIZE*4/5 - 10, SIZE/10 - 5)
                                    if len(nom_sauvegarde[i]) < 30:
                                        font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int(SIZE / 15))
                                    else:
                                        font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int(SIZE / (len(nom_sauvegarde[i])/2) ))
                                    tmp_text = font.render(nom_sauvegarde[i], True, "white")
                                    tmp_text_rect = tmp_text.get_rect(center = (SIZE*4/10, SIZE/20+i*SIZE/10) )
                                    text_sauvegardes_rect[i] = tmp_text_rect

                                # menu déroulant    
                                if nb_sauv > 3:
                                    menu = pygame.Surface( ( int(SIZE*4/5) , int(nb_sauv * SIZE/10) + 5 ) )
                                    area = pygame.Rect(0, 0, SIZE*4/5, SIZE*2/5 +5)
                                else:
                                    menu = pygame.Surface( ( int(SIZE*4/5) , int(nb_sauv * SIZE/10) + 5 ) )
                                    area = pygame.Rect(0, 0, SIZE*4/5, SIZE*nb_sauv/10 +5)
                                menu.blit( background_deroulant, (0, 0) )
                                menu_rect = menu.get_rect()

                                menu_subsurface = menu.subsurface(area)

                                sauvegarde_choisie = -1
                                # ======= FIN MENU DEROULANT + LISTES SAUVERGARDES =======
                    else:
                        affichage_erreur(fenetre, "Aucune sauvegarde sélectionnée !")

                elif event.button == 1 and b_retour.rectangle.collidepoint(event.pos):
                    running = False
                    quel_menu = MENU_PRINCIPAL
                    nom_fichier = ""
                    break
                # 4 = scroll up
                elif event.button == 4: 
                    area.y -= pos_change
                    area.clamp_ip(menu_rect)
                    menu_subsurface = menu.subsurface(area)
                # 5 = scroll down
                elif event.button == 5: 
                    area.y += pos_change
                    area.clamp_ip(menu_rect)
                    menu_subsurface = menu.subsurface(area)
                # vérifie si on clique à l'intérieur de la zone déroulante
                # en fonction de pos
                if x_point_menu > cx1 and y_point_menu > cy1 and x_point_menu < cx2 and y_point_menu < cy2:
                    x_point_menu = x_point_menu - SIZE/10
                    y_point_menu = y_point_menu - SIZE*3/10 + area.y
                    point_menu = (x_point_menu, y_point_menu)
                    for i in range (nb_sauv):    
                        # 1 = click gauche        
                        if event.button == 1 and tab_sauvegarde[i].rectangle.collidepoint(point_menu):
                            if sauvegarde_choisie != i:
                                sauvegarde_choisie = i
                            elif sauvegarde_choisie == i:
                                sauvegarde_choisie = -1

        if running == False:
            break
        
        fenetre.blit(background, (0, 0))
        fenetre.blit(menu_subsurface, pos)

        b_titre.affichage_bouton(fenetre)

        b_charger.collision_bouton(fenetre, point)
        b_supprimer.collision_bouton(fenetre, point)
        b_retour.collision_bouton(fenetre, point)

        for i in range(nb_sauv):
            if sauvegarde_choisie == i:
                tab_sauvegarde[i].affichage_bouton_survole(menu)
            else:
                tab_sauvegarde[i].affichage_bouton(menu)
            menu.blit(text_sauvegardes[i], text_sauvegardes_rect[i])

        pygame.display.flip()

    return quel_menu, nom_fichier

def affichage_choix_de_difficulte(fenetre):
    
    background = pygame.image.load("Interface_Graphique/Sprites/Backgroundv5.png") 
    fenetre.blit(background, (0, 0))

    b_titre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Titre_choix_difficulte.png", "Interface_Graphique/Sprites/Titre_choix_difficulte.png", SIZE*0.5/10, SIZE/10, SIZE*9/10, SIZE/8)
    b_titre.affichage_bouton(fenetre)

    b_facile = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_facile.png", "Interface_Graphique/Sprites/Bouton_facile2.png", SIZE*0.5/10, SIZE*4.5/10, SIZE*2.5/10, SIZE/10)
    b_facile.affichage_bouton(fenetre)

    b_intermediare = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_moyen.png", "Interface_Graphique/Sprites/Bouton_moyen2.png", SIZE*3.75/10, SIZE*4.5/10, SIZE*2.5/10, SIZE/10)
    b_intermediare.affichage_bouton(fenetre)

    b_difficile = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_difficile.png", "Interface_Graphique/Sprites/Bouton_difficile2.png", SIZE*7/10, SIZE*4.5/10, SIZE*2.5/10, SIZE/10)
    b_difficile.affichage_bouton(fenetre)

    b_retour = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_retour.png", "Interface_Graphique/Sprites/Bouton_retour2.png", SIZE/3, SIZE*4/5, SIZE/3, SIZE/10)
    b_retour.affichage_bouton(fenetre)

    pygame.display.flip()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if event.button == 1 and b_facile.rectangle.collidepoint(event.pos):
                    niveau_de_difficulte = 0
                    retour, quel_joueur_joue = affichage_commencer(fenetre)
                    if retour == False:
                        running = False
                        break

                elif event.button == 1 and b_intermediare.rectangle.collidepoint(event.pos):
                    niveau_de_difficulte = 1
                    retour, quel_joueur_joue = affichage_commencer(fenetre)
                    if retour == False:
                        running = False
                        break

                elif event.button == 1 and b_difficile.rectangle.collidepoint(event.pos):
                    niveau_de_difficulte = 2
                    retour, quel_joueur_joue = affichage_commencer(fenetre)
                    if retour == False:
                        running = False
                        break

                elif event.button == 1 and b_retour.rectangle.collidepoint(event.pos):
                    running = False
                    niveau_de_difficulte = -1
                    quel_joueur_joue = -1
                    break

        if running == False:
            break
        
        fenetre.blit(background, (0, 0))
        b_titre.affichage_bouton(fenetre)
        point = pygame.mouse.get_pos()
        b_facile.collision_bouton(fenetre, point)
        b_intermediare.collision_bouton(fenetre, point)
        b_difficile.collision_bouton(fenetre, point)
        b_retour.collision_bouton(fenetre, point)

        pygame.display.flip()

    return niveau_de_difficulte, quel_joueur_joue

def affichage_commencer(fenetre):
    
    background = pygame.image.load("Interface_Graphique/Sprites/Backgroundv5.png") 
    fenetre.blit(background, (0, 0))

    b_titre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Titre_commencer.png", "Interface_Graphique/Sprites/Titre_commencer.png", SIZE*0.5/10, SIZE/10, SIZE*9/10, SIZE/8)
    b_titre.affichage_bouton(fenetre)
    
    b_oui = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_oui.png", "Interface_Graphique/Sprites/Bouton_oui2.png", SIZE/5, SIZE/2, SIZE/4, SIZE/10)
    b_oui.affichage_bouton(fenetre)

    b_non = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_non.png", "Interface_Graphique/Sprites/Bouton_non2.png", SIZE * 5.5 / 10, SIZE/2, SIZE/4, SIZE/10)
    b_non.affichage_bouton(fenetre)

    b_retour = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_retour.png", "Interface_Graphique/Sprites/Bouton_retour2.png", SIZE/3, SIZE*4/5, SIZE/3, SIZE/10)
    b_retour.affichage_bouton(fenetre)

    pygame.display.flip()

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if event.button == 1 and b_oui.rectangle.collidepoint(event.pos):
                    running = False
                    retour = False
                    quel_joueur_joue = True
                    break

                elif event.button == 1 and b_non.rectangle.collidepoint(event.pos):
                    running = False
                    retour = False
                    quel_joueur_joue = False
                    break

                elif event.button == 1 and b_retour.rectangle.collidepoint(event.pos):
                    running = False
                    retour = True
                    quel_joueur_joue = -1
                    break

        if running == False:
            break

        fenetre.blit(background, (0, 0))
        b_titre.affichage_bouton(fenetre)
        point = pygame.mouse.get_pos()
        b_oui.collision_bouton(fenetre, point)
        b_non.collision_bouton(fenetre, point)
        b_retour.collision_bouton(fenetre, point)
    
        pygame.display.flip()

    return retour, quel_joueur_joue

def affichage_partie(fenetre, grille, mode_de_jeu, qui_commence, niveau_de_difficulte):
    background = pygame.image.load("Interface_Graphique/Sprites/Backgroundv5.png") 
    fenetre.blit(background, (0, 0))

    print(qui_commence)
    
    b_j1 = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_j1.png", "Interface_Graphique/Sprites/Bouton_j1_2.png", SIZE*8.15/10, SIZE*0.5/10, SIZE*1.5/10, SIZE/15)
    b_j1.affichage_bouton(fenetre)

    if mode_de_jeu == True:
        b_j2 = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_j2.png", "Interface_Graphique/Sprites/Bouton_j2_2.png", SIZE*8.15/10, SIZE*2/10, SIZE*1.5/10, SIZE/15)
        b_j2.affichage_bouton(fenetre)
    else:
        b_j2 = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_ordi.png", "Interface_Graphique/Sprites/Bouton_ordi_2.png", SIZE*8.15/10, SIZE*2/10, SIZE*1.5/10, SIZE/15)
        b_j2.affichage_bouton(fenetre)

    joueur_actuel, joueur_suivant = attribution_des_joueurs(qui_commence, mode_de_jeu, niveau_de_difficulte)

    if type(joueur_actuel) == Gestion_joueur.Ordinateur:
        joueur_actuel.premier_coup(grille.grille)
        affichage_jeton(fenetre, grille, 5, 3)
        joueur_actuel, joueur_suivant = joueur_suivant, joueur_actuel

    b_aide = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_aide.png", "Interface_Graphique/Sprites/Bouton_aide2.png", SIZE*8.15/10, SIZE*5/10, SIZE*1.5/10, SIZE/15)
    b_aide.affichage_bouton(fenetre)

    b_sauvegarde = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_sauv.png", "Interface_Graphique/Sprites/Bouton_sauv2.png", SIZE*8.15/10, SIZE*6.5/10, SIZE*1.5/10, SIZE/15)
    b_sauvegarde.affichage_bouton(fenetre)

    b_abandon = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_abandon.png", "Interface_Graphique/Sprites/Bouton_abandon2.png", SIZE*8.15/10, SIZE*8/10, SIZE*1.5/10, SIZE/15)
    b_abandon.affichage_bouton(fenetre)

    pygame.display.flip()

    affichage_grille_jeton(fenetre, grille)

    tour = qui_commence
    aide = 0
    texte_fin_de_partie = ""
    running = True
    while running:

        point = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                colonne_selectionnee = selection_colonne(fenetre, event)

                if event.button == 1 and b_aide.rectangle.collidepoint(event.pos):
                    

                    if aide == 0:
                        aide = 1
                    else:
                        aide = 0
                        fenetre.blit(background, (0, 0))
                        affichage_grille_jeton(fenetre, grille)

                elif event.button == 1 and b_sauvegarde.rectangle.collidepoint(event.pos):
                    affichage_sauvegarde(fenetre, grille)
                    fenetre.blit(background, (0, 0))
                    affichage_grille_jeton(fenetre, grille)
                    
                elif event.button == 1 and b_abandon.rectangle.collidepoint(event.pos):
                    
                    
                    confirmation = affichage_confirmation(fenetre, "Êtes-vous sûr ?")
                    fenetre.blit(background, (0, 0))
                    affichage_grille_jeton(fenetre, grille)
                    if confirmation == True:
                        running = False
                        tour = not tour
                        break

                elif colonne_selectionnee != -1 and grille.coup_valide(colonne_selectionnee):
                    num_ligne, num_colonne, joueur_actuel, joueur_suivant = actions_coup_joueur(grille, colonne_selectionnee, joueur_actuel, joueur_suivant, niveau_de_difficulte)
                    affichage_jeton(fenetre, grille, num_ligne, num_colonne)
                    afficher_grille(grille.grille)

                    val_fin_de_partie = fin_de_partie(grille, (joueur_suivant.commence-1)%2 + 1)
                    if val_fin_de_partie != 0:
                        if val_fin_de_partie == 2:
                            if tour == True:
                                return "Vainqueur : J1 !"
                            elif tour == False and mode_de_jeu == True:
                                return "Vainqueur : J2 !"
                            elif tour == False and mode_de_jeu == False:
                                return "Vainqueur : ORDI !"
                        else:
                            return "Match Nul !"
                    tour = not tour
                    if type(joueur_actuel) == Gestion_joueur.Ordinateur:
                        num_ligne, num_colonne, joueur_actuel, joueur_suivant = actions_coup_joueur(grille, colonne_selectionnee, joueur_actuel, joueur_suivant, niveau_de_difficulte)
                        affichage_jeton(fenetre, grille, num_ligne, num_colonne)
                        

                        val_fin_de_partie = fin_de_partie(grille, (joueur_suivant.commence-1)%2 + 1)
                        if val_fin_de_partie != 0:
                            if val_fin_de_partie == 2:
                                if tour == True:
                                    return "Vainqueur : J1 !"
                                elif tour == False and mode_de_jeu == True:
                                    return "Vainqueur : J2 !"
                                elif tour == False and mode_de_jeu == False:
                                    return "Vainqueur : ORDI !"
                            else:
                                return "Match Nul !"
                        tour = not tour
                    
                    pygame.mixer.music.load('Interface_Graphique/Sounds/jeton.wav')
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play()
                    
        if running == False:
            break

        if mode_de_jeu == False and tour == False:
            pass

        if aide == 1:
            affichage_aide(fenetre, grille)

        if tour == True:
            b_j1.affichage_bouton_survole(fenetre)
            b_j2.affichage_bouton(fenetre)
        else:
            b_j2.affichage_bouton_survole(fenetre)
            b_j1.affichage_bouton(fenetre)

        if aide == 1:
            b_aide.affichage_bouton_survole(fenetre)
        else:
            b_aide.affichage_bouton(fenetre)

        b_sauvegarde.collision_bouton(fenetre, point)
        b_abandon.collision_bouton(fenetre, point)

        pygame.display.flip()

    if tour == True:
        texte_fin_de_partie = "Vainqueur : J1 !"
    elif tour == False and mode_de_jeu == True:
        texte_fin_de_partie = "Vainqueur : J2 !"
    elif tour == False and mode_de_jeu == False:
        texte_fin_de_partie = "Vainqueur : ORDI !"

    return texte_fin_de_partie

def affichage_sauvegarde(fenetre, grille):
    
    background = pygame.image.load("Interface_Graphique/Sprites/Backgroundv5.png") 
    fenetre.blit(background, (0, 0))

    b_titre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Menu_sauvegarde.png", "Interface_Graphique/Sprites/Menu_sauvegarde.png", SIZE*0.5/10, SIZE/10, SIZE*9/10, SIZE/6)
    b_titre.affichage_bouton(fenetre)
    
    b_sauvegarder = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_sauv.png", "Interface_Graphique/Sprites/Bouton_sauv2.png", SIZE*6.75/10, SIZE*4/5, SIZE/4, SIZE/10)
    b_sauvegarder.affichage_bouton(fenetre)

    b_supprimer = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_supprimer.png", "Interface_Graphique/Sprites/Bouton_supprimer2.png", SIZE*3.75/10, SIZE*4/5, SIZE/4, SIZE/10)
    b_supprimer.affichage_bouton(fenetre)

    b_retour = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_retour.png", "Interface_Graphique/Sprites/Bouton_retour2.png", SIZE*0.75/10, SIZE*4/5, SIZE/4, SIZE/10)
    b_retour.affichage_bouton(fenetre)

    pygame.display.flip()

    # ============== DEB MENU DEROULANT + LISTES SAUVERGARDES ==============
    # nombre de sauvegardes
    nb_sauv = 0

    # init sauvegardes
    tab_sauvegarde = []
    nom_sauvegarde = []
    text_sauvegardes = []
    text_sauvegardes_rect = []
    sauvegarde_choisie = -1

    # récupérer les fichiers .txt
    path = r'Liste_sauvegardes'
    tmp = []
    for files in os.walk(path):
        for filename in files:
            tmp.append(filename)

    for j in range (len (tmp[2])):
        if tmp[2][j].endswith('.txt'):
            nb_sauv += 1
            nom_sauvegarde.append(tmp[2][j])

    # menu déroulant    

    if nb_sauv > 3:
        menu = pygame.Surface( ( int(SIZE*4/5) , int(nb_sauv * SIZE/10) + 5 ) )
        area = pygame.Rect(0, 0, SIZE*4/5, SIZE*2/5 +5)
    else:
        menu = pygame.Surface( ( int(SIZE*4/5) , int(nb_sauv * SIZE/10) + 5 ) )
        area = pygame.Rect(0, 0, SIZE*4/5, SIZE*nb_sauv/10 +5)

    background_deroulant = pygame.image.load("Interface_Graphique/Sprites/Backgroundv4.png") 
    menu.blit( background_deroulant, (0, 0) )
    menu_rect = menu.get_rect()

    menu_subsurface = menu.subsurface(area)

    #point de la zone déroulante 
    pos = (SIZE/10, SIZE*3/10)
    # vitesse de déroulement
    pos_change = 20
    # zone menu_déroulant
    cx1 = SIZE/10
    cx2 = SIZE/10 + SIZE*4/5
    cy1 = SIZE*3/10
    cy2 = SIZE*3/10 + SIZE*2/5 +5

    for i in range(nb_sauv):
        sauv = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_vide.png", "Interface_Graphique/Sprites/Bouton_vide2.png", 5, 5 + i*SIZE/10, SIZE*4/5 - 10, SIZE/10 - 5)
        sauv.affichage_bouton(menu)
        tab_sauvegarde.append(sauv)
        
        if len(nom_sauvegarde[i]) < 30:
            font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int(SIZE / 15))
        else:
            font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int(SIZE / (len(nom_sauvegarde[i])/2) ))
        tmp_text = font.render(nom_sauvegarde[i], True, "white")
        tmp_text_rect = tmp_text.get_rect(center = (SIZE*4/10, SIZE/20+i*SIZE/10) )
        text_sauvegardes.append(tmp_text)
        text_sauvegardes_rect.append(tmp_text_rect)
        menu.blit(tmp_text, tmp_text_rect)

    # ============== FIN MENU DEROULANT + LISTES SAUVERGARDES ==============

    running = True
    while running:
                
        point = pygame.mouse.get_pos()
        x_point_menu , y_point_menu = point
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if event.button == 1 and b_sauvegarder.rectangle.collidepoint(event.pos):
                    if sauvegarde_choisie != -1:
                        confirmation = affichage_confirmation(fenetre, "Ecraser les données ?")
                        if confirmation == True :
                            sauvegarde(grille.grille, nom_sauvegarde[sauvegarde_choisie] )
                            running = False
                            break
                    else:
                        running = False
                        affichage_nouvelle_sauvegarde(fenetre, grille)
                        break
                elif event.button == 1 and b_supprimer.rectangle.collidepoint(event.pos):
                    if sauvegarde_choisie != -1:
                        
                        confirmation = affichage_confirmation(fenetre, "Supprimer la sauvegarde ?")

                        if confirmation == True:

                            verif_supprimer = supprimer_sauvegarde(nom_sauvegarde[sauvegarde_choisie])
                            if verif_supprimer == False:
                                affichage_erreur(fenetre, "Erreur lors de la suppression")
                            else:
                                # ======= MODIF DEB MENU DEROULANT + LISTES SAUVERGARDES =======
                                # nombre de sauvegardes
                                nb_sauv -= 1
                                tab_sauvegarde.remove( tab_sauvegarde[sauvegarde_choisie] )
                                nom_sauvegarde.remove( nom_sauvegarde[sauvegarde_choisie] )
                                text_sauvegardes.remove( text_sauvegardes[sauvegarde_choisie] )
                                text_sauvegardes_rect.remove( text_sauvegardes_rect[sauvegarde_choisie] )
                                #modification des coordonnées
                                for i in range(nb_sauv):
                                    tab_sauvegarde[i].changement_taille_bouton(5, 5 + i*SIZE/10, SIZE*4/5 - 10, SIZE/10 - 5)
                                    if len(nom_sauvegarde[i]) < 30:
                                        font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int(SIZE / 15))
                                    else:
                                        font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int(SIZE / (len(nom_sauvegarde[i])/2) ))
                                    tmp_text = font.render(nom_sauvegarde[i], True, "white")
                                    tmp_text_rect = tmp_text.get_rect(center = (SIZE*4/10, SIZE/20+i*SIZE/10) )
                                    text_sauvegardes_rect[i] = tmp_text_rect

                                # menu déroulant    
                                if nb_sauv > 3:
                                    menu = pygame.Surface( ( int(SIZE*4/5) , int(nb_sauv * SIZE/10) + 5 ) )
                                    area = pygame.Rect(0, 0, SIZE*4/5, SIZE*2/5 +5)
                                else:
                                    menu = pygame.Surface( ( int(SIZE*4/5) , int(nb_sauv * SIZE/10) + 5 ) )
                                    area = pygame.Rect(0, 0, SIZE*4/5, SIZE*nb_sauv/10 +5)
                                menu.blit( background_deroulant, (0, 0) )
                                menu_rect = menu.get_rect()

                                menu_subsurface = menu.subsurface(area)

                                sauvegarde_choisie = -1
                                # ======= FIN MENU DEROULANT + LISTES SAUVERGARDES =======
                    else:
                        affichage_erreur(fenetre, "Aucune sauvegarde sélectionnée !")

                elif event.button == 1 and b_retour.rectangle.collidepoint(event.pos):
                    running = False
                    nom_fichier = ""
                    break
                # 4 = scroll up
                elif event.button == 4: 
                    area.y -= pos_change
                    area.clamp_ip(menu_rect)
                    menu_subsurface = menu.subsurface(area)
                # 5 = scroll down
                elif event.button == 5: 
                    area.y += pos_change
                    area.clamp_ip(menu_rect)
                    menu_subsurface = menu.subsurface(area)
                # vérifie si on clique à l'intérieur de la zone déroulante
                # en fonction de pos
                if x_point_menu > cx1 and y_point_menu > cy1 and x_point_menu < cx2 and y_point_menu < cy2:
                    x_point_menu = x_point_menu - SIZE/10
                    y_point_menu = y_point_menu - SIZE*3/10 + area.y
                    point_menu = (x_point_menu, y_point_menu)
                    for i in range (nb_sauv):    
                        # 1 = click gauche        
                        if event.button == 1 and tab_sauvegarde[i].rectangle.collidepoint(point_menu):
                            if sauvegarde_choisie != i:
                                sauvegarde_choisie = i
                            elif sauvegarde_choisie == i:
                                sauvegarde_choisie = -1

        if running == False:
            break
        
        fenetre.blit(background, (0, 0))
        fenetre.blit(menu_subsurface, pos)

        b_titre.affichage_bouton(fenetre)

        #mouse detection
        b_sauvegarder.collision_bouton(fenetre, point)
        b_supprimer.collision_bouton(fenetre, point)
        b_retour.collision_bouton(fenetre, point)

        for i in range(nb_sauv):
            if sauvegarde_choisie == i:
                tab_sauvegarde[i].affichage_bouton_survole(menu)
            else:
                tab_sauvegarde[i].affichage_bouton(menu)
            menu.blit(text_sauvegardes[i], text_sauvegardes_rect[i])

        pygame.display.flip()

def affichage_nouvelle_sauvegarde(fenetre, grille):
    background = pygame.image.load("Interface_Graphique/Sprites/Backgroundv5.png") 
    fenetre.blit(background, (0, 0))

    b_titre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Menu_sauvegarde.png", "Interface_Graphique/Sprites/Menu_sauvegarde.png", SIZE*0.5/10, SIZE/10, SIZE*9/10, SIZE/6)
    b_titre.affichage_bouton(fenetre)

    b_sauvegarder = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_sauv.png", "Interface_Graphique/Sprites/Bouton_sauv2.png", SIZE*6.75/10, SIZE*4/5, SIZE/4, SIZE/10)
    b_sauvegarder.affichage_bouton(fenetre)

    b_retour = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_retour.png", "Interface_Graphique/Sprites/Bouton_retour2.png", SIZE*0.75/10, SIZE*4/5, SIZE/4, SIZE/10)
    b_retour.affichage_bouton(fenetre)
        
    input_box = pygame.Rect(SIZE/2 - SIZE/9.5, SIZE/2, SIZE/10, SIZE/20)
    clock = pygame.time.Clock()
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    font = pygame.font.Font(None, 50)

    pygame.display.flip()

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if event.button == 1 and b_sauvegarder.rectangle.collidepoint(event.pos):
                    if text != "": 
                        confirmation = affichage_confirmation(fenetre, "Confirmer ?")
                        if confirmation == True: 
                            if text.find(".txt") == -1:
                                text += '.txt'
                            if sauvegarde(grille.grille, text):
                                running = False
                                break
                            else:
                                affichage_erreur(fenetre, "Le fichier {} n'a pas pu être sauvergardé".format(text))
                    else:
                        affichage_erreur(fenetre, "Nom du fichier vide")
                if event.button == 1 and b_retour.rectangle.collidepoint(event.pos):
                    running = False
                    break
                if event.button == 1 and input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        text = ''
                        input_box.x = SIZE/2 - SIZE/9.5
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 30:
                            text += event.unicode  
        
        if running == False:
            break

        fenetre.blit(background, (0, 0))

        b_titre.affichage_bouton(fenetre)

        point = pygame.mouse.get_pos()
        b_sauvegarder.collision_bouton(fenetre, point)
        b_retour.collision_bouton(fenetre, point)
        
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(SIZE/5, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the input_box rect.
        if width > SIZE/5:
            input_box.x = SIZE/2 - SIZE/9.5 - ( (width-SIZE/5) /2 )

        pygame.draw.rect(fenetre, color, input_box, 4)
        # Blit the text.
        fenetre.blit(txt_surface, (input_box.x+5, input_box.y+7))
    
        pygame.display.flip()
        clock.tick(30)

def affichage_fin_de_partie(fenetre, texte_fin_de_partie):
    
    background = pygame.image.load("Interface_Graphique/Sprites/Background_trans.png") 
    fenetre.blit(background, (0, 0))
    print("texte = ", texte_fin_de_partie)
    font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int( SIZE / 6 ) )
    texte_aff = font.render(texte_fin_de_partie, True, "royalblue1")
    texte_rect = texte_aff.get_rect(center = (SIZE*5/10, SIZE*2.25/10) )
    fenetre.blit(texte_aff, texte_rect)

    #DEBUT SON
    
    pygame.mixer.music.load('Interface_Graphique/Sounds/OMG.wav') #victoire_2.wav
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play()
    #FIN SON 
    
    b_rejouer = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_rejouer.png", "Interface_Graphique/Sprites/Bouton_rejouer2.png", SIZE/3, SIZE/2, SIZE/3, SIZE/10)
    b_rejouer.affichage_bouton(fenetre)

    b_menu_principal = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_mainmenu.png", "Interface_Graphique/Sprites/Bouton_mainmenu2.png", SIZE/3, SIZE*6.5/10, SIZE/3, SIZE/10)
    b_menu_principal.affichage_bouton(fenetre)

    b_quitter = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_quitter.png", "Interface_Graphique/Sprites/Bouton_quitter2.png", SIZE/3, SIZE*4/5, SIZE/3, SIZE/10)
    b_quitter.affichage_bouton(fenetre)

    pygame.display.flip()

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if b_rejouer.rectangle.collidepoint(event.pos):
                    running = False
                    quel_menu = MODE_DE_JEU
                    break
                elif b_menu_principal.rectangle.collidepoint(event.pos):
                    running = False
                    quel_menu = MENU_PRINCIPAL
                    break
                elif b_quitter.rectangle.collidepoint(event.pos):
                    running = False
                    quel_menu = -1
                    break

        if running == False:
            break

        point = pygame.mouse.get_pos()
        b_rejouer.collision_bouton(fenetre, point)
        b_menu_principal.collision_bouton(fenetre, point)
        b_quitter.collision_bouton(fenetre, point)
    
        pygame.display.flip()
    
    return quel_menu

def affichage_confirmation(fenetre, texte):
    
    b_fenetre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Blackground.png", "Interface_Graphique/Sprites/Blackground.png", SIZE/5, SIZE/5, SIZE*3/5, SIZE*4/10)
    b_fenetre.affichage_bouton(fenetre)
    
    if len(texte) < 25:
        font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int( SIZE / 12 ) )
    else:
        font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int( SIZE / (len(texte)/1.5) ) )

    texte_aff = font.render(texte, True, "royalblue1")
    texte_rect = texte_aff.get_rect(center = (SIZE*5/10, SIZE*3.5/10) )
    fenetre.blit(texte_aff, texte_rect)

    b_oui = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_oui.png", "Interface_Graphique/Sprites/Bouton_oui2.png", SIZE*3/10, SIZE*4.5/10, SIZE*1.5/10, SIZE*0.75/10)
    b_oui.affichage_bouton(fenetre)

    b_non = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_non.png", "Interface_Graphique/Sprites/Bouton_non2.png", SIZE*5.5/10, SIZE*4.5/10, SIZE*1.5/10, SIZE*0.75/10)
    b_non.affichage_bouton(fenetre)

    pygame.display.flip()

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if event.button == 1 and b_oui.rectangle.collidepoint(event.pos):
                    running = False
                    resultat = True
                    break
                elif event.button == 1 and b_non.rectangle.collidepoint(event.pos):
                    running = False
                    resultat = False
                    break

        if running == False:
            break

        point = pygame.mouse.get_pos()
        b_oui.collision_bouton(fenetre, point)
        b_non.collision_bouton(fenetre, point)
    
        pygame.display.flip()

    return resultat

def affichage_erreur(fenetre, texte):
    
    #DEBUT SON
    
    pygame.mixer.music.load('Interface_Graphique/Sounds/erreur.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    #FIN SON

    b_fenetre = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Blackground.png", "Interface_Graphique/Sprites/Blackground.png", SIZE/5, SIZE/5, SIZE*3/5, SIZE*4/10)
    b_fenetre.affichage_bouton(fenetre)
    
    b_croix_rouge = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_croix.png", "Interface_Graphique/Sprites/Bouton_croix2.png", SIZE*7.5/10, SIZE/5, SIZE/20, SIZE/20)
    b_croix_rouge.affichage_bouton(fenetre)

    b_ok = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Bouton_ok.png", "Interface_Graphique/Sprites/Bouton_ok2.png", SIZE*4/10, SIZE*4.5/10, SIZE/5, SIZE*0.75/10)
    b_ok.affichage_bouton(fenetre)

    if len(texte) > 20:
        font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int( SIZE / 18 ) )
    else:
        font = pygame.font.Font('Interface_Graphique/Cafeteria-Bold.otf', int( SIZE / 12 ) )

    texte_aff = font.render(texte, True, "royalblue1")
    texte_rect = texte_aff.get_rect(center = (SIZE*5/10, SIZE*3.5/10) )
    fenetre.blit(texte_aff, texte_rect)

    pygame.display.flip()

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pygame.mixer.music.load('Interface_Graphique/Sounds/clic.wav')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()

                if event.button == 1 and b_croix_rouge.rectangle.collidepoint(event.pos):
                    running = False
                    break
                elif event.button == 1 and b_ok.rectangle.collidepoint(event.pos):
                    running = False
                    break

        point = pygame.mouse.get_pos()
        b_croix_rouge.collision_bouton(fenetre, point)
        b_ok.collision_bouton(fenetre, point)
    
        pygame.display.flip()

def affichage_aide(fenetre, grille):
    for num_colonne in range (7):
        b_fleche = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Arrow.png", "Interface_Graphique/Sprites/Arrow.png", SIZE * 0.41/10 + num_colonne * (SIZE*1.068/10), SIZE*9/10, SIZE*0.89/10, SIZE*0.89/10)
        b_fleche.affichage_bouton(fenetre)

def affichage_jeton(fenetre, grille, num_ligne, num_colonne):
    if grille.grille[num_ligne][num_colonne] is not None:
        if grille.grille[num_ligne][num_colonne].couleur == 1:
            b_jeton_rouge = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Jeton_rouge.png", "Interface_Graphique/Sprites/Jeton_rouge.png",SIZE * 0.41/10 + num_colonne * (SIZE*1.068/10), SIZE*2.58/10 + num_ligne * (SIZE*1.068/10), SIZE*0.89/10, SIZE*0.89/10) #SIZE*7.92/10 - num_ligne * (SIZE*1.068/10)
            b_jeton_rouge.affichage_bouton(fenetre)

        else:
            b_jeton_jaune = Gestion_bouton.Bouton("Interface_Graphique/Sprites/Jeton_jaune.png", "Interface_Graphique/Sprites/Jeton_jaune.png", SIZE * 0.41/10 + num_colonne * (SIZE*1.068/10), SIZE*2.58/10 + num_ligne * (SIZE*1.068/10), SIZE*0.89/10, SIZE*0.89/10)
            b_jeton_jaune.affichage_bouton(fenetre)

def affichage_grille_jeton(fenetre, grille): 
    b_grille = Gestion_bouton.Bouton("Interface_Graphique/Sprites/grille.png", "Interface_Graphique/Sprites/grille.png", SIZE*0.20/10, SIZE*2.4/10, SIZE*7.7/10, SIZE*6.6/10)
    b_grille.affichage_bouton(fenetre)

    afficher_grille(grille.grille)
    for ligne in range(grille.ligne):
        for colonne in range(grille.colonne):
            affichage_jeton(fenetre, grille, ligne, colonne)
    
def selection_colonne(fenetre, event):
    """
        Cette fonction permet de vérifier si l'evenement passé en paramètre est un clic gauche.
        Si c'est un clic gauche et qu'il a été fait dans la zone de la grille, càd dans une des colonnes,
        alors il retourne le numéro de la colonne dans laquelle le clic a été fait.

        Paramètre : 
            fenetre : la fenêtre de l'écran
            event : evenement Pygame (clic, touche, quitter ...) 
            
        Renvoie : 
            Un entier correspondant au numéro de colonne dans laqeulle le clic a été fait. 
            0 - 6 : numéro de colonne
            -1 : clic hors zone de grille
    """
    num_colonne = -1
    if event.button == 1:
        b_zone_contact = []
        for i in range (7):
            tmp = pygame.Rect(SIZE*0.20/10 + (i * SIZE*1.1/10), SIZE*2.4/10, SIZE*1.1/10, SIZE*9/10)
            b_zone_contact.append(tmp)

        for i in range (7):
            if b_zone_contact[i].collidepoint(event.pos):
                num_colonne = i

    return num_colonne


def lancer_affichage():
    pygame.init()
    pygame.display.set_caption('Puissance 4')  
    fenetre = pygame.display.set_mode() 
    LONG, LARG = fenetre.get_size() 
    global SIZE 
    SIZE= int(LARG*0.95)
    print("SIZE =", SIZE)
    fenetre = pygame.display.set_mode((SIZE, SIZE))
    #init une grille à zero
    cls_grille = Gestion_grille.Grille(6,7)
    running = True
    quel_menu = MENU_PRINCIPAL
    nom_fichier = ""
    mode_de_jeu = 0
    qui_commence = 2
    niveau_de_difficulte = -1
    texte_fin_de_partie = ""

    while running:
        if quel_menu == MENU_PRINCIPAL:
            nom_fichier = ""
            cls_grille = Gestion_grille.Grille(6,7)
            #print("nom_fichier =", nom_fichier)
            quel_menu = affichage_menu_principal(fenetre)
            
        elif quel_menu == MODE_DE_JEU:
            
            quel_menu, mode_de_jeu, qui_commence, niveau_de_difficulte = affichage_mode_de_jeu(fenetre)
                    
        elif quel_menu == CHARGEMENT: 
            quel_menu, nom_fichier = affichage_chargement(fenetre)
            #print("nom_fichier =", nom_fichier)
            # Grille à afficher ici ou dans quel_menu == PARTIE?
            
            if quel_menu == MODE_DE_JEU:
                resultat = chargement(nom_fichier)
                if type(resultat) is bool:
                    affichage_erreur(fenetre, "Le fichier {} n'a pas pu être chargé".format(nom_fichier))
                    quel_menu = CHARGEMENT
                else:
                    cls_grille = resultat[1]

            #print("quel_menu = ",quel_menu)
        elif quel_menu == PARTIE: 
            # afficher_grille(cls_grille.grille)
            # print("quel_menu =", quel_menu)
            # print("mode_de_jeu =", mode_de_jeu)
            # print("difficulté =", niveau_de_difficulte)
            # print("qui_commence =", qui_commence)
            quel_menu = FIN_DE_PARTIE
            texte_fin_de_partie = affichage_partie(fenetre, cls_grille, mode_de_jeu, qui_commence, niveau_de_difficulte)
        elif quel_menu == FIN_DE_PARTIE:
            quel_menu = affichage_fin_de_partie(fenetre, texte_fin_de_partie)
            nom_fichier = ""
            cls_grille.vider_grille()
            Gestion_jeton.Jeton.reinitialise_nombre_jeton()
        
        else : break

