assert calculer_taille(None) == 0, "Erreur : La taille d'un arbre vide (None) doit être 0."

# Racine seule
racine_solo = Noeud(10)
assert calculer_taille(racine_solo) == 1, (
    "Erreur : Un arbre avec uniquement la racine doit avoir une taille de 1."
)

# Arbre à 3 nœuds
arbre_3 = Noeud(10, Noeud(5), Noeud(15))
assert calculer_taille(arbre_3) == 3, "Erreur : Cet arbre contient 3 nœuds."

# Arbre déséquilibré à 4 nœuds
arbre_4 = Noeud(10, Noeud(5, Noeud(2)), Noeud(15))
assert calculer_taille(arbre_4) == 4, "Erreur : Cet arbre contient 4 nœuds."
