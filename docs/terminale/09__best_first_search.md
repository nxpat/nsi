# Algorithme Best-First Search

L'algorithme **Best-First Search** (parcours au plus proche) est un algorithme de recherche de chemin qui se distingue du parcours en largeur (BFS) par sa stratégie de sélection des sommets à explorer.

## Principales caractéristiques

*   **Principe de sélection :** Contrairement au BFS qui utilise une file d'attente classique (FIFO), le Best-First choisit, parmi les sommets en attente d'exploration (la « frontière »), celui qui est géographiquement le **plus proche de la cible**, généralement calculé « à vol d'oiseau ».
*   **Algorithme « informé » :** On le qualifie d'algorithme informé car il utilise une **heuristique** (une règle simplifiée), en l'occurrence le calcul de la distance euclidienne pour guider ses choix vers la destination.
*   **Rapidité et exploration :** Cet algorithme est très rapide et a l'avantage d'explorer **moins d'arêtes** que des méthodes plus exhaustives comme l'algorithme A* ou Dijkstra.
*   **Non-optimalité :** Son principal inconvénient est qu'il **ne garantit pas de trouver le chemin le plus court**. Il peut se laisser « piéger » par des configurations particulières du réseau et fournir un itinéraire sous-optimal.
*   **Utilisation pratique :** Il reste très efficace dans des réseaux routiers denses où la stratégie consistant à se rapprocher le plus vite possible de la cible est souvent payante.

En résumé, c'est un algorithme qui privilégie la **rapidité d'exécution** au détriment de la précision absolue de l'itinéraire trouvé. Il a d'ailleurs servi d'inspiration pour la création de l'algorithme **A***, qui combine la rapidité du **Best-First** avec la garantie d'optimalité de l'algorithme de **Dijkstra**.

## Différences avec l'algorithme de Dijkstra

La principale différence entre l'algorithme de **Dijkstra** et le **Best-First Search** réside dans la stratégie de sélection des sommets à explorer et la garantie d'obtenir le chemin le plus court.

Voici les points de divergence majeurs :

### 1. Critère de sélection (Origine vs Cible)
*   **Dijkstra :** Sélectionne le sommet dont la distance estimée depuis le **point de départ** est la plus courte. Il construit progressivement le chemin en s'assurant de la validité de la distance parcourue depuis l'origine.
*   **Best-First Search :** Sélectionne le sommet qui semble le plus proche de la **cible (point d'arrivée)**, généralement en utilisant une mesure "à vol d'oiseau" (distance euclidienne).

### 2. Garantie d'optimalité
*   **Dijkstra :** **Garantit mathématiquement** de trouver le chemin le plus court entre le départ et l'arrivée dans un graphe pondéré à poids positifs.
*   **Best-First Search :** **Ne garantit pas** l'optimalité. Il peut se laisser "piéger" par la configuration du graphe et fournir un chemin plus long que le chemin minimal théorique.

### 3. Étendue de la recherche
*   **Dijkstra :** Permet de trouver le plus court chemin de l'origine vers **n'importe quel autre sommet** du graphe.
*   **Best-First Search :** Est une recherche ciblée qui ne s'intéresse qu'à un seul sommet de destination spécifique.

### 4. Efficacité et exploration
*   **Dijkstra :** Explore généralement un **grand nombre d'arêtes** car il examine toutes les directions possibles pour garantir le minimum, ce qui le rend plus "coûteux" en temps de calcul.
*   **Best-First Search :** Explore **beaucoup moins d'arêtes** car il fonce vers la cible, ce qui le rend très rapide.

### Tableau récapitulatif

| Caractéristique | Dijkstra | Best-First Search |
| :--- | :--- | :--- |
| **Objectif de sélection** | Plus proche du **départ** | Plus proche de l'**arrivée** |
| **Chemin le plus court** | **Garanti** (Optimal) | **Non garanti** |
| **Type d'algorithme** | Non informé (exhaustif) | Informé (Heuristique) |
| **Rapidité** | Plus lent (explore tout) | Très rapide |

L'algorithme **A*** tente de combiner le meilleur des deux mondes : la garantie d'optimalité de Dijkstra et la rapidité de guidage vers la cible du Best-First Search.