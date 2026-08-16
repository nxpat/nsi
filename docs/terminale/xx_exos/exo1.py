from math import inf


def rendu_monnaie_it(valeurs, somme):
    # f[s] représente le nombre minimal de pièces pour former la somme s
    # Initialisation : f[0] = 0 et inf pour les autres sommes
    f = [0] + [inf] * somme

    for s in range(1, somme + 1):
        for x in valeurs:
            if s >= x:
                # À compléter : mise à jour de f[s] avec le minimum de pièces
                ...

    return f[somme]
