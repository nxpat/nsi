# Vérification de la présence d'une docstring
doc = calcule_aire_rectangle.__doc__
assert doc is not None and len(doc.strip()) > 15, (
    "N'oubliez pas de rédiger une docstring explicative dans la fonction."
)

# Test du calcul correct
assert calcule_aire_rectangle(5, 3) == 15, "calcule_aire_rectangle(5, 3) devrait valoir 15."
assert calcule_aire_rectangle(2.5, 4) == 10.0, "calcule_aire_rectangle(2.5, 4) devrait valoir 10.0."

# Vérification des préconditions (longueur ou largeur <= 0 doivent lever une AssertionError)
try:
    calcule_aire_rectangle(0, 5)
    assert False, "Une longueur égale à 0 aurait dû lever une AssertionError."
except AssertionError:
    pass

try:
    calcule_aire_rectangle(5, -2)
    assert False, "Une largeur négative (-2) aurait dû lever une AssertionError."
except AssertionError:
    pass
