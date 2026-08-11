# Chapitre 1 : Structurer les données

Ce chapitre explore comment organiser les données pour les manipuler efficacement. Il introduit la notion fondamentale de **Type Abstrait de Données (TAD)** (**Abstract Data Type - ADT**) qui permet de séparer l'utilisation d'une structure de sa réalisation technique.

## 1. Interface et Implémentation

Pour résoudre un problème informatique, on utilise des structures de données adaptées. Il est crucial de distinguer deux aspects :

*   **L'interface** (**Interface**) : C’est la « notice d’utilisation ». Elle définit l'ensemble des opérations (primitives) que l'on peut effectuer sur la structure (ex: ajouter, supprimer, tester si vide), sans dire comment elles sont codées.
*   **L’implémentation** (ou implantation) (**Implementation**) : C’est le code concret (en Python par exemple) qui réalise les opérations de l'interface. Une même interface peut avoir plusieurs implémentations différentes (ex: une pile faite avec une liste Python ou avec des objets).


## 2. Les Structures Linéaires

Les structures linéaires stockent les données les unes après les autres.

### A. Les Listes (simplement) chaînées (**Linked Lists**)
Une liste est une séquence ordonnée d'éléments. Sa définition est souvent récursive :

*   Une liste est soit **vide** (`nil`).
*   Soit composée d'une **tête** (**Head**) (le premier élément) et d'une **queue** (**Tail**) (qui est elle-même une liste contenant le reste des éléments).

**Primitives essentielles :** `creer_liste()`, `est_vide()`, `ajouter_en_tete(x)`, `tete()`, `queue()`.

### B. Les Piles (**Stacks**) - Mode LIFO
Une pile suit le principe **LIFO** (*Last In, First Out*) : le dernier élément arrivé est le premier à sortir (comme une pile d'assiettes).

*   On n'accède qu'à l'élément au **sommet** (**Top**).
*   **Utilisations :** Gestion de l'historique d'un navigateur, fonction "Annuler" (Ctrl+Z), parcours en profondeur d'un graphe.

**Primitives :** `creer_pile()`, `est_vide()`, `empiler(x)` (**push**), `depiler()` (**pop**), `sommet()` (**peek**).

### C. Les Files (**Queues**) - Mode FIFO
Une file suit le principe **FIFO** (*First In, First Out*) : le premier élément arrivé est le premier à sortir (comme une file d'attente au cinéma).

*   On ajoute à la **queue** (**Rear**) et on retire à la **tête** (**Front**).
*   **Utilisations :** File d'attente d'impression, gestion des processus, parcours en largeur d'un arbre/graphe.

**Primitives :** `creer_file()`, `est_vide()`, `enfiler(x)` (**enqueue**), `defiler()` (**dequeue**).


## 3. L'outil de base de l'implémentation objet : la Cellule

Pour construire ces structures en Programmation Orientée Objet, on utilise souvent une classe **Cellule** (**Node**) qui sert de maillon :

```python
class Cellule:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur   # La donnée stockée
        self.suivant = suivant # Lien vers la cellule suivante
```


## 4. Exercices d'application

### Exercice 1 : Manipulation de Pile
Soit une pile `P` initialement vide. On effectue les opérations suivantes :
`empiler(P, 5)`, `empiler(P, 3)`, `x = depiler(P)`, `empiler(P, 8)`, `empiler(P, 2)`, `depiler(P)`.
1. Quel est le contenu de la pile (du bas vers le haut) ?
2. Quelle est la valeur de `x` ?
3. Quel est l'élément au sommet de la pile à la fin ?

{{ IDE('01_exos_tad/exo1') }}

### Exercice 2 : FIFO vs LIFO
Vous gérez les dossiers de patients arrivant aux urgences.
1. Quelle structure de données garantit que le patient arrivé en premier sera vu en premier ?
2. Si vous utilisez l'autre structure à la place, quel problème cela pose-t-il ?

### Exercice 3 : Interface vs Implémentation
Un collègue a écrit une fonction `calculer_distance(chemin)` qui utilise une structure de type `Pile` pour stocker les étapes.

Si vous changez le code interne de la classe `Pile` (l'implémentation) pour le rendre plus rapide, mais que vous gardez les mêmes noms de méthodes (`empiler`, `depiler`), le code de votre collègue fonctionnera-t-il toujours ? Pourquoi ?

### Exercice 4 : Parenthésage (Défi)
Utilisez une pile pour écrire l'algorithme vérifiant si une expression est bien parenthésée (ex: `( ( ) )` est correct, `( ) ) (` ne l'est pas).
*   *Indice : On empile quand on voit `(` et on dépile quand on voit `)`. L'expression est correcte si la pile est vide à la fin et qu'on n'a jamais essayé de dépiler une pile vide.*

{{ IDE('01_exos_tad/exo4') }}


## 5. Complément : bableau et liste chaînée

La distinction entre le **tableau** (souvent implémenté comme un tableau dynamique en Python via le type `list`) et la **liste chaînée** est fondamentale en informatique, car leurs performances diffèrent selon l'opération effectuée.

### 5.1. Accès aux données (Lecture par index)

*   **Tableau** : Il permet un **accès direct** à n'importe quel élément grâce à son index. La complexité est en **temps constant $O(1)$**, car l'adresse mémoire de l'élément se calcule instantanément.

*   **Liste chaînée** : On n'a accès directement qu'au premier élément (la tête). Pour atteindre le $i$-ème élément, il faut parcourir tous les maillons un par un. La complexité est donc **linéaire $O(n)$**.

### 5.2. Ajout et retrait d'éléments
Les performances varient radicalement selon l'endroit où l'on modifie la structure :

*   **En fin de structure** :
    *   **Tableau** : L'ajout (`append`) ou le retrait (`pop`) en fin de tableau est très efficace, s'effectuant en **temps constant $O(1)$**.
    *   **Liste chaînée** : Sans pointeur vers la fin, il faut parcourir toute la liste pour ajouter un élément, ce qui est en $O(n)$.

*   **En début de structure** :
    *   **Tableau** : C'est son point faible. Retirer le premier élément (`pop(0)`) oblige à décaler tous les autres éléments d'une case vers la gauche. Cette opération est donc en **temps linéaire $O(n)$**.
    *   **Liste chaînée** : C'est sa force. L'ajout ou la suppression en tête de liste ne demande que de modifier quelques liens (pointeurs) entre les cellules. L'opération est en **temps constant $O(1)$**.

### 5.3. Utilisation de la mémoire

*   **Tableau** : Les données sont stockées de manière contiguë. Cependant, en tant que "tableau dynamique", Python réserve parfois plus de place que nécessaire pour anticiper les futurs ajouts.

*   **Liste chaînée** : Chaque élément est encapsulé dans une **cellule** qui contient non seulement la valeur, mais aussi l'**adresse** de la cellule suivante. Cela consomme plus de mémoire par élément à cause du stockage de ces liens (pointeurs).

### Résumé des performances

| Opération | Tableau (Python `list`) | Liste chaînée (Objet `Cellule`) |
| :--- | :--- | :--- |
| **Accès par index** | **$O(1)$ (très rapide)** | $O(n)$ (lent) |
| **Ajout/Retrait en tête** | $O(n)$ (lent) | **$O(1)$ (très rapide)** |
| **Ajout/Retrait en queue**| **$O(1)$ (très rapide)** | $O(n)$ (ou $O(1)$ si optimisé) |
| **Recherche de valeur** | $O(n)$ | $O(n)$ |

**En conclusion**, le choix dépend de l'usage : si on a besoin besoin d'accéder souvent à des éléments au milieu, le **tableau** est préférable. Si on doit fréquemment ajouter ou retirer des éléments au début (comme pour une file d'attente), la **liste chaînée** est plus performante.

## 6. Complément : les dictionnaires

Les dictionnaires (**Dictionaries**) offrent plusieurs avantages significatifs par rapport aux listes, principalement en termes de structure de données et de rapidité d'accès aux informations.

Voici les principaux points de différenciation.

### 6.1. Accès sémantique par Clés (vs Index numériques)
Contrairement aux listes qui sont des structures **ordonnées** accédées par un index entier (0, 1, 2...), un dictionnaire associe des **clés** à des **valeurs**. 

*   Cette structure est plus intuitive pour modéliser des situations du monde réel, comme un dictionnaire de traduction (français-anglais) ou une base de données où l'on cherche une information par un nom plutôt que par sa position.

*   Les opérations de base incluent l'ajout d'un couple clé-valeur, la suppression d'une clé et la modification de la valeur associée.

### 6.2. Performance de recherche (Complexité)
C'est l'avantage technique majeur. La performance d'un dictionnaire dépend de son **implantation** :

*   **Recherche dans une liste** : Pour trouver si une valeur existe dans une liste, il faut généralement la parcourir entièrement. La complexité est donc **linéaire $O(n)$**.

*   **Recherche dans un dictionnaire (Table de hachage)** : En Python, les dictionnaires utilisent une **fonction de hachage** qui transforme la clé en un indice directement. Cela permet d'accéder à la valeur associée sans avoir à parcourir toute la structure. L'accès est donc extrêmement rapide, se faisant en **temps constant $O(1)$**, peu importe la taille du dictionnaire.

### 6.3. Flexibilité et Modélisation complexe
Les dictionnaires sont particulièrement adaptés pour représenter des structures de données non linéaires ou volumineuses :

*   **Représentation de Graphes** : On utilise souvent des dictionnaires pour implémenter des **listes d'adjacences**. Chaque sommet est une clé, et la valeur associée est la liste de ses voisins. C'est une méthode compacte qui ne code que les relations existantes.

*   **Prétraitement algorithmique** : Dans l'algorithme de recherche textuelle de **Boyer-Moore**, un dictionnaire est utilisé pour stocker la position la plus à droite de chaque caractère du motif recherché. Cela permet de calculer instantanément le décalage nécessaire lors d'une recherche, améliorant grandement l'efficacité.

*   **Manipulation de données API** : Les réponses des API (souvent au format JSON) sont naturellement converties en dictionnaires Python, ce qui facilite leur manipulation et le filtrage des données.

**En résumé**, si la liste est idéale pour stocker une suite ordonnée d'éléments, le dictionnaire est indispensable pour **rechercher et modifier rapidement des données** grâce à un système d'association clé-valeur performant.

***