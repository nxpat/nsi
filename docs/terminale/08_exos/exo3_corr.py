parcours_A = [5, 2, 8, 10, 15]
parcours_B = [2, 5, 8, 10, 15]

reponse = "B"


def est_triee(liste):
    for i in range(len(liste) - 1):
        if liste[i] >= liste[i + 1]:
            return False
    return True
