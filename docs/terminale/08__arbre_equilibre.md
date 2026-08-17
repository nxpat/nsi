# Arbre équilibré

Un **arbre équilibré** est un arbre binaire (généralement un arbre binaire de recherche) qui respecte des contraintes de structure pour minimiser sa hauteur totale.

### 1. Définition et principe
De manière intuitive, un arbre est dit équilibré lorsque tous les chemins allant de la racine aux feuilles ont **à peu près la même longueur**. Cela signifie que les sous-arbres gauche et droit de chaque nœud ont une **taille similaire**.

Dans le cas plus formel des **arbres AVL** (un type d'arbre de recherche équilibré), la règle est plus stricte : pour chaque nœud, la différence entre la hauteur du sous-arbre gauche et celle du sous-arbre droit ne doit pas excéder **1**.

### 2. Pourquoi l'équilibre est-il important ?
L'équilibre d'un arbre influence directement l'efficacité des algorithmes.
*   **Performance optimale :** Dans un arbre équilibré de $n$ nœuds, la hauteur est de l'ordre de **$\log_2(n)$**. Les opérations de recherche, d'insertion et de suppression sont alors très rapides (complexité logarithmique).
*   **Le contre-exemple (arbre dégénéré) :** À l'inverse, si un arbre n'est pas équilibré, il peut devenir "filiforme" ou "dégénéré" (ressemblant à une liste chaînée). Dans ce cas, les recherches deviennent beaucoup plus lentes, avec une complexité linéaire en $O(n)$.

### 3. Exemples et maintien de l'équilibre
*   **Arbre complet :** Un arbre binaire est dit **complet** s'il possède tous les nœuds possibles à chaque niveau (soit $2^p$ nœuds à la profondeur $p$). C'est l'exemple type de l'arbre parfaitement équilibré.
*   **Rééquilibrage :** Comme les insertions successives peuvent déséquilibrer un arbre, il existe des algorithmes (comme les **rotations** gauche et droite utilisées pour les arbres AVL) qui permettent de restructurer l'arbre pour maintenir son équilibre tout en préservant ses propriétés de tri.

En résumé, l'équilibrage est une stratégie visant à "tasser" l'arbre pour qu'il soit le plus large et le moins haut possible, garantissant ainsi des performances de recherche optimales.