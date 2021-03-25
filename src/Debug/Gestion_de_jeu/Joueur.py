
class Joueur:
    """
        Commentaire sur la classe
    """

    def __init__(self, j_commence):
        """ Commentaire sur le constructeur """
        self.commence = j_commence

class Ordinateur(Joueur):
    """
        Commentaire sur la classe
    """

    def __init__(self, o_commence, o_difficulte):
        """
            Constructeur de la classe Ordinateur
            Fait appel au constrcuteur de la classe Joueur
            et permet d'assigner un niveau de difficulté à l'ordinateur
        """
        Joueur.__init__(o_commence)
        self.difficulte = o_difficulte
