# Comment supprimer un nœud dans un Arbre Binaire de Recherche (ABR)

La suppression d'un nœud dans un **Arbre Binaire de Recherche (ABR)** est une opération plus complexe que l'insertion, car elle nécessite de maintenir la propriété de tri de l'arbre : pour chaque nœud, les valeurs à gauche sont inférieures et celles à droite sont supérieures.

L'algorithme se décompose généralement en **trois cas de figure** selon la structure du nœud à supprimer :

### 1. Le nœud est une feuille
C'est le cas le plus simple. Si le nœud n'a aucun fils, on le supprime simplement en le remplaçant par une valeur vide (`None` ou `null`) dans son nœud parent.

### 2. Le nœud possède un seul fils
Si le nœud à supprimer n'a qu'un seul descendant (soit à gauche, soit à droite), on "saute" ce nœud : on relie directement son parent à son unique fils. Le fils prend alors la place du nœud supprimé dans la structure.

### 3. Le nœud possède deux fils
C'est le cas le plus délicat car on ne peut pas simplement supprimer le nœud sans briser la hiérarchie. Il faut le remplacer par une valeur qui préserve l'ordre de l'arbre. On a alors deux choix possibles :

*   **Le plus grand élément du sous-arbre gauche :** par définition, il est supérieur à tous les autres éléments à gauche et inférieur à tous ceux de droite.

*   **Le plus petit élément du sous-arbre droit :** on cherche la valeur minimale à droite, on remplace la valeur du nœud actuel par celle-ci, puis on supprime de manière récursive ce nœud minimal (qui, lui, sera forcément dans le cas 1 ou 2).

### Implémentation type en Python
Voici comment cette logique est structurée dans une classe `Noeud` :

```python
def supprimer_noeud_courant(self):
    # Cas 1 : Le nœud est une feuille
    if self.est_feuille():
        return None
    # Cas 2 : Le nœud n'a qu'un fils (à droite ou à gauche)
    elif self.noeud_gauche is None:
        return self.noeud_droit
    elif self.noeud_droit is None:
        return self.noeud_gauche
    # Cas 3 : Le nœud a deux fils
    else:
        # On cherche et supprime le min du sous-arbre droit
        (valeur, noeud) = self.noeud_droit.chercher_et_supprimer_min()
        self.valeur = valeur
        self.noeud_droit = noeud
        return self
```

### Complexité et points d'attention

*   **Complexité :** Comme la recherche et l'insertion, la suppression s'effectue en un temps proportionnel à la hauteur de l'arbre, soit **$O(h)$**. Si l'arbre est équilibré, la complexité est logarithmique, soit **$O(\log n)$**.

*   **Éléments absents :** Si la clé à supprimer n'est pas trouvée après avoir parcouru une branche jusqu'à une feuille, l'algorithme ne fait rien.

*   **Hors programme :** cette opération est considérée comme **"hors programme"** de la spécialité NSI en raison de sa complexité technique, contrairement à l'insertion et à la recherche.