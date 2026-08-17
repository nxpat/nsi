def somme_liste(L):
    if L == []:
        return 0
    else:
        return L[0] + somme_liste(L[1:])
