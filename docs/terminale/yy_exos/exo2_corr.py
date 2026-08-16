class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit


def chercher(noeud, x):
    if noeud is None:
        return False
    if noeud.valeur == x:
        return True
    if x < noeud.valeur:
        return chercher(noeud.gauche, x)
    else:
        return chercher(noeud.droit, x)
