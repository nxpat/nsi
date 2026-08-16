from math import inf


def rendu_monnaie_it(valeurs, somme):
    f = [0] + [inf] * somme
    for s in range(1, somme + 1):
        for x in valeurs:
            if s >= x:
                f[s] = min(f[s], 1 + f[s - x])
    return f[somme]
