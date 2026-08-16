# Focus : L'algorithme de Boyer-Moore (Horspool)

L'algorithme de Boyer-Moore repose sur deux idées fondamentales qui lui permettent d'éviter de lire tous les caractères du texte, le rendant parfois **sous-linéaire** (complexité estimée à $(O(n/p)$ dans les cas favorables).

## 1. Comparaison de droite à gauche
Contrairement à l'approche naïve, on aligne le motif sur une fenêtre du texte et on commence la comparaison par le **dernier caractère du motif** (à l'index $j = p-1$) en remontant vers la gauche. Si une différence est détectée dès le début, on peut décaler le motif sans avoir testé les autres caractères de la fenêtre.

## 2. La règle du mauvais caractère (Sauts intelligents)
Lorsqu'un caractère du texte (appelons-le `x`) ne correspond pas au caractère du motif, on effectue un décalage calculé grâce à un **prétraitement** du motif :

*   **Si `x` n'est pas dans le motif :** On peut décaler le motif entièrement après la position de ce caractère `x`.
*   **Si `x` est présent dans le motif :** On décale le motif pour aligner sa **dernière occurrence** (la plus à droite avant la position actuelle) avec le caractère `x` du texte.
*   **Sécurité :** Si le calcul donne un décalage nul ou négatif, on avance par défaut d'une seule case.

## 3. Implémentation Python
Le prétraitement consiste à créer un dictionnaire stockant la position la plus à droite de chaque caractère du motif.

```python
def calculer_positions(motif):
    """Prétraitement : dictionnaire des dernières occurrences"""
    dico = {}
    for j in range(len(motif)):
        dico[motif[j]] = j
    return dico

def correspondance(texte, motif, p, i, dico_droite):
    """Compare de droite à gauche et renvoie le décalage"""
    # j varie de p-1 à 0 en décroissant
    for j in range(p - 1, -1, -1):
        x = texte[i + j]
        if x != motif[j]:
            # Règle du mauvais caractère : calcul du saut
            derniere_pos = dico_droite.get(x, -1)
            decalage = max(1, j - derniere_pos)
            return False, decalage
    return True, 0

def cherche_boyer_moore(texte, motif):
    n, p = len(texte), len(motif)
    dico_droite = calculer_positions(motif)
    i = 0
    while i + p <= n:
        ok, decalage = correspondance(texte, motif, p, i, dico_droite)
        if ok:
            return i # Trouvé !
        i += decalage
    return -1
```

### Avantages et Efficacité

*   **Efficacité spatiale :** Le dictionnaire ne dépend que de la taille du motif et de l'alphabet utilisé.
*   **Vitesse :** Plus le motif est long, plus les sauts sont potentiellement grands, ce qui rend l'algorithme extrêmement efficace pour chercher dans des romans entiers (ex: chercher "Julien trembla" dans *Le Rouge et le Noir*).
*   **Complexité :** Dans le pire cas (très rare), elle reste de $O(p(n-p))$, mais en pratique, elle est bien meilleure que la recherche naïve.