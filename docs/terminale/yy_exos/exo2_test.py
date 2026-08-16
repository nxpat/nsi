# Construction de l'ABR :
#        10
#       /  \
#      5    15
#     / \
#    2   7
abr = Noeud(10, Noeud(5, Noeud(2), Noeud(7)), Noeud(15))

assert chercher(None, 10) is False, "Erreur : Recherche dans un arbre vide doit renvoyer False."
assert chercher(abr, 10) is True, "Erreur : La racine 10 doit être trouvée."
assert chercher(abr, 7) is True, "Erreur : La clé 7 est présente dans l'ABR."
assert chercher(abr, 15) is True, "Erreur : La clé 15 est présente dans l'ABR."
assert chercher(abr, 3) is False, "Erreur : La clé 3 n'existe pas dans l'ABR."
assert chercher(abr, 20) is False, "Erreur : La clé 20 n'existe pas dans l'ABR."
