nom_erreur = "TypeError"


def division(a, b):
    assert isinstance(b, (int, float)) and b != 0, "b doit être un nombre non nul"
    return a / b
