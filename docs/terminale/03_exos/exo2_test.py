assert len(cas_de_tests) >= 3, "Erreur Q1 : Vous devez fournir au moins 3 cas de test."
for t in cas_de_tests:
    assert isinstance(t, tuple) and len(t) == 3 and len(t[1]) == 2, (
        "Chaque cas de test doit être de la forme ('Description', (prix, pourcentage), resultat_attendu)."
    )

assert "limite" in nature_du_cas.lower(), (
    "Erreur Q2 : Tester 100% (ou 0%) permet de tester une 'valeur limite' aux bornes de l'intervalle acceptable."
)
