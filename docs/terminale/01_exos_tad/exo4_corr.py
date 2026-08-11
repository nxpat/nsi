class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        return self.elements.pop()

    def est_vide(self):
        return len(self.elements) == 0


def verifier_parentheses(expression):
    p = Pile()
    for char in expression:
        if char == "(":
            p.empiler(char)
        elif char == ")":
            if p.est_vide():
                return False  # On essaie de fermer une parenthèse jamais ouverte
            p.depiler()

    # L'expression est correcte seulement s'il ne reste
    # plus de parenthèses ouvertes non fermées
    return p.est_vide()
