# Détection de cycles

La détection de cycles dans un graphe repose principalement sur l'utilisation de l'algorithme de **parcours en profondeur (DFS)**.

Voici les principes fondamentaux pour y parvenir selon les sources :

### 1. Définition du cycle
Un cycle est une **chaîne simple fermée**, c'est-à-dire un chemin dont les sommets de départ et d'arrivée sont identiques et où toutes les arêtes (ou arcs) sont distinctes. Dans un graphe orienté, on parle plus spécifiquement de **circuit**.

### 2. Méthode par parcours en profondeur (DFS)
L'algorithme DFS permet de s'enfoncer dans une branche du graphe. La détection d'un cycle survient lorsqu'on rencontre un sommet **déjà exploré** au cours du parcours actuel.

#### Pour un graphe non orienté :
Il faut être vigilant à ne pas considérer un simple aller-retour entre deux sommets liés (A → B puis B → A) comme un cycle.

*   **Principe :** On marque chaque sommet visité.
*   **Condition de détection :** Si, lors de l'exploration d'un voisin, on tombe sur un sommet déjà marqué qui **n'est pas le parent direct** (le sommet d'où l'on vient), alors un cycle est détecté.

#### Pour un graphe orienté (circuit) :

*   **Condition de détection :** On détecte un circuit si l'on rencontre un sommet qui est **en cours de visite** (c'est-à-dire présent dans la pile d'exécution de la récursivité).

### 3. Exemple d'implémentation en Python
Avec une fonction récursive de détection :

```python
visites = {}

def trouver_cycle(graphe, sommet, depuis=None):
    """
    Détecte un cycle dans un graphe non orienté.
    'depuis' permet d'ignorer le sommet parent direct.
    """
    visites[sommet] = True
    for voisin in graphe[sommet]:
        if voisin not in visites:
            if trouver_cycle(graphe, voisin, sommet):
                return True
        elif voisin != depuis:
            # On a trouvé un sommet déjà visité qui n'est pas le parent direct
            return True
    return False
```

**Points clés à retenir :**

*   L'utilisation d'un **dictionnaire ou d'un tableau** pour marquer les sommets visités est indispensable pour éviter les boucles infinies et identifier les retours sur des sommets déjà connus.

*   Le parcours en largeur (BFS) est moins adapté à cette tâche spécifique car il explore par "générations" de distance plutôt que par branches profondes.