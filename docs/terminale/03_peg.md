# Chapitre 3 : Programmer en grand

Lorsque le code d'un programme dépasse quelques centaines de lignes, il devient nécessaire de le structurer pour faciliter sa maintenance, son évolution et la collaboration entre développeurs.

## 1. La Modularité et les API

### Modules et Bibliothèques

*   **Module** : Un fichier contenant des définitions de fonctions, de classes ou de variables que l'on peut importer dans un autre programme via la commande `import`.

*   **Bibliothèque (Library)** : Un ensemble de plusieurs modules offrant des fonctionnalités thématiques (ex: `math`, `random`, `matplotlib`).

### Notion d'API (Application Programming Interface)
Une **API** est un ensemble normalisé de briques logicielles permettant à un système d'offrir des services à d'autres sans révéler son fonctionnement interne. 

*   **Interface** : Définit le « quoi » (quelles fonctions appeler et comment les utiliser).
*   **Implémentation** : Définit le « comment » (le code interne caché à l'utilisateur).
*   **Encapsulation** : Permet de modifier l'implémentation interne sans impacter les utilisateurs de l'interface.

---

## 2. Spécification et Documentation

Pour qu'un module soit utilisable par d'autres, il doit être documenté :

*   **Docstring** : Une chaîne de caractères placée juste après la définition d'une fonction ou d'une classe (entre `""" ... """`) pour expliquer son rôle. On peut y accéder via la fonction `help(nom_fonction)`.

*   **Préconditions** : Conditions que les arguments d'entrée doivent vérifier pour que la fonction soit valide. On utilise souvent des clauses `assert` pour les tester.

*   **Post-conditions** : Propriétés garanties sur le résultat à la sortie de la fonction.

---

## 3. Mise au point et Gestion des bugs

### Types d'erreurs classiques

*   `ZeroDivisionError` : Division par zéro.
*   `IndexError` : Accès à un indice hors des bornes d'un tableau.
*   `TypeError` : Opération sur un type non supporté (ex: additionner un entier et une chaîne).
*   `NameError` : Utilisation d'une variable non définie.

### Méthodes de débuggage

1.  **Exécution pas-à-pas** : Simuler manuellement ou via un outil l'évolution des variables à chaque ligne.
2.  **Affichages temporaires** : Utiliser `print()` pour vérifier l'état des données en cours d'exécution.
3.  **Utilisation d'un débuggeur** : Outils intégrés aux environnements de développement (IDE) ou outils en ligne comme Python Tutor.

---

## 4. Validation par les Tests

Un test ne garantit jamais l'absence totale de bug, mais il augmente la confiance dans le programme.

*   **Test unitaire** : Teste une petite unité isolée du programme, généralement une seule fonction.
*   **Test « boîte noire » (fonctionnel)** : Conçu uniquement à partir de la spécification (entrées/sorties attendues), sans regarder le code interne.
*   **Test « boîte blanche » (structurel)** : Conçu en examinant le code pour s'assurer que chaque branche (les `if`, les boucles) est bien exécutée.
*   **Non-régression** : Vérifier que la correction d'un bug ou l'ajout d'une fonction n'a pas cassé ce qui fonctionnait déjà.

**Outil conseillé :** Le module **pytest** permet d'automatiser l'exécution de fonctions de test commençant par `test_`.

---

## 5. Exercices d'application

### Exercice 1 : Analyse d'erreurs
Soit le code suivant :
```python
def division(a, b):
    return a / b

x = division(10, "2")
```

1. Quelle erreur Python va-t-il lever ?
2. Écrire la ligne de code utilisant `assert` à ajouter au début de la fonction pour s'assurer que `b` est bien un nombre (type `int` ou `float`) et qu'il est non nul.

### Exercice 2 : Test « boîte noire »
Vous devez tester une fonction `calcul_remise(prix, pourcentage)` qui applique une réduction sur un prix.

1. Proposer trois cas de tests sous forme de triplets (descriptif, données, résultat attendu) incluant des valeurs limites.
2. Pourquoi tester `pourcentage = 100` est-il important dans ce cadre ?

### Exercice 3 : Documentation et Sécurisation
Écrire la **docstring** et une clause `assert` de précondition pour la fonction suivante, sachant que la longueur et la largeur doivent être strictement positives :
```python
def calcule_aire_rectangle(longueur, largeur):
    """
    Indiquer ici le rôle de la fonction et de ses paramètres
    """
    # Ajouter ici l'assertion de précondition
    return longueur * largeur
```

***

## 6. Automatisation des tests avec Pytest

L'automatisation des tests avec **pytest** est une pratique standard en Python pour garantir la qualité du code. Ce module externe est l'outil le plus utilisé car il est très complet.

Voici la démarche pour mettre en œuvre des tests automatisés :

### 6.1. Structure et nommage
Pour que **pytest** détecte automatiquement les tests à effectuer, il faut respecter des conventions de nommage strictes :

*   **Fichiers** : Le nom du fichier Python doit commencer par `test_` (par exemple : `test_algorithmes.py`).
*   **Fonctions** : À l'intérieur de ces fichiers, chaque cas de test doit être une fonction dont le nom commence également par `test_`.

### 6.2. Écriture d'un cas de test
Un cas de test unitaire classique se structure généralement en trois étapes :

1.  Définir le résultat **attendu**.
2.  Calculer le résultat **effectif** en appelant la fonction du programme.
3.  Utiliser l'instruction **`assert`** pour comparer les deux.

**Exemple de structure :**
```python
def test_calcul_aire():
    attendu = 50
    effectif = rectangle.calcule_aire(10, 5)
    assert attendu == effectif
```

### 6.3. Exécution des tests
L'exécution se fait via le terminal de commande :

*   **Pour tester tout un dossier** : Taper simplement `pytest`. L'outil cherchera tous les fichiers commençant par `test_` dans le répertoire courant et exécutera les fonctions de test qu'ils contiennent.
*   **Pour tester un fichier précis** : Taper `pytest nom_du_fichier.py`.

### 6.4. Lecture du rapport de test
Après exécution, **pytest** génère un rapport :

*   **Un point (`.`)** signifie que le test a réussi (aucune erreur n'a été levée).
*   **Un `F` (Fail)** signifie que le test a échoué. Une `AssertionError` a été levée car le résultat effectif ne correspondait pas à l'attendu.
*   En cas d'échec, le rapport détaille précisément quelle ligne a posé problème et quelles étaient les valeurs comparées.

### 6.5. Tester les cas d'erreur (Préconditions)
Si le programme doit lever une erreur dans certains cas (par exemple si une précondition `assert` n'est pas vérifiée), il est possible d'automatiser ce test avec `pytest.raises` :

```python
import pytest

def test_division_par_zero():
    with pytest.raises(ZeroDivisionError):
        ma_fonction_division(10, 0)
```

### 6.6. Aller plus loin : Analyse de couverture
Il est possible de coupler **pytest** avec l'outil **coverage** pour savoir quel pourcentage du code d'un programme est réellement testé :

*   `coverage run -m pytest fichier_test.py` : exécute les tests et analyse la couverture.
*   `coverage report -m` : affiche un résumé dans le terminal indiquant les lignes non lues par les tests.