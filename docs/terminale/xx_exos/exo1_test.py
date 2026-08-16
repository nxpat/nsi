from math import inf

assert rendu_monnaie_it([1, 2, 5], 11) == 3, (
    "Erreur : Pour 11 avec [1, 2, 5], le résultat doit être 3 pièces (5 + 5 + 1)."
)
assert rendu_monnaie_it([1, 2, 5], 0) == 0, "Erreur : Pour une somme de 0, la réponse doit être 0."
assert rendu_monnaie_it([1, 3, 4], 6) == 2, (
    "Erreur : Pour 6 avec [1, 3, 4], l'optimum est 2 pièces (3 + 3)."
)
assert rendu_monnaie_it([2, 5], 3) == inf, (
    "Erreur : Si la somme ne peut pas être rendue, la fonction doit renvoyer inf."
)
