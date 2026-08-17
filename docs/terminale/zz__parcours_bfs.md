# Implémentation d'un parcours en largeur (BFS) en Python

L'implémentation du parcours en largeur (**BFS** pour *Breadth-First Search*) en Python repose sur l'utilisation d'une structure de données de type **file (FIFO)** pour gérer l'ordre de visite des sommets.

Voici les étapes et le code pour implémenter cet algorithme selon vos sources :

### 1. Structure de données requise
Pour une implémentation efficace, on utilise généralement le module `collections.deque` pour créer la file, car il permet des ajouts et des retraits rapides aux extrémités. On utilise également un système pour marquer les sommets déjà rencontrés (par exemple des couleurs ou un dictionnaire) afin d'éviter de tourner en rond dans les circuits.

### 2. Exemple d'implémentation (Parcours complet)
Le code suivant réalise un parcours en largeur à partir d'un sommet d'origine et renvoie un tableau de `provenance`, utile pour reconstituer les chemins :

```python
from collections import deque

# Définition des états (couleurs)
BLANC = 0  # Sommet non exploré
BLEU = 1   # Sommet à explorer (la frontière)
ROUGE = 2  # Sommet exploré

def parcours_largeur(adj):
    """
    Effectue un parcours en largeur sur un graphe représenté par
    une liste d'adjacence 'adj'.
    """
    n = len(adj)
    provenance =  * n
    couleur = [BLANC] * n
    
    # Initialisation avec le premier sommet (indice 0)
    couleur = BLEU
    file = deque()
    
    while len(file) > 0:
        k = file.popleft() # Retrait du plus ancien (FIFO)
        couleur[k] = ROUGE
        
        for j in adj[k]: # Exploration des voisins
            if couleur[j] == BLANC:
                couleur[j] = BLEU
                provenance[j] = k # On mémorise le père
                file.append(j)
                
    return provenance
```

### 3. Points clés de l'algorithme

*   **Fonctionnement par générations :** L'algorithme visite d'abord le sommet origine, puis tous ses voisins directs (distance 1), puis les voisins de ses voisins (distance 2), et ainsi de suite.

*   **Plus court chemin :** Le BFS garantit de trouver le **chemin le plus court** en nombre d'étapes (nombre d'arêtes traversées) entre le départ et n'importe quel autre sommet.

*   **Reconstitution du chemin :** Grâce au tableau `provenance`, il suffit de remonter de "père en père" depuis le sommet d'arrivée pour retrouver l'itinéraire complet.

### 4. Utilisation pour trouver un chemin spécifique
Si on souhaite simplement trouver un chemin entre deux sommets précis, on peut arrêter la boucle `while` dès que le sommet cible passe à l'état "exploré" (ROUGE).