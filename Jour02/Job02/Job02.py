class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    # Accesseurs
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    # Mutateurs
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

# Créer un livre
livre = Livre("Titre", "Auteur", 100)

# Changer la valeur du nombre de pages
livre.set_nombre_de_pages(200)

# Vérifier que les modifications soient bien prises en compte
print(livre.get_nombre_de_pages())  # Affiche : 200
