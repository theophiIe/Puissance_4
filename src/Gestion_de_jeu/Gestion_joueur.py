import Gestion_jeton

class Joueur:
    """ Cette classe permet créer un joueur. """

    def __init__(self, j_commence):
        """
            Constructeur de la classe Joueur permettant de créer un joueur
            en indiquant si le joueur commence ou non la partie.

            Paramètre:
                j_commence : variable de type booléenne qui nous permet de savoir si le 
                             joueur commence la partie ou non.
                             1 commence la partie.
                             0 ne commence pas la partie.
        """

        self.commence = j_commence

    def jouer_coup(self, j_grille, j_num_colonne):
        """
            Méthode de la classe permettant de placer le jeton
            dans la grille à la colonne souhaitée par le joueur.

            Paramètres:
                j_grille : matrice de la classe Grille.
                j_num_colonne : variable de type entier positif
                                correspondant à un numéro de colonne
                                de la matrice.
                      
            Renvoie : 
                Cette méthode renvoie un entier correspondant au numéro de la ligne où le coup a été joué.
        """

        num_ligne = 5

        for i in range(0, 6):
            if(j_grille[i][j_num_colonne] is not None):
                num_ligne = i - 1
                break
        
        couleur = 0
        
        if(self.commence):
            couleur = 1
        
        else:
            couleur = 2

        j_grille[num_ligne][j_num_colonne] = Gestion_jeton.Jeton(couleur)

        return num_ligne

class Ordinateur(Joueur):
    """
        La classe Ordinateur est une classe fille de la classe Joueur.
        
        Cette classe est utilisée pour le joueur contrôlé par l'ordinateur.
    """

    def __init__(self, o_commence, o_difficulte):
        """
            Constructeur de la classe Ordinateur. On fait appel au constucteur
            de la classe Joueur et on définit un niveau de difficulté.

            Paramètres:
                o_commence : variable de type booléenne permettant de savoir
                            si l'ordinateur commence la partie.
                            True : commence la partie.
                            False : ne commence pas la partie.
                
                o_difficulte : varible de type entier positif nous permettant de
                               définir le niveau de difficulté de l'ordinateur.
        """

        super().__init__(o_commence)
        self.difficulte = o_difficulte

    def premier_coup(self, o_grille):
        """
            Cette méthode permet de jouer un jeton au centre de la grille
            si l'ordinateur commence la partie.
        """

        self.jouer_coup(o_grille, 3)
