def recherche_naive(texte, motif):
    n = len(texte)
    m = len(motif)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if texte[i + j] != motif[j]:
                match = False
                break
        if match:
            return i
    return None
