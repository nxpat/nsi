class Personnage:
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv

    def est_vivant(self):
        return self.pv > 0
