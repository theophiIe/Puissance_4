import sys
sys.path.append('src/Gestion_de_jeu')
sys.path.append('src/Interface_Graphique')
sys.path.append('data/Liste_sauvegardes')
sys.path.append('src/Sauvegarde_et_Chargement')
sys.path.append('src/Strategies')

from Gestion_interface import *
programIcon = pygame.image.load('assets\sprites\logo.png')
pygame.display.set_icon(programIcon)
lancer_affichage()