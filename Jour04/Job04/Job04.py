# Créer une classe nommée Forme possédant une méthode nommée aire qui renvoie 0.
class Forme:
    def aire(self):
        return 0

# Créer une classe Rectangle qui hérite de la classe Forme et qui possède deux attributs largeur et hauteur.
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Surcharger la méthode aire dans la classe Rectangle afin qu’elle ne renvoie plus 0, mais l’aire du rectangle.
    def aire(self):
        return self.largeur * self.hauteur

# Créer une instance de la classe Rectangle avec une largeur de 5 et une hauteur de 10
rectangle = Rectangle(5, 10)

# Écrire en console le résultat de la méthode aire de la classe Rectangle.
print(rectangle.aire())
