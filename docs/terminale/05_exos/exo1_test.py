assert somme_liste([]) == 0, "Erreur : La somme d'une liste vide doit être 0."
assert somme_liste([5]) == 5, "Erreur : La somme de [5] doit valoir 5."
assert somme_liste([1, 2, 3, 4, 5]) == 15, "Erreur : La somme de [1, 2, 3, 4, 5] doit valoir 15."
assert somme_liste([-2, 3, 10]) == 11, "Erreur : La fonction doit gérer les nombres négatifs."
