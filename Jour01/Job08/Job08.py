import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Rayon: {self.rayon}, Circonférence: {self.circonférence()}, Diamètre: {self.diametre()}, Aire: {self.aire()}")

    def circonférence(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon

# Créer deux cercles avec des rayons de 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Afficher les informations pour chaque cercle
cercle1.afficherInfos()
cercle2.afficherInfos()
