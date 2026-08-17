# Arbre d'appels et complexité

L'**arbre d'appels** est une représentation graphique de l'exécution d'un programme récursif qui permet de visualiser directement sa **complexité** en fonction de la structure et du nombre de nœuds produits.

### 1. Visualisation du nombre total d'opérations
Chaque nœud de l'arbre représente un appel à la fonction. Le coût total de l'algorithme est donc directement proportionnel au **nombre total de nœuds** dans l'arbre.

*   Dans un algorithme à **complexité linéaire**, comme le calcul de la somme des $n$ premiers entiers ou de la factorielle, l'arbre ne bifurque pas ; il forme une chaîne simple (ou cascade) de $n$ appels.
*   Dans un algorithme à **complexité exponentielle**, comme la version naïve de Fibonacci, chaque appel en génère deux autres, provoquant une "explosion" du nombre de nœuds qui double presque à chaque niveau de profondeur.

### 2. Illustration de la profondeur (Complexité spatiale)
La **hauteur de l'arbre** correspond à la profondeur maximale de la pile d'exécution. 

*   Pour l'**exponentiation rapide**, l'arbre montre que l'on divise l'exposant par deux à chaque étape. La profondeur de l'arbre est donc très réduite : elle est proportionnelle à $\log_2(n)$. Cela illustre pourquoi un tel algorithme est beaucoup plus performant qu'une boucle itérative sur de grandes valeurs.

### 3. Mise en évidence de l'efficacité (ou de l'inefficacité)
L'arbre d'appels permet de repérer visuellement les faiblesses d'un algorithme :

*   **Redondance :** Dans l'arbre de `fib(5)`, on peut voir que `fib(3)` est calculé plusieurs fois dans des branches différentes. Cette répétition inutile de calculs est ce qui conduit à une complexité prohibitive, que la programmation dynamique permet d'optimiser.
*   **Paradigme "Diviser pour régner" :** Pour le tri fusion, l'arbre illustre la division du problème en deux sous-problèmes à chaque étage. On y voit que la profondeur est de $\log_2(n)$ niveaux et que chaque niveau nécessite un travail de fusion proportionnel à $n$, d'où une complexité globale de $O(n \log_2 n)$.

En résumé, la **forme** de l'arbre (chaîne, arbre équilibré ou arbre binaire complet) traduit visuellement la vitesse à laquelle le nombre d'opérations croît par rapport à la taille de l'entrée.