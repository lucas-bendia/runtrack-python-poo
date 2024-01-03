class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseurs
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Créer un rectangle avec longueur 10 et largeur 5
rect = Rectangle(10, 5)

# Changer la valeur de la longueur et de la largeur
rect.set_longueur(20)
rect.set_largeur(10)

# Vérifier que les modifications soient bien prises en compte
print(rect.get_longueur())  # Affiche : 20
print(rect.get_largeur())  # Affiche : 10
