class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def ajouter_population(self):
        self.__population += 1

    def afficher_population(self):
        print(f"La population de {self.__nom} est {self.__population}")


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_population()


# Créer un objet Ville pour Paris avec une population initiale de 1000000
paris = Ville("Paris", 1000000)
paris.afficher_population()  # Affiche la population de Paris

# Créer un autre objet Ville pour Marseille avec une population initiale de 861635
marseille = Ville("Marseille", 861635)
marseille.afficher_population()  # Affiche la population de Marseille

# Ajouter trois personnes à Paris
personne1 = Personne("Jean", 30, paris)
personne2 = Personne("Marie", 25, paris)
personne3 = Personne("Paul", 35, paris)

# Affiche la nouvelle population de Paris
paris.afficher_population()
