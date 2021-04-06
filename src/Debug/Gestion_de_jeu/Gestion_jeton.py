class Jeton:
    """
        Cette classe nous permet de créer les jetons qui seront placés
        dans la grille.

        La variable nombre_jeton est de type entier et nous permet de connaitre
        le nombre de jetons utilisés dans la partie.
    """
    
    nombre_jeton = 0

    def __init__(self, j_couleur):
        """ 
            Constructeur de la classe Jeton.
            Permet de créer un jeton en lui assignant une couleur

            Paramètre:
            j_couleur: variable de type booléen
                        0 représente la couleur Jaune
                        1 représente la couleur Rouge
        """
        self.couleur = j_couleur
        Jeton.incremente_nombre_jeton()

    def incremente_nombre_jeton(cls):
        """ Méthode de classe permettant d'incrémenter le nombre de jetons """
        cls.nombre_jeton += 1

    incremente_nombre_jeton = classmethod(incremente_nombre_jeton)

    def decremente_nombre_jeton(cls):
        """ Méthode de classe permettant de décrémenter le nombre de jetons """
        cls.nombre_jeton -= 1

    decremente_nombre_jeton = classmethod(decremente_nombre_jeton)

    def reinitialise_nombre_jeton(cls):
        """ Méthode de classe permettant de remettre le nombre de jetons à 0 """
        cls.nombre_jeton = 0

    reinitialise_nombre_jeton = classmethod(reinitialise_nombre_jeton)
