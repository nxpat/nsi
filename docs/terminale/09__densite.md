# Densité d'un graphe

La densité $D$ d'un graphe simple est un indicateur de sa connectivité, variant entre 0 (aucune arête) et 1 (graphe complet). Elle se calcule selon le type de graphe (avec $S$ le nombre de sommets et $A$ le nombre d'arêtes ou d'arcs) :

*   **Pour un graphe orienté :**
    $$D = \frac{A}{S \times (S - 1)}$$
*   **Pour un graphe non-orienté :**
    $$D = \frac{2 \times A}{S \times (S - 1)}$$

Un graphe est qualifié de **« creux »** si sa densité est proche de 0 et de **« dense »** si elle est proche de 1. Par exemple, les réseaux sociaux ou routiers sont souvent des graphes creux.