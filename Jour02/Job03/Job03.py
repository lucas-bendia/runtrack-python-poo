class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True

    # Accessors
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    # Mutators
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    # Méthodes supplémentaires
    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Erreur : Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
        else:
            print("Erreur : Le livre n'a pas été emprunté.")

# Interagir avec l'utilisateur
titre = input("Entrez le titre du livre : ")
auteur = input("Entrez l'auteur du livre : ")
nombre_de_pages = int(input("Entrez le nombre de pages du livre : "))

# Créer un livre
livre = Livre(titre, auteur, nombre_de_pages)

# Afficher les détails du livre
print("Titre : ", livre.get_titre())
print("Auteur : ", livre.get_auteur())
print("Nombre de pages : ", livre.get_nombre_de_pages())

# Emprunter le livre
livre.emprunter()

# Vérifier si le livre est disponible
if livre.verification():
    print("Le livre est disponible.")
else:
    print("Le livre n'est pas disponible.")

# Rendre le livre
livre.rendre()

# Vérifier à nouveau si le livre est disponible
if livre.verification():
    print("Le livre est disponible.")
else:
    print("Le livre n'est pas disponible.")
