# Test 1 : Vérification de l'initialisation
try:
    p1 = Personnage("Gollum", 10)
except TypeError:
    raise AssertionError("Le constructeur doit accepter exactement deux paramètres : nom et pv.")

assert hasattr(p1, "nom"), "L'attribut 'nom' n'a pas été créé dans le constructeur."
assert hasattr(p1, "pv"), "L'attribut 'pv' n'a pas été créé dans le constructeur."
assert p1.nom == "Gollum", "L'attribut 'nom' est mal initialisé."
assert p1.pv == 10, "L'attribut 'pv' est mal initialisé."

# Test 2 : Vérification de la méthode est_vivant
assert p1.est_vivant() == True, "La méthode est_vivant() doit renvoyer True quand pv > 0."

p2 = Personnage("Squelette", 0)
assert p2.est_vivant() == False, "La méthode est_vivant() doit renvoyer False quand pv = 0."

p3 = Personnage("Fantôme", -5)
assert p3.est_vivant() == False, "La méthode est_vivant() doit renvoyer False quand pv < 0."
