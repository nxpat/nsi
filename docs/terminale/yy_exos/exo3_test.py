assert reponse.strip().upper() == "B", (
    "Erreur Q1 : Le parcours infixe d'un ABR donne toujours les clés triées par ordre croissant (Réponse B)."
)

assert est_triee([1, 2, 3, 4]) is True, "Erreur : [1, 2, 3, 4] est triée."
assert est_triee([1, 3, 2, 4]) is False, "Erreur : [1, 3, 2, 4] n'est pas triée."
assert est_triee(parcours_A) is False, "Erreur : Le parcours A n'est pas trié."
assert est_triee(parcours_B) is True, "Erreur : Le parcours B est bien trié."
