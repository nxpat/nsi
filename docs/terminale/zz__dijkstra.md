# Algorithme de Dijkstra

L'algorithme de Dijkstra est une méthode permettant de trouver le **chemin le plus court** entre un sommet de départ et tous les autres sommets d'un **graphe pondéré et connexe**. 

Voici les principes fondamentaux de son fonctionnement :

## 1. Conditions préalables et initialisation

*   **Type de graphe :** L'algorithme opère sur un graphe **pondéré** et **connexe**.
*   **Poids positifs :** L'algorithme nécessite que tous les poids des arêtes soient **positifs** pour garantir que le chemin trouvé soit bien le plus court.
*   **Table des poids estimés :** On maintient un tableau (`poids_est`) qui stocke la distance minimale provisoire entre l'origine et chaque sommet.
*   **Valeurs initiales :** Au départ, la distance vers le sommet d'origine est fixée à **0**, et toutes les autres distances sont fixées à **l'infini (∞)**.
*   **File de priorité :** On utilise une structure de données appelée **file de priorité** pour gérer les sommets à explorer. Elle permet d'extraire systématiquement le sommet ayant le poids estimé le plus faible.

## 2. Choix de la structure de données en Python

L'implémentation repose sur le module **`heapdict`**. Contrairement au module standard `heapq`, `heapdict` permet de **modifier la valeur** d'une clé déjà présente dans la file, ce qui est indispensable pour mettre à jour (relâcher) le poids d'un sommet lorsque l'on trouve un chemin plus court.

## 3. Le cycle de l'algorithme
L'algorithme répète les étapes suivantes tant que la file de priorité n'est pas vide :

1.  **Sélection :** On extrait de la file le sommet **$k$** dont la distance estimée depuis l'origine est la **minimale**.
2.  **Exploration (Relâchement) :** Pour chaque voisin **$j$** du sommet $k$, on calcule une nouvelle distance potentielle : 
    $d = \text{poids\_est}[k] + \text{poids}(k, j)$.
3.  **Mise à jour :** Si cette nouvelle distance $d$ est **inférieure** à la distance actuelle enregistrée pour $j$ ($d < \text{poids\_est}[j]$) :
    *   On met à jour `poids_est[j]` avec cette nouvelle valeur plus courte.
    *   On enregistre que le sommet $k$ est le "père" de $j$ (tableau de `provenance`) pour pouvoir reconstruire le chemin plus tard.
    *   On met à jour la position de $j$ dans la file de priorité.

## 4. Terminaison et Résultat

*   **Garantie d'optimalité :** Contrairement à l'algorithme *Best-First Search*, Dijkstra **garantit mathématiquement** de trouver le chemin le plus court car il explore toutes les directions de manière exhaustive en s'assurant de toujours valider le coût minimal.
*   **Portée :** À la fin de l'exécution, l'algorithme a calculé le plus court chemin de l'origine vers **n'importe quel autre sommet** du graphe.
*   **Complexité :** Avec une implémentation optimisée (comme le module `heapdict` en Python), les opérations sur la file de priorité coûtent $O(\log n)$. La complexité totale de l'algorithme est de l'ordre de **$(p + n) \log(n)$**, où $n$ est le nombre de sommets et $p$ le nombre d'arêtes.

En résumé, Dijkstra fonctionne par "vagues" successives de distance croissante depuis le point de départ, en privilégiant toujours le sommet le plus proche de l'origine parmi ceux restant à explorer.

L'implémentation de l'algorithme de **Dijkstra** en Python nécessite une structure de données spécifique pour être efficace : la **file de priorité**.


## 5. Exemple d'implémentation en Python
L'algorithme prend en entrée une liste d'adjacence (`adj`) et une matrice des poids (`poids`).

```python
import heapdict
from math import inf

def dijkstra(adj, poids):
    n = len(adj)
    # Tableau pour stocker le sommet parent (pour reconstruire le chemin)
    provenance =  * n 
    # Tableau des distances minimales estimées, initialisées à l'infini
    poids_est = [inf] * n
    poids_est = 0 # Distance vers le départ fixée à 0
    
    # Initialisation de la file de priorité
    poids_fp = heapdict.heapdict()
    poids_fp = 0
    
    while len(poids_fp) > 0:
        # On extrait le sommet 'k' ayant le poids minimal
        k = poids_fp.popitem()
        
        for j in adj[k]: # Exploration des voisins de k
            # Calcul de la nouvelle distance potentielle
            d = poids_est[k] + poids[k][j]
            
            # Si on a trouvé un chemin plus court vers 'j'
            if d < poids_est[j]:
                provenance[j] = k
                poids_est[j] = d
                # Mise à jour (ou insertion) dans la file de priorité
                poids_fp[j] = d 
                
    return provenance
```

### 5.1. Fonctionnement étape par étape

1.  **Initialisation :** Toutes les distances sont à l'infini, sauf l'origine à 0.
2.  **Sélection :** On extrait de la file le sommet de poids minimal.
3.  **Relâchement (Mise à jour) :** Pour chaque voisin, on vérifie si passer par le sommet actuel réduit la distance vers ce voisin. Si oui, on met à jour la table des distances et la file de priorité.
4.  **Terminaison :** On recommence jusqu'à ce que la file soit vide.

### 5.2. Reconstitution du chemin
L'algorithme renvoie un tableau `provenance`. Pour obtenir l'itinéraire complet vers un sommet cible, il faut utiliser une fonction qui remonte de "père en père" :

```python
def decrit_chemin(etiquettes, provenance):
    n = len(etiquettes)
    s = ""
    k = n - 1 # On part de l'arrivée
    while k != 0:
        s = ' ' + etiquettes[k] + s
        k = provenance[k]
    return etiquettes + s
```
