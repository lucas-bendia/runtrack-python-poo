class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = reservoir

    # Mutateurs
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    # Accesseurs
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Le réservoir est vide, veuillez le remplir.")

    def arreter(self):
        self.__en_marche = False

    # Méthode privée
    def __verifier_plein(self):
        return self.__reservoir

def menu():
    voiture = Voiture("Audi", "Q3", 2022, 15000)
    while True:
        print("\n1. Démarrer la voiture")
        print("2. Arrêter la voiture")
        print("3. Afficher les informations de la voiture")
        print("4. Quitter")
        choix = input("Choisissez une option : ")
        if choix == "1":
            voiture.demarrer()
        elif choix == "2":
            voiture.arreter()
        elif choix == "3":
            print(f"Marque : {voiture.get_marque()}")
            print(f"Modèle : {voiture.get_modele()}")
            print(f"Année : {voiture.get_annee()}")
            print(f"Kilométrage : {voiture.get_kilometrage()}")
        elif choix == "4":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

menu()
