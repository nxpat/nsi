class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit


def calculer_taille(noeud):
    if noeud is None:
        return 0
    else:
        # À compléter : 1 + taille sous-arbre gauche + taille sous-arbre droit
        return ...
