# Chapitre 8 : Les Graphes - Notions Essentielles

Les graphes sont des structures de données fondamentales en informatique permettant de modéliser des **réseaux** (routiers, sociaux, électriques) ou des relations entre des entités.

## 1. Vocabulaire et Fondamentaux

Un graphe $G = (S, A)$ est composé de deux ensembles :

*   **$S$ :** l'ensemble des **sommets** (ou nœuds).
*   **$A$ :** l'ensemble des **liens** entre les sommets.

### Caractéristiques de base

*   **Graphe non orienté :** Les liens sont des **arêtes**. La relation est symétrique : si A est lié à B, alors B est lié à A.
*   **Graphe orienté :** Les liens sont des **arcs** (représentés par des flèches). Le lien va d'une origine vers une destination.
*   **Ordre d'un graphe :** Le nombre total de sommets $n$.
*   **Taille d'un graphe :** Le nombre total d'arêtes ou d'arcs.
*   **Degré d'un sommet :** Nombre d'arêtes reliées à ce sommet. Dans un graphe orienté, on distingue le **degré entrant** et le **degré sortant**.

!!! tip "Le saviez-vous ?"
    L'origine de la théorie des graphes remonte à **Leonhard Euler** en 1735 avec le problème des sept ponts de Königsberg.

## 2. Propriétés des Graphes

*   **Graphe valué (ou pondéré) :** Chaque arête/arc possède un **poids** (coût, distance, temps).
*   **Graphe complet :** Un graphe simple où chaque sommet est relié à tous les autres.
*   **Chaîne / Chemin :** Suite de sommets reliés par des arêtes (chaîne) ou des arcs (chemin).
*   **Cycle / Circuit :** Une chaîne (cycle) ou un chemin (circuit) dont les sommets de départ et d'arrivée sont identiques.
*   **Connexité :** Un graphe est **connexe** s'il existe une chaîne entre n'importe quelle paire de sommets.

## 3. Représentations Informatiques

Il existe deux manières principales de représenter un graphe en mémoire :

### A. Matrice d'adjacence
C'est un tableau de taille $n \times n$ où la case `M[i][j]` vaut 1 s'il existe un lien entre le sommet $i$ et $j$, sinon 0.

*   **Avantage :** Accès très rapide ($O(1)$) pour vérifier l'existence d'une arête.
*   **Inconvénient :** Très coûteux en mémoire ($n^2$) pour les graphes **creux** (peu de liens).

### B. Listes d'adjacence
On associe à chaque sommet la liste de ses voisins.

*   **Avantage :** Compact en mémoire pour les graphes peu denses.
*   **Inconvénient :** La recherche d'une arête spécifique est plus lente ($O(\text{degré du sommet})$).

```python
# Exemple de liste d'adjacence en Python (dictionnaire)
graphe = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

## 4. Algorithmes de Parcours

### Parcours en Largeur (BFS, Breadth-First Search)
Cet algorithme explore le graphe étage par étage, en visitant d'abord tous les voisins directs d'un sommet, puis les voisins des voisins.

*   **Outil :** Utilise une **file (FIFO)**.
*   **Application :** Trouver le plus court chemin en nombre d'étapes.

### Parcours en Profondeur (DFS, Depth-First Search)
Cet algorithme explore chaque branche le plus loin possible avant de revenir en arrière pour explorer d'autres chemins.

*   **Outil :** Utilise une **pile (LIFO)** ou la **récursivité**.
*   **Application :** Détecter des cycles ou tester la connexité.

---

## Exercices d'application

### Exercice 1 : Modélisation
Soit le graphe non orienté suivant : Sommets {1, 2, 3, 4} et Arêtes {(1,2), (2,3), (2,4), (3,4)}.

1. Quel est l'ordre du graphe ?
2. Quel est le degré du sommet 2 ?
3. Le graphe est-il complet ?

??? success "Solution"
    1. L'ordre est **4** (il y a 4 sommets).
    2. Le degré du sommet 2 est **3** (relié à 1, 3 et 4).
    3. Non, car le sommet 1 n'est pas relié aux sommets 3 et 4.

### Exercice 2 : Matrice d'adjacence
Donnez la matrice d'adjacence du graphe de l'exercice 1.

??? success "Solution"
    En prenant les sommets dans l'ordre 1, 2, 3, 4 :
    ```
    []
    ```
    Note : La matrice est symétrique car le graphe est non orienté.

### Exercice 3 : Algorithmes
Si vous devez trouver le chemin le plus court (en nombre de villes) entre deux villes dans un réseau ferroviaire, quel parcours utilisez-vous ?

*   A) Parcours en profondeur
*   B) Parcours en largeur

??? success "Solution"
    **B) Parcours en largeur.** Il permet de visiter les sommets par "générations" de distance croissante, garantissant ainsi l'optimalité du nombre d'étapes.
