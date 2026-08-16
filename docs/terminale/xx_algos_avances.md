Voici une proposition de résumé de cours pour le **Chapitre 13 : Les algorithmes avancés**, structuré pour une intégration dans MkDocs et compatible avec Pyodide. Ce chapitre se concentre sur deux familles d'algorithmes : la **programmation dynamique** et la **recherche textuelle**.

***

# Chapitre 13 : Algorithmes avancés

 Ce chapitre se concentre sur deux familles d'algorithmes : la **programmation dynamique** et la **recherche textuelle**.

Lobjectif est de **réduire la complexité** de calculs coûteux, soit en évitant de recalculer des résultats identiques, soit en optimisant la recherche de motifs dans des textes.

## 1. La Programmation Dynamique

### Principe
La programmation dynamique est une méthode de résolution de problèmes complexes en les décomposant en **sous-problèmes plus simples** qui se chevauchent. Contrairement à la stratégie "Diviser pour régner" où les sous-problèmes sont indépendants (comme dans le tri fusion), ici, les mêmes calculs apparaissent de nombreuses fois.

### Caractéristiques
Pour qu'un problème puisse être résolu par programmation dynamique, il doit posséder deux propriétés :
1.  **Sous-structure optimale :** La solution optimale du problème global s'obtient à partir des solutions optimales des sous-problèmes.
2.  **Sous-problèmes superposés :** Le traitement récursif fait apparaître les mêmes sous-problèmes de nombreuses fois.

### Méthodes de résolution
*   **Méthode descendante (*Top-down*) :** On utilise la récursivité en ajoutant la **mémoïsation** (*memoization*), qui consiste à stocker les résultats des appels déjà effectués dans un dictionnaire ou un tableau pour ne pas les recalculer.
*   **Méthode ascendante (*Bottom-up*) :** On remplit de façon itérative un tableau en partant des cas les plus simples pour arriver au résultat final.

**Exemple : Suite de Fibonacci**
La version récursive naïve a une complexité exponentielle car elle recalcule inutilement plusieurs fois les mêmes termes.

```python
# Version descendante avec mémoïsation
def fibo_dyn(n, mem={}):
    if n <= 1:
        return n
    if n not in mem:
        mem[n] = fibo_dyn(n - 1, mem) + fibo_dyn(n - 2, mem)
    return mem[n]

# Test
print(fibo_dyn(50)) 
```

### Applications classiques

*   **Rendu de monnaie :** Trouver le nombre minimal de pièces pour rendre une somme donnée.
*   **Problème du sac à dos :** Maximiser la valeur d'objets emportés sans dépasser une capacité de poids.
*   **Alignement de séquences :** Calcul de la plus longue sous-chaîne commune.

## 2. Recherche Textuelle

L'objectif est de trouver la position d'un **motif** (chaîne `m`) dans un **texte** (chaîne `t`).

### L'approche naïve
On compare le motif avec chaque fenêtre du texte en se décalant d'un caractère à chaque échec. Sa complexité est de l'ordre de $O(n \times m)$.

### L'algorithme de Boyer-Moore
C'est une optimisation majeure utilisée dans les éditeurs de texte. Il repose sur deux principes :

1.  **Parcours à l'envers :** On compare les caractères du motif en partant de la **droite** vers la gauche.
2.  **Sauts intelligents (Règle du mauvais caractère) :** En cas de discordance, au lieu de se décaler d'une seule case, on utilise un **prétraitement** du motif pour décaler le curseur de plusieurs positions.

Si le caractère du texte provoquant l'erreur existe ailleurs dans le motif, on aligne le motif sur ce caractère. S'il n'existe pas, on peut décaler le motif juste après cette position.

***

## Exercices d'application

### Exercice 1 : Rendu de monnaie (Dynamique)
On dispose d'un système de pièces. Compléter la fonction ascendante pour calculer le nombre minimal de pièces pour une `somme` donnée.

```python
from math import inf

def rendu_monnaie_it(valeurs, somme):
    # f[s] représente le nombre minimal de pièces pour former la somme s
    # Initialisation : f[0] = 0 et inf pour les autres sommes
    f = [0] + [inf] * somme
    
    for s in range(1, somme + 1):
        for x in valeurs:
            if s >= x:
                # À compléter : mise à jour de f[s] avec le minimum de pièces
                ...
                
    return f[somme]

# Tests
print(rendu_monnaie_it([1, 2, 5], 11))  # Devrait afficher 3 (5+5+1)
print(rendu_monnaie_it([2, 5], 3))      # Devrait afficher inf (impossible)
```

### Exercice 2 : Recherche naïve de motif
Compléter la fonction `recherche_naive` pour qu'elle renvoie l'indice de la première occurrence de `motif` dans `texte`, ou `None` sinon.

```python
def recherche_naive(texte, motif):
    n = len(texte)
    m = len(motif)

    # Parcoure les positions possibles du motif dans le texte
    # À compléter.
    pass

# Test
print(recherche_naive("algorithmes avancés", "avance")) # Devrait afficher 13
```

### Exercice 3 : Prétraitement Boyer-Moore
Dans l'algorithme de Boyer-Moore, on crée un dictionnaire des sauts pour la "règle du mauvais caractère". Pour le motif `"NSInsi"`, quel serait le décalage associé au caractère `'i'` s'il provoque une erreur à la dernière position ?

*Indice : On cherche la distance entre la dernière occurrence de la lettre (avant la fin) et la fin du motif.*

??? info "Réponse"
    **Réponse attendue :** 0 (puisque c'est le dernier caractère) ou le calcul de la position précédente.