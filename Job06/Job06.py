class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        print(f"L'âge de l'animal est {self.age} ans")

    def nommer(self, nom):
        self.prenom = nom
        print(f"L’animal se nomme {self.prenom}")

# Création d'un animal
animal = Animal()

# Affichage de l'âge initial
animal.vieillir()

# Nommer l'animal et afficher son nom
animal.nommer("Luna")
