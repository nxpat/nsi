# Arbres binaires de recherche (ABR)

Voici plusieurs types d'**arbres binaires de recherche (ABR)**, allant d'exemples numériques simples à des structures plus complexes pour stocker des objets ou des mots. Un ABR est défini par la propriété suivante : pour tout nœud, les clés du sous-arbre gauche sont inférieures ou égales à la sienne, et celles du sous-arbre droit lui sont supérieures ou égales.

### 1. Exemples avec des clés numériques
C'est l'utilisation la plus courante pour illustrer le concept. Les sources montrent qu'un même ensemble de nombres peut être organisé en plusieurs ABR différents selon l'ordre d'insertion :

*   **Ensemble `{2, 3, 5, 7, 9, 11, 13}` :** cet ensemble peut être représenté par un arbre équilibré (plus efficace pour la recherche) ou un arbre "dégénéré" (ressemblant à une liste), ce qui impacte le temps de recherche moyen.
*   **ABR avec doublons :** un exemple montre un arbre où la valeur 6 apparaît deux fois (une fois à la racine et une fois dans le sous-arbre gauche), illustrant que les ABR peuvent accepter des clés non distinctes.
*   **Structure complexe :** un exemple détaillé présente un arbre de racine **8**, avec un fils gauche **4** (ayant pour enfants **3** et **6**) et un fils droit **12** (ayant pour enfants **9** et **14**).

### 2. Exemples avec des chaînes de caractères
Les ABR ne se limitent pas aux nombres ; ils peuvent utiliser n'importe quel type de données pourvu qu'elles soient comparables (ordre alphabétique pour les textes).

*   **Arbre de lettres :** un document illustre un ABR stockant les lettres **B, E, G, F, H, E** organisées selon l'ordre alphabétique.
*   **Arbres lexicographiques :** ils sont utilisés pour représenter des dictionnaires, par exemple un dictionnaire de mots commençant par la lettre "A".

### 3. Exemples avec des objets complexes (POO)
Grâce à la programmation orientée objet, on peut stocker des instances de classes personnalisées dans un ABR, à condition de définir les opérateurs de comparaison (`<`, `>`, `==`).

*   **Classe `Personne` :** un exemple montre comment classer des individus soit par leur identifiant (`id`), soit par un critère multicritère (nom, puis prénom, puis id).
*   **Indexation de collections :** les ABR sont utilisés pour indexer des bases de données de films, permettant des recherches rapides par titre ou par prix.

### 4. Applications concrètes citées
Les sources mentionnent plusieurs domaines fondamentaux où ces arbres de recherche sont appliqués :
*   **Gestion de fichiers :** organisation et recherche de fichiers sur un disque dur.

*   **Bases de données :** gestion des adhérents d'une bibliothèque (recherche par nom).
*   **Web :** le **DOM** (Document Object Model) d'une page HTML est structuré sous forme d'arbre de racine `<html>`.
*   **Moteurs de recherche :** bien que plus complexe, l'algorithme *PageRank* est une application des structures hiérarchiques et relationnelles.