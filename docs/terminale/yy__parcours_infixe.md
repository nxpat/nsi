# Pparcours infixe

Le **parcours infixe** (ou parcours en ordre) est une méthode de parcours en profondeur (DFS) d'un arbre binaire qui suit une logique récursive précise pour visiter chaque nœud.

### 1. Principe de fonctionnement
Dans un parcours infixe, on traite les éléments de l'arbre dans l'ordre suivant :

1.  On parcourt récursivement le **sous-arbre gauche**.
2.  On examine (ou traite) la **racine** (le nœud actuel).
3.  On parcourt récursivement le **sous-arbre droit**.

### 2. Algorithme (en pseudo-code)
La fonction se définit de manière récursive comme suit :
```python
fonction parcours_infixe(arbre):
    si arbre n'est pas vide:
        parcours_infixe(arbre.fils_gauche)  # Étape 1
        traiter(arbre.valeur)                # Étape 2
        parcours_infixe(arbre.fils_droit)   # Étape 3
```

### 3. Propriété majeure avec les ABR
L'intérêt principal du parcours infixe réside dans son utilisation sur les **arbres binaires de recherche (ABR)**. En raison de la structure de ces arbres (où les valeurs à gauche sont plus petites que la racine et les valeurs à droite sont plus grandes), un parcours infixe permet de **récupérer les clés de l'arbre dans l'ordre croissant**.

Par exemple, si un ABR contient les nombres `{5, 2, 11}`, le parcours infixe visitera d'abord le nœud 2, puis le 5, et enfin le 11.

### 4. Application aux expressions arithmétiques
Pour un arbre syntaxique représentant une expression arithmétique (comme `(2 * 3) + 5`), le parcours infixe permet de retrouver la **notation habituelle** de l'expression telle que nous la lisons, avec les opérateurs placés entre leurs opérandes.