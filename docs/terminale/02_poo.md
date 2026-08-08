# Chapitre 2 : Programmation Orientée Objet (POO)

Ce chapitre introduit un nouveau **paradigme de programmation** qui permet de structurer les programmes en regroupant des données et les fonctions qui les manipulent au sein d'entités appelées **objets**.

## 1. Concepts fondamentaux

### La notion d'Objet et de Classe
*   **Classe** : C’est un « moule » ou un modèle ou un plan de fabrication qui définit la structure des objets. Elle précise quels seront les **attributs** (données) et les **méthodes** (fonctions) communs à tous les objets de ce type.
*   **Objet (ou Instance)** : C’est une entité concrète créée à partir d’une classe. On peut créer plusieurs instances (objets) distinctes à partir d'une même classe.

### Le vocabulaire technique
*   **Attributs** : Ce sont les variables attachées à un objet qui définissent son état (ex: la longueur d'un rectangle).
*   **Méthodes** : Ce sont les fonctions définies à l'intérieur d'une classe qui agissent sur l'objet (ex: calculer l'aire).
*   **Constructeur (`__init__`)** : C'est une méthode spéciale appelée automatiquement lors de la création d'un objet pour initialiser ses attributs.
*   **Le mot-clé `self`** : Dans la définition de la classe, `self` représente l'instance de l'objet en cours de manipulation.

---

## 2. Syntaxe en Python

Voici l'exemple classique d'une classe représentant un **Rectangle** :

```markdown
class Rectangle:
    """Classe définissant un rectangle par sa longueur et sa largeur."""
    
    def __init__(self, longueur, largeur):
        # Initialisation des attributs
        self.longueur = longueur
        self.largeur = largeur

    def calcule_aire(self):
        # Méthode utilisant les attributs de l'objet via self
        return self.longueur * self.largeur
```
.

### Utilisation (Instanciation)
Pour créer et utiliser un objet :
```python
# Création d'une instance de la classe Rectangle
rect1 = Rectangle(10, 5)

# Accès aux attributs
print(rect1.longueur) # Affiche 10

# Appel d'une méthode
aire = rect1.calcule_aire()
print(aire) # Affiche 50
```
.

---

## 3. Points importants à retenir

### Composition d'objets
Un attribut d'un objet peut lui-même être un autre objet. C'est une notion essentielle pour préparer l'étude de structures de données plus complexes comme les **listes chaînées** ou les **arbres**.

**Exemple :**
Une classe `Personne` peut posséder un attribut `chien` qui est une instance d'une classe `Chien`.

### Interface et Implantation
*   **L'interface** est l'ensemble des méthodes qu'un utilisateur de la classe peut appeler sans avoir besoin de connaître le code interne.
*   **L'implantation** est la manière dont le développeur a écrit le code à l'intérieur de la classe.
Cette séparation permet de modifier l'implantation (pour la rendre plus rapide par exemple) sans que l'utilisateur n'ait à changer son propre programme.

### Méthodes spéciales (Hors programme mais utiles)
*   `__str__` : Permet de définir ce qui s'affiche quand on utilise `print(objet)`.
*   `__eq__` : Permet de définir comment comparer deux objets avec l'opérateur `==`.

---

## 4. Exercice

{{ IDE('02_exos_poo/personnage') }}

---

## 5. Pourquoi utiliser la POO ?

L'utilisation de la **Programmation Orientée Objet (POO)** répond à plusieurs besoins dans le développement logiciel moderne :

1.  **Modélisation intuitive du monde réel** : La POO permet de concevoir des programmes en utilisant des concepts proches de la réalité. On définit des **classes** (**Classes**) qui servent de plans pour créer des **objets** (**Objects**) ayant leurs propres caractéristiques (**attributs** - **Attributes**) et comportements (**méthodes** - **Methods**). Par exemple, modéliser un rectangle avec sa longueur et sa largeur est plus naturel qu'utiliser des variables isolées.

2.  **Séparation de l'interface et de l'implantation** : C'est l'un des points les plus importants. Un utilisateur de la classe n'a besoin de connaître que l'**interface** (**Interface**) — c'est-à-dire les méthodes disponibles — sans se soucier de la manière dont le code est écrit à l'intérieur (**implantation** - **Implementation**). Cela permet au développeur de modifier ou d'optimiser l'implantation sans que le programme de l'utilisateur ne cesse de fonctionner.

3.  **Encapsulation et sécurité du code** : L'**encapsulation** (**Encapsulation**) permet de regrouper les données et les fonctions qui les manipulent, protégeant ainsi l'état interne de l'objet . Elle aide à limiter les erreurs en empêchant des modifications accidentelles de données sensibles.

4.  **Modularité et Réutilisabilité** : Le code est découpé en briques logiques indépendantes (**modularité** - **Modularity**) . Une classe bien conçue peut être réutilisée dans de nombreux autres projets ou via des **bibliothèques** (**Libraries**) et des **API** (**Application Programming Interfaces**) .

5.  **Gestion des structures de données complexes** : La POO est particulièrement adaptée lorsqu'on doit manipuler des types de données fortement structurés. Elle facilite la création de structures comme les **listes chaînées** (**Linked Lists**), les **piles** (**Stacks**) ou les **files** (**Queues**) en encapsulant chaque maillon dans un objet « Cellule ».

6.  **Facilité de mise au point** : Découper un programme en petites méthodes facilite l'écriture de **tests unitaires** (**Unit Tests**) et le **débogage** (**Debugging**). Par exemple, définir une méthode spéciale `__str__` permet d'afficher facilement l'état d'un objet pour vérifier son contenu.

---

## 6. Mots-clés essentiels de la POO (Français/Anglais)

Voici les termes techniques fréquemment rencontrés en **Programmation Orientée Objet (POO)** (**Object-Oriented Programming - OOP**) :

*   **Classe** (**Class**) : Le moule ou le plan de fabrication.
*   **Objet** ou **Instance** (**Object** / **Instance**) : L'entité concrète créée à partir d'une classe.
*   **Attribut** (**Attribute** / **Property**) : Une variable attachée à l'objet définissant son état.
*   **Méthode** (**Method**) : Une fonction interne à la classe agissant sur l'objet.
*   **Constructeur** (**Constructor** / **Initializer**) : La méthode spéciale (`__init__` en Python) appelée à la création de l'objet.
*   **Encapsulation** (**Encapsulation**) : Le principe de regrouper données et méthodes en restreignant l'accès direct aux attributs.
*   **Interface** (**Interface**) : L'ensemble des moyens de communication avec un objet.
*   **Implantation** ou **Implémentation** (**Implementation**) : Le code concret qui réalise les opérations de la classe.
*   **Héritage** (**Inheritance**) : (Hors programme NSI) Capacité d'une classe à hériter des caractéristiques d'une autre.
*   **Polymorphisme** (**Polymorphism**) : (Hors programme NSI) Capacité d'utiliser une même interface pour des types d'objets différents.


Illustration de l'héritage et du polymorphisme à partir de notre exemple de la classe `Rectangle`, pour comprendre comment la POO est utilisée dans l'industrie.

### 1. L'Héritage (Inheritance)
L'héritage permet de créer une nouvelle classe à partir d'une classe existante. La nouvelle classe (classe fille) récupère les attributs et les méthodes de la classe parente.

**Exemple :** Un **Carré** est un cas particulier de **Rectangle** où la longueur est égale à la largeur.

```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calcule_aire(self):
        return self.longueur * self.largeur

# La classe Carre hérite de Rectangle
class Carre(Rectangle):
    def __init__(self, cote):
        # On appelle le constructeur de la classe parente (Rectangle)
        super().__init__(cote, cote)
```

### 2. Le Polymorphisme (Polymorphism)
Le polymorphisme est la capacité d'appeler une méthode portant le même nom sur des objets de types différents, chaque objet l'exécutant à sa manière.

**Exemple :** Imaginons une classe `Cercle`. Si nous mettons différents objets de forme dans une liste, nous pouvons calculer leurs aires sans nous soucier de leur type précis.

```python
import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcule_aire(self):
        return math.pi * (self.rayon ** 2)

# Utilisation du polymorphisme
formes = [Rectangle(10, 5), Carre(4), Cercle(3)]

for f in formes:
    # Python appelle la "bonne" méthode calcule_aire selon l'objet
    print(f"Aire : {f.calcule_aire()}")
```

---

## 7. La POO dans les autres langages courants

La plupart des langages modernes utilisent la POO, mais avec des philosophies différentes concernant la "sécurité" et l'encapsulation.

*   **Java** : C'est le langage "tout objet" par excellence. Contrairement à Python où l'encapsulation est une convention, Java impose des mots-clés (`private`, `public`) pour restreindre strictement l'accès aux données.

*   **C++** : Langage très utilisé pour la performance (jeux vidéo, systèmes). Il a introduit la POO par-dessus le langage C. Il permet un contrôle très fin sur la mémoire, mais est beaucoup plus complexe à manipuler que Python.

*   **JavaScript** : Utilisé pour le web. Il utilisait historiquement un système de "prototypes", mais possède aujourd'hui une syntaxe `class` très proche de Python pour faciliter la structuration du code.

*   **Swift** (Apple) : Le langage pour les applications iPhone. Il utilise une POO moderne et sécurisée, très axée sur les "Protocoles" (une forme d'interface avancée).

*   **Rust** : Un langage moderne qui n'utilise pas de "classes" au sens traditionnel. Il utilise des `structs` pour les données et des `traits` pour les comportements. C'est une approche alternative à l'héritage classique, très appréciée pour sa sécurité mémoire.

*   **Fortran** : Historiquement l'un des premiers langages pour le calcul scientifique. Bien que très ancien et initialement procédural, il a intégré des concepts d'objets dans ses versions récentes (depuis Fortran 2003) pour gérer des simulations complexes.

**À retenir :** Si Python est privilégié en NSI pour sa simplicité et sa concision, les concepts d'objets, de méthodes et d'attributs sont universels et se retrouvent dans presque tous les environnements de développement professionnels.