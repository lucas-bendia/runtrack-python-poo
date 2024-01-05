class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for valeur in range(1, 14) for couleur in ['Coeur', 'Carreau', 'Trefle', 'Pique']]

    def distribuer_carte(self):
        return self.paquet.pop()

    def jouer(self):
        joueur = [self.distribuer_carte(), self.distribuer_carte()]
        croupier = [self.distribuer_carte(), self.distribuer_carte()]

        while True:
            print("Votre main:", [(carte.valeur, carte.couleur) for carte in joueur])
            choix = input("Voulez-vous prendre une autre carte? (O/N) ")
            if choix.lower() == 'o':
                joueur.append(self.distribuer_carte())
                # Vérifiez si le joueur a dépassé 21
                if sum(carte.valeur for carte in joueur) > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    return
            else:
                break

        while sum(carte.valeur for carte in croupier) < 17:
            croupier.append(self.distribuer_carte())

        print("Main du croupier:", [(carte.valeur, carte.couleur) for carte in croupier])
        if sum(carte.valeur for carte in croupier) > 21:
            print("Le croupier a dépassé 21. Vous avez gagné.")
        elif sum(carte.valeur for carte in joueur) > sum(carte.valeur for carte in croupier):
            print("Vous avez gagné.")
        else:
            print("Le croupier a gagné.")

jeu = Jeu()
jeu.jouer()
