class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA/100)

    def afficher(self):
        return f'Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}, Prix TTC: {self.CalculerPrixTTC()}'

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

# Créer quelques produits
produit1 = Produit('Produit 1', 100, 20)
produit2 = Produit('Produit 2', 200, 15)

# Calculer leurs prix avec la TVA
print(produit1.CalculerPrixTTC())
print(produit2.CalculerPrixTTC())

# Modifier le nom et le prix de chaque produit
produit1.modifier_nom('Nouveau Produit 1')
produit1.modifier_prix(150)
produit2.modifier_nom('Nouveau Produit 2')
produit2.modifier_prix(250)

# Afficher les nouveaux prix des produits
print(produit1.afficher())
print(produit2.afficher())
