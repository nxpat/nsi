# Chapitre 5 : La Récursivité

## 1. Définition et Principe
Une fonction est dite **récursive** lorsqu'elle s'appelle elle-même au cours de son exécution. 

L'idée centrale est de résoudre un problème complexe en le décomposant en un ou plusieurs sous-problèmes identiques mais de taille plus petite. En répétant ce processus, on aboutit à un problème si simple qu'il peut être résolu directement : c'est le **cas élémentaire**.

## 2. Les deux piliers d'une fonction récursive
Pour qu'une fonction récursive soit correcte, elle doit impérativement comporter deux parties :

1.  **Le cas de base (ou condition d'arrêt) :** C'est la situation la plus simple qui ne nécessite pas d'appel récursif. Sans lui, la fonction s'appellerait à l'infini.
2.  **L'appel récursif :** La fonction s'appelle elle-même sur une donnée "plus petite" ou plus proche du cas de base pour assurer la terminaison du programme.

### Exemple : La fonction Factorielle
Mathématiquement, $n! = n \times (n-1) \times \dots \times 1$ avec $0! = 1$.
Sa définition récursive est :

- Si $n = 0$, $n! = 1$ (cas de base)
- Si $n > 0$, $n! = n \times (n-1)!$ (appel récursif).

```python
def factorielle(n):
    if n == 0:
        return 1 # Cas de base
    else:
        return n * factorielle(n - 1) # Appel récursif
```

## 3. Fonctionnement en mémoire : La pile d'appels
Lorsqu'un programme exécute une fonction récursive, chaque appel est stocké dans une structure de données appelée **pile d'exécution** (ou *stack*).

- Chaque appel crée un **contexte d'exécution** (un "cadre") contenant les variables locales.
- Les contextes s'empilent jusqu'à atteindre le cas de base.
- Une fois le cas de base résolu, les résultats "remontent" et les contextes sont dépilés successivement pour finaliser les calculs.

**Représentation :** On utilise souvent un **arbre d'appels** pour visualiser cette cascade d'exécutions.

## 4. Un paradigme puissant : "Diviser pour régner"
La récursivité est au cœur de la stratégie **"Diviser pour régner"** (Divide and Conquer), qui consiste à :

1.  **Diviser** le problème en sous-problèmes plus petits.
2.  **Régner** en résolvant les sous-problèmes récursivement.
3.  **Combiner** les résultats pour obtenir la solution finale.

Le **tri fusion** (*merge sort*) est l'exemple type : on coupe un tableau en deux, on trie chaque moitié récursivement, puis on fusionne les deux moitiés triées. Sa complexité est de l'ordre de $n \log_2(n)$, ce qui est bien plus efficace qu'un tri par insertion pour de grandes listes.

## 5. Limites et Vigilance

*   **Profondeur de récursion :** Python limite par défaut le nombre d'appels récursifs (généralement à 1000) pour éviter de saturer la mémoire. Dépasser cette limite provoque une erreur `RecursionError`.
*   **Efficacité :** Certains algorithmes récursifs "naïfs" effectuent plusieurs fois les mêmes calculs (comme pour la suite de Fibonacci), ce qui les rend très lents par rapport à une version itérative ou optimisée par **programmation dynamique**.

***

## Exercices d'application

### Exercice 1 : Somme des éléments d'une liste
Compléter la fonction récursive `somme_liste(L)` qui calcule la somme des nombres contenus dans une liste `L`.
*Indice : Le cas de base est une liste vide (somme = 0).*

```python
def somme_liste(L):
    if L == []:
        return 0
    else:
        # À compléter : premier élément + somme du reste de la liste
        return ...

# Test
print(somme_liste()) # Devrait afficher 15
```
{{ IDE('05_exos/exo1') }}

### Exercice 2 : Compte à rebours
Écrire une fonction récursive `compte_a_rebours(n)` qui affiche les nombres de `n` jusqu'à 0.

```python
def compte_a_rebours(n):
    # Afficher n, puis déclencher l'appel récursif si n > 0
    pass

# Test
compte_a_rebours(5)
```

{{ IDE('05_exos/exo2') }}

### Exercice 3 : Le Palindrome
Un palindrome est un mot qui se lit de la même façon dans les deux sens (ex: "radar"). Compléter la fonction ci-dessous.

```python
def est_palindrome(mot):
    if len(mot) <= 1:
        return True
    # Ccompléter la condition et la valeur de retour récursive
    if ...:
        return False
    else:
        return ...

# Tests
print(est_palindrome("radar"))    # True
print(est_palindrome("nsi"))      # False
```

{{ IDE('05_exos/exo3') }}