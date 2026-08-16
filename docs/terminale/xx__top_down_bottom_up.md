# Programmation dynamique : approches Top-down et Bottom-up
Les approches **Top-down** (descendante) et **Bottom-up** (ascendante) sont deux méthodes de résolution utilisées en **programmation dynamique** pour optimiser des calculs complexes en évitant de résoudre plusieurs fois les mêmes sous-problèmes.

## 1. L'approche descendante (Top-down)
*   **Principe :** On commence par le **problème initial** et on le décompose récursivement en sous-problèmes plus petits.
*   **Fonctionnement :** Elle utilise la **récursivité**. Pour éviter l'explosion du nombre de calculs (comme dans le cas de Fibonacci naïf), on utilise la **mémoïsation** : on enregistre les résultats des sous-problèmes dans un cache (dictionnaire ou tableau) au fur et à mesure qu'on les rencontre pour la première fois.
*   **Avantage :** Elle ne calcule que les sous-problèmes strictement nécessaires pour obtenir la solution finale.

## 2. L'approche ascendante (Bottom-up)
*   **Principe :** On résout d'abord les **plus petits sous-problèmes** (les cas de base), puis on combine leurs résultats pour résoudre des problèmes de taille croissante jusqu'à atteindre le problème global.
*   **Fonctionnement :** Elle est généralement **itérative** (utilisation de boucles). On remplit systématiquement un tableau de résultats en partant des indices les plus bas.
*   **Avantage :** Elle évite les risques de dépassement de la pile d'appels (liés à la récursion) et permet parfois de mieux optimiser l'espace mémoire en n'effaçant les résultats intermédiaires dont on n'a plus besoin.

## Exemple comparatif : La suite de Fibonacci
Pour calculer le $n$-ième terme de la suite :

*   **En Top-down :** On appelle `fibo(n)`, qui appelle `fibo(n-1)` et `fibo(n-2)`. Si `fibo(n-2)` est déjà en mémoire, on renvoie la valeur immédiatement sans refaire l'arbre d'appels.
*   **En Bottom-up :** On remplit un tableau en commençant par `f=0`, `f=1`, puis on calcule `f`, `f`, etc., jusqu'à arriver à `f[n]`.