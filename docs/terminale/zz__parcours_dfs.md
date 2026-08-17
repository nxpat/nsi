# Implémentation d'un parcours en profondeur (DFS) en Python

L'implémentation du parcours en profondeur (**DFS** pour *Depth-First Search*) peut se faire de deux manières principales : par la **récursivité** (la plus naturelle) ou de façon **itérative** en utilisant une **pile**.

### 1. Implémentation récursive
C'est la méthode privilégiée car elle utilise implicitement la pile d'exécution du langage. L'algorithme explore une branche jusqu'au bout (jusqu'à un "cul-de-sac") avant de remonter pour explorer les autres voisins.

Voici une implémentation :

```python
def parcours_profondeur_recursif(racine):
    """Initialise le parcours et le dictionnaire des sommets visités"""
    deja_explore = { racine: True }
    print(racine) # Traitement du sommet racine
    _parcours_profondeur_recursif(racine, deja_explore)

def _parcours_profondeur_recursif(s, deja_explore):
    """Fonction récursive d'exploration"""
    for v in voisins(s): # On parcourt les voisins du sommet actuel
        if v not in deja_explore.keys():
            # Traitement du sommet v (ex: print)
            print(v)
            deja_explore[v] = True
            # Appel récursif pour aller plus profondément
            _parcours_profondeur_recursif(v, deja_explore)
```

### 2. Implémentation itérative (avec une Pile)
Si on ne souhaite pas utiliser la récursivité (pour éviter de saturer la pile d'exécution sur de très grands graphes), on peut utiliser une structure de données de type **pile (LIFO - Last In First Out)**.

*   **Principe :** Contrairement au BFS qui utilise une file (FIFO), le DFS itératif utilise une pile. On ajoute les voisins à la pile et on récupère toujours le **dernier ajouté** pour continuer l'exploration, ce qui force l'algorithme à s'enfoncer dans le graphe.

### 3. Points clés à retenir

*   **Marquage des sommets :** Il est crucial d'utiliser un dictionnaire (ou un tableau de booléens) pour enregistrer les sommets déjà visités afin d'éviter les boucles infinies dans les graphes contenant des cycles.

*   **Applications :** Le DFS est particulièrement utile pour détecter la présence de **cycles**, tester la **connexité** d'un graphe ou résoudre des puzzles comme les **labyrinthes**.

*   **Différence avec BFS :** Alors que le BFS explore par "générations" de distance, le DFS privilégie la distance maximale par rapport à l'origine avant de revenir en arrière.