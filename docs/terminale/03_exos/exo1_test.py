assert nom_erreur.strip() == "TypeError", (
    "Erreur Q1 : Effectuer '10 / \"2\"' tente de diviser un int par un str, ce qui lève une TypeError."
)

# Test du fonctionnement normal
assert division(10, 2) == 5.0, "La division 10 / 2 devrait retourner 5.0."

# Test que l'assertion bloque les chaînes de caractères
try:
    division(10, "2")
    assert False, "L'assertion aurait dû bloquer l'argument '2' (chaine de caractères)."
except AssertionError:
    pass

# Test que l'assertion bloque la division par zéro
try:
    division(10, 0)
    assert False, "L'assertion aurait dû bloquer b = 0."
except AssertionError:
    pass
