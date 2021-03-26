class Jetons:
    """
        Commentaire sur la classe
    """
    
    nombre_jeton = 0

    def __init__(self, j_couleur):
        """ Commentaire sur la méthode """
        self.couleur = j_couleur

    def incremente_nombre_jeton(cls):
        """ Commentaire sur la méthode """
        cls.nombre_jeton += 1

    incremente_nombre_jeton = classmethod(incremente_nombre_jeton)