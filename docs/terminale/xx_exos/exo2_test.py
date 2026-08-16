assert recherche_naive("algorithmes avancés", "avance") == 13, (
    "Échec : 'avance' commence à l'indice 13."
)
assert recherche_naive("python", "th") == 2, "Échec : 'th' commence à l'indice 2 dans 'python'."
assert recherche_naive("python", "java") is None, (
    "Échec : Doit renvoyer None si le motif n'est pas trouvé."
)
assert recherche_naive("abc", "abc") == 0, "Échec : Si motif == texte, renvoyer 0."
assert recherche_naive("abc", "abcd") is None, (
    "Échec : Doit renvoyer None si le motif est plus long que le texte."
)
assert recherche_naive("aaaaa", "aa") == 0, (
    "Échec : Doit renvoyer l'indice de la première occurrence."
)
