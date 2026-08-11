def calcule_aire_rectangle(longueur, largeur):
    """
    Calcule l'aire d'un rectangle.

    Paramètres :
        longueur (int ou float) : Longueur du rectangle (> 0)
        largeur (int ou float) : Largeur du rectangle (> 0)

    Valeur de retour :
        (int ou float) : L'aire du rectangle
    """
    assert longueur > 0 and largeur > 0, (
        "La longueur et la largeur doivent être strictement positives."
    )
    return longueur * largeur
