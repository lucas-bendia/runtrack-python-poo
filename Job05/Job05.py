class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return f"Les coordonnées du point sont ({self.x}, {self.y})"

    def afficherX(self):
        return f"La coordonnée x du point est {self.x}"

    def afficherY(self):
        return f"La coordonnée y du point est {self.y}"

    def changerX(self, newX):
        self.x = newX

    def changerY(self, newY):
        self.y = newY

# Création d'un point
point = Point(2, 3)

# Appel des méthodes
print(point.afficherLesPoints())
print(point.afficherX())
print(point.afficherY())

# Changement des coordonnées
point.changerX(5)
point.changerY(7)

print(point.afficherLesPoints())
