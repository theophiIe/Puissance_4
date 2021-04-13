import pygame

class Bouton:
    def __init__(self, b_image, b_image_survole, b_position_x, b_position_y, b_largeur, b_hauteur):
        """
            Cette méthode est le constructeur de la classe Bouton qui permet de créer les boutons.
            Pour de la saisie des positions sur les axes x et y du bouton, le point (0,0) est situé en haut à gauche.
            De plus, les coordonnées x et y correspondent au point situé en haut à gauche du bouton.
            
            Paramètres : 
                b_image : chaîne de caractères qui correspond au chemin de l'image affichée dans le bouton
                b_image_survole : chaîne de caractères qui correspond au chemin de l'image affichée dans le bouton lorsqu'il est survolé
                b_position_x : entier qui définit la position en abscisse du bouton
                b_position_y : entier qui définit la position en ordonnée du bouton
                b_largeur : entier qui correpond à la largeur du bouton, en pixels
                b_hauteur : entier qui correspond à la hauteur du bouton, en pixels
            
            Cette fonction ne renvoie rien.
        """
        self.point_x = b_position_x
        self.point_y = b_position_y

        self.rectangle = pygame.Rect(b_position_x, b_position_y, b_largeur, b_hauteur)

        self.chargement_image = pygame.image.load(b_image)
        self.image = pygame.transform.scale(self.chargement_image,(int(b_largeur), int(b_hauteur)))
        
        self.chargement_image_survole = pygame.image.load(b_image_survole)
        self.image_survole = pygame.transform.scale(self.chargement_image_survole,(int(b_largeur), int(b_hauteur)))


        
    def changement_taille_bouton(self, b_position_x, b_position_y, b_largeur, b_hauteur):
        """
            Cette méthode permet de changer les dimensions du rectangle ainsi que 
            celles des deux images présentes dans le bouton dans certains cas.
            Cette fonction est utilisée lorsque la fenêtre est redimensionnée. 

            Paramètres : 
                b_position_x : entier qui définit la position en abscisse du bouton
                b_position_y : entier qui définit la position en ordonnée du bouton
                b_largeur : entier qui correpond à la largeur du bouton, en pixels
                b_hauteur : entier qui correspond à la hauteur du bouton, en pixels
            
            Cette méthode ne renvoie rien.
            
        """
        self.point_x = b_position_x
        self.point_y = b_position_y

        self.rectangle = pygame.Rect(b_position_x, b_position_y, b_largeur, b_hauteur)

        self.image = pygame.transform.scale(self.chargement_image,(int(b_largeur), int(b_hauteur)))
        
        self.image_survole = pygame.transform.scale(self.chargement_image_survole,(int(b_largeur), int(b_hauteur)))


    def affichage_bouton(self, b_fenetre):
        """
            Cette méthode permet d'afficher le bouton dans la fenêtre graphique passée en paramètre.
            
            Paramètre : 
                b_fenetre : instance de la fenetre graphique où ajouter le bouton
                        
            Cette méthode ne renvoie rien.
        """
        
        b_fenetre.blit(self.image, (self.point_x, self.point_y) )

    def affichage_bouton_survole(self, b_fenetre):
        """
            Cette méthode modifie l'image du bouton qui est survolé par la souris.
            
            Paramètre : 
                b_fenetre : instance de la fenetre graphique où ajouter le bouton
                        
            Cette méthode ne renvoie rien.
        """
        
        b_fenetre.blit(self.image_survole, (self.point_x, self.point_y) )

    def collision_bouton(self, b_fenetre, b_position_souris):
        """
            Cette méthode permet de récupérer constamment la position de la souris et vérifie 
            si le curseur pointe sur le bouton ou non.
            Le paramètre position_souris correspond à la valeur retournée par la fonction pygame.mouse.get_pos()
            Cette valeur est sous la forme d'un tuple d'entiers qui correspond aux coordonnées en abscisse et 
            ordonnée de la souris à l'instant présent. 
            
            Paramètre : 
                b_fenetre : instance de la fenetre graphique où ajouter le bouton
                b_position_souris : tuple d'entiers avec les coordonnées de la souris
                
            Cette méthode ne renvoie rien.
        """
        collision = self.rectangle.collidepoint(b_position_souris)

        if collision:
            self.affichage_bouton_survole(b_fenetre)
        else:
            self.affichage_bouton(b_fenetre)

    

    
