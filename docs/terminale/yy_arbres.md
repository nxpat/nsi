# Chapitre 7 : Les Arbres

Ce chapitre introduit les structures de données hiérarchiques, s'éloignant des structures linéaires (listes, piles, files) pour modéliser des relations de parenté ou des organisations complexes.

## 1. Vocabulaire et Définitions Générales

Un **arbre** est un graphe connexe et acyclique. En informatique, on étudie principalement les **arbres enracinés** :

*   **Racine :** L'unique nœud sans parent, point d'entrée de l'arbre.
*   **Nœud :** Élément de l'arbre contenant une donnée (clé) et des liens vers ses fils.
*   **Feuille :** Nœud n'ayant aucun fils (nœud externe).
*   **Nœud interne :** Nœud possédant au moins un fils.
*   **Arborescence :** Chaque nœud (sauf la racine) a exactement un parent.

### Exemples d'utilisation

*   Systèmes de fichiers (répertoires et fichiers).
*   Le DOM (Document Object Model) d'une page HTML.
*   Arbres syntaxiques pour les expressions arithmétiques.

## 2. L'Arbre Binaire

Un **arbre binaire** est une structure récursive : soit il est vide, soit il est constitué d'une racine et de deux sous-arbres (gauche et droit), eux-mêmes arbres binaires.

### Mesures de l'arbre

*   **Taille (n) :** Nombre total de nœuds.
*   **Profondeur d'un nœud :** Nombre d'arêtes entre la racine et ce nœud (la racine est à la profondeur 0).
*   **Hauteur (h) :** Profondeur maximale de ses nœuds. 
    *   *Convention :* Un arbre vide a une hauteur de -1, un arbre réduit à sa racine a une hauteur de 0.
*   **Encadrement :** Pour un arbre de taille $n$ et de hauteur $h$, on a $\lfloor \log_2(n) \rfloor \le h \le n-1$.

## 3. Implémentation en Python (POO)

On utilise généralement deux classes : une pour les nœuds et une pour l'arbre lui-même.

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

class ArbreBinaire:
    def __init__(self, racine=None):
        self.racine = racine

    def est_vide(self):
        return self.racine is None

# Exemple de construction manuelle
#      A
#     / \
#    B   C
n_b = Noeud("B")
n_c = Noeud("C")
n_a = Noeud("A", n_b, n_c)
mon_arbre = ArbreBinaire(n_a)
```

## 4. Les Parcours d'Arbre

Parcourir un arbre, c'est visiter tous ses nœuds exactement une fois.

### Parcours en profondeur (DFS)
1.  **Prefixe :** Racine, puis sous-arbre gauche, puis sous-arbre droit.
2.  **Infixe :** Sous-arbre gauche, puis racine, puis sous-arbre droit.
3.  **Suffixe (Postfixe) :** Sous-arbre gauche, puis sous-arbre droit, puis racine.

### Parcours en largeur (BFS)
On visite les nœuds **niveau par niveau**, de gauche à droite, en utilisant une **file**.

## 5. Arbres Binaires de Recherche (ABR)

Un **ABR** est un arbre binaire où pour chaque nœud :
*   Toutes les clés du sous-arbre **gauche** sont inférieures ou égales à la clé du nœud.
*   Toutes les clés du sous-arbre **droit** sont supérieures ou égales à la clé du nœud.

**Propriété majeure :** Un parcours **infixe** d'un ABR donne les clés dans l'ordre croissant.

### Efficacité
La recherche, l'insertion et la suppression dans un ABR équilibré ont une complexité **logarithmique $O(\log n)$**, ce qui est bien plus performant qu'une liste pour de grandes collections.

***

## Exercices d'application

### Exercice 1 : Calcul de la taille
Compléter la fonction récursive pour calculer la taille d'un arbre.

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

def calculer_taille(noeud):
    if noeud is None:
        return 0
    else:
        # À compléter : 1 + taille sous-arbre gauche + taille sous-arbre droit
        return ...

# Tests
print(calculer_taille(None))  # Devrait afficher 0

racine_solo = Noeud(10)
print(calculer_taille(racine_solo))  # Devrait afficher 1

arbre_3 = Noeud(10, Noeud(5), Noeud(15))
print(calculer_taille(arbre_3))  # Devrait afficher 3

arbre_4 = Noeud(10, Noeud(5, Noeud(2)), Noeud(15))
print(calculer_taille(arbre_4))  # Devrait afficher 4
```

### Exercice 2 : Recherche dans un ABR
Écrire la méthode `chercher` pour un ABR.

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

def chercher(noeud, x):
    if noeud is None:
        return False
    if noeud.valeur == x:
        return True
    
    # À compléter : effectuer l'appel récursif à gauche ou à droite
    if x < noeud.valeur:
        return ...
    else:
        return ...

# Tests
# Construction de l'ABR :
#        10
#       /  \
#      5    15
#     / \
#    2   7
abr = Noeud(10, Noeud(5, Noeud(2), Noeud(7)), Noeud(15))

print(chercher(None, 10))  # Doit afficher False
print(chercher(abr, 10))  # Doit afficher True
print(chercher(None, 17))  # Doit afficher False
print(chercher(abr, 15))  # Doit afficher True
```

### Exercice 3 : Identifier un ABR
Parmi les deux suites de clés obtenues par parcours infixe, laquelle correspond à un ABR ?

```python
# Deux parcours infixes observés :
parcours_A = [5, 2, 8, 10, 15]
parcours_B = [2, 5, 8, 10, 15]

# 1. Quelle lettre ("A" ou "B") correspond au parcours infixe d'un ABR ?
reponse = "..."

# 2. Écrire la fonction est_triee(liste) permettant de vérifier si le parcours est croissant
def est_triee(liste):
    # Doit renvoyer True si la liste est strictement croissante, False sinon
    pass

print(est_triee(parcours_A))  # Doit afficher False
print(est_triee(parcours_B))  # Doit afficher True
```