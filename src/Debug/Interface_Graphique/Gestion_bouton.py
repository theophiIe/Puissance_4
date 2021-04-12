import pygame

class Bouton:
    def __init__(self, b_image, b_image_survole, b_position_x, b_position_y, b_largeur, b_hauteur):
        
        self.point_x = b_position_x
        self.point_y = b_position_y

        self.rectangle = pygame.Rect(b_position_x, b_position_y, b_largeur, b_hauteur)

        self.chargement_image = pygame.image.load(b_image)
        self.image = pygame.transform.scale(self.chargement_image,(int(b_largeur), int(b_hauteur)))
        
        self.chargement_image_survole = pygame.image.load(b_image_survole)
        self.image_survole = pygame.transform.scale(self.chargement_image_survole,(int(b_largeur), int(b_hauteur)))


    def changement_taille_bouton(self, b_position_x, b_position_y, b_largeur, b_hauteur):
        
        self.point_x = b_position_x
        self.point_y = b_position_y

        self.rectangle = pygame.Rect(b_position_x, b_position_y, b_largeur, b_hauteur)

        self.image = pygame.transform.scale(self.chargement_image,(int(b_largeur), int(b_hauteur)))
        
        self.image_survole = pygame.transform.scale(self.chargement_image_survole,(int(b_largeur), int(b_hauteur)))


    def affichage_bouton(self, b_fenetre):
        WHITE = pygame.Color("white")
        pygame.draw.rect(b_fenetre, WHITE, self.rectangle, 1)
        b_fenetre.blit(self.image, (self.point_x, self.point_y) )

    def affichage_bouton_survole(self, b_fenetre):
        b_fenetre.blit(self.image_survole, (self.point_x, self.point_y) )

    def collision_bouton(self, b_fenetre, position_souris):
        collision = self.rectangle.collidepoint(position_souris)

        if collision:
            self.affichage_bouton_survole(b_fenetre)
        else:
            self.affichage_bouton(b_fenetre)

    

    
