# Chapitre 4 : SGBD Relationnels et SQL

SGBD = « Système de gestion de bases de données » – Logiciel qui enregistre, manipule et gère les données dans une base de données.

DBMS = “Database Management System”

## 1. Le Modèle Relationnel

Le modèle relationnel organise les données sous forme de **tables** (appelées **relations**).

### Concepts clés

*   **Relation** : Une table composée de lignes et de colonnes.
*   **Attribut** : Le nom d'une colonne (ex: "Nom", "Age").
*   **Domaine** : Le type de données autorisé pour un attribut (Entier, Chaîne de caractères, etc.).
*   **n-uplet (ou enregistrement)** : Une ligne de la table correspondant à une entrée de données.
*   **Clé primaire** : Un attribut (ou groupe d'attributs) dont la valeur permet d'identifier de manière unique chaque ligne d'une table. Elle ne peut pas être vide (`NOT NULL`).
*   **Clé étrangère** : Un attribut dans une table qui fait référence à la clé primaire d'une autre table, permettant d'établir des liens entre elles.

### Contraintes d'intégrité
Pour garantir la cohérence des données, on définit des contraintes :

*   **NOT NULL** : La valeur doit obligatoirement être renseignée.
*   **UNIQUE** : Deux lignes ne peuvent pas avoir la même valeur pour cet attribut.
*   **CHECK** : Vérifie une condition booléenne (ex: `AGE >= 0`).

Voici l'ajout de la section demandée pour le résumé du **Chapitre 4 : SGBD Relationnels**, formatée en Markdown pour votre page GitHub Pages.

### Les types de relations entre tables

Dans un schéma relationnel, les tables ne sont pas isolées mais liées entre elles par des références, notamment via les **clefs étrangères**. On distingue principalement deux types de relations :

#### A. Relations « un-à-plusieurs » (one-to-many)
*   **Principe** : Une ligne d’une table A peut être liée à **plusieurs** lignes d’une autre table B.
*   **Mise en œuvre** : La table B possède une **clé étrangère** qui référence la clé primaire de la table A.
*   **Exemple** : Un auteur (table A) peut écrire plusieurs livres (table B) ; chaque ligne de la table `Livres` contiendra une colonne `id_auteur` pointant vers l'identifiant unique de l'auteur.

#### B. Relations « plusieurs-à-plusieurs » (many-to-many)
*   **Principe** : Une ligne de la table A peut être liée à **plusieurs** lignes de la table B **et inversement**.
*   **Mise en œuvre** : Comme il est impossible de stocker plusieurs valeurs dans une seule cellule, on utilise une **table d’association** (ou table de jointure). Cette table intermédiaire contient au moins deux clés étrangères : l’une pointant vers la table A, l’autre vers la table B.
*   **Exemple** : Des étudiants (table A) peuvent suivre plusieurs cours (table B) et chaque cours est suivi par plusieurs étudiants. Une table `Inscriptions` (table C) fera le lien en stockant les couples `(id_etudiant, id_cours)`.

Cette structuration des données est essentielle pour éviter la **redondance** et garantir l'**intégrité référentielle** de la base de données. Lors d'une interrogation, on utilise la clause `JOIN` en SQL pour reconstituer les informations liées entre ces tables.

---

## 2. Le Langage SQL : Manipulation et Définition

Le SQL (**Structured Query Language**) est le langage standard pour interagir avec un SGBD.

### Création et Modification (LDD - Langage de Définition de Données) :
*   `CREATE TABLE NomTable (...)` : Crée une nouvelle table avec ses attributs et contraintes.
*   `DROP TABLE NomTable` : Supprime une table.

### Mise à jour des données (LMD - Langage de Manipulation de Données) :
*   **Insertion** : `INSERT INTO Table VALUES (val1, val2, ...)`
*   **Suppression** : `DELETE FROM Table WHERE condition` (Attention : sans `WHERE`, toute la table est vidée).
*   **Modification** : `UPDATE Table SET Attribut = nouvelle_valeur WHERE condition`.

---

## 3. L'Interrogation des Données : La clause SELECT

L'extraction de données se fait principalement avec la commande `SELECT`.

### Structure de base :
```sql
SELECT attribut1, attribut2 -- Projection : choix des colonnes
FROM Table                  -- Origine des données
WHERE condition             -- Sélection : choix des lignes
ORDER BY attribut ASC/DESC  -- Tri des résultats
```
*   `SELECT *` : Sélectionne toutes les colonnes.
*   `SELECT DISTINCT` : Élimine les doublons dans les résultats.

### Jointures :
La jointure permet de combiner deux tables ayant un attribut commun (souvent une clé étrangère).
```sql
SELECT * FROM Table1 
JOIN Table2 ON Table1.id = Table2.id_reference;
```

### Fonctions d'agrégation :
Elles permettent de réaliser des calculs sur un ensemble de lignes :

*   `COUNT(*)` : Compte le nombre de lignes.
*   `SUM(attribut)` : Somme des valeurs.
*   `AVG(attribut)` : Moyenne des valeurs.
*   `MIN()` / `MAX()` : Valeurs minimale et maximale.

---

## 4. Utilisation en Mode Programme avec Python

En Python, on utilise souvent la bibliothèque `sqlite3` pour interagir avec une base de données.

### Étapes principales :
1.  **Connexion** : `conn = sqlite3.connect("base.db")`
2.  **Création d'un curseur** : `cur = conn.cursor()`
3.  **Exécution** : `cur.execute("REQUETE SQL")`
4.  **Récupération** : `resultats = cur.fetchall()` (renvoie une liste de tuples).
5.  **Validation** : `conn.commit()` (indispensable pour enregistrer les modifications `INSERT`, `UPDATE`, `DELETE`).
6.  **Fermeture** : `conn.close()`

### Sécurité : Injections SQL :
Il ne faut jamais construire une requête par concaténation de chaînes avec des variables utilisateurs. On utilise des **requêtes paramétrées** avec le symbole `?` pour éviter que des utilisateurs malveillants n'injectent du code SQL destructeur.
*   *Exemple sûr* : `cur.execute("SELECT * FROM User WHERE nom = ?", (nom_utilisateur,))`.

---

## 5. Exercices d'application

### Exercice 1 : Modèle relationnel
Soit la relation `Livre (id_livre INT, titre TEXT, auteur TEXT, id_editeur INT)`.

1. Quelle est la clé primaire probable de cette relation ?
2. Si `id_editeur` fait référence à une table `Editeur`, comment appelle-t-on cet attribut ?

### Exercice 2 : Requêtes SQL
On considère une table `Eleves (id, nom, prenom, age, classe)`. Écrire les requêtes SQL pour :

1. Afficher le nom et le prénom de tous les élèves de la classe 'Te1'.
2. Afficher l'âge moyen des élèves de la table.
3. Supprimer l'élève dont l'id est 42.

### Exercice 3 : Python et SQL
Compléter le script Python suivant pour récupérer tous les titres de la table `Livre` :
```python
import sqlite3
conn = sqlite3.connect("bibliotheque.db")
cur = conn.cursor()

# À compléter
cur.execute("................................")
livres = cur................()

for l in livres:
    print(l)

conn.close()
```

---

## 6. Complément : jointure et produit cartésien

Dans le modèle relationnel, la différence entre un produit cartésien et une jointure réside essentiellement dans le **filtrage des données** et la **cohérence logique** du résultat obtenu.

### 6.1. Le Produit Cartésien
Le produit cartésien de deux tables est une opération qui consiste à créer toutes les paires possibles de lignes (n-uplets) entre ces deux tables.

*   **Nombre de lignes :** Si une table $t_1$ possède $n_1$ lignes et une table $t_2$ possède $n_2$ lignes, le produit cartésien contiendra **$n_1 \times n_2$** lignes.
*   **Contenu :** Il associe chaque enregistrement de la première table à absolument tous les enregistrements de la seconde, sans aucun critère de correspondance. Par exemple, si on combine trois tables de 5, 3 et 3 lignes, on obtient 45 lignes, dont beaucoup n'ont aucun sens logique (comme associer un abonné à tous les livres de la bibliothèque, même ceux qu'il n'a pas empruntés).

### 6.2. La Jointure
La jointure est une opération plus précise qui combine deux tables en faisant correspondre les éléments selon une **condition spécifique**.

*   **Condition de jointure :** Le plus souvent, on utilise un attribut commun (comme une **clé étrangère** faisant référence à une **clé primaire**) pour lier les lignes qui ont un rapport entre elles. 
*   **Syntaxe SQL :** Elle utilise généralement le mot-clé `JOIN` suivi de la clause `ON` pour définir l'attribut de liaison.

### 6.3. Comparaison et efficacité

*   **Lien théorique :** D'un point de vue théorique, une jointure peut être vue comme un **produit cartésien suivi d'une sélection** (filtre `WHERE`) qui ne garde que les lignes satisfaisant la condition de correspondance.
*   **Performance :** Calculer un produit cartésien complet avant de le filtrer est très inefficace, surtout sur de grandes bases de données. Les Systèmes de Gestion de Bases de Données (SGBD) utilisent des **optimiseurs de requêtes** pour réaliser la jointure directement, évitant ainsi de générer inutilement toutes les combinaisons possibles de lignes.

En résumé, alors que le **produit cartésien** est une combinaison brute et exhaustive de toutes les lignes, la **jointure** est une combinaison intelligente et filtrée qui ne conserve que les données liées logiquement entre elles.

---

## 7. Complément : Jointure avec 3 tables

Pour réaliser une jointure entre trois tables en SQL, le principe consiste à **enchaîner les clauses `JOIN`** les unes à la suite des autres.

### 7.1. Syntaxe générale
La structure de la requête suit ce modèle :
```sql
SELECT *
FROM Table1
JOIN Table2 ON Table1.cle_primaire = Table2.cle_etrangere
JOIN Table3 ON Table2.autre_cle = Table3.cle_primaire;
```

### 7.2. Fonctionnement logique
L'opération se déroule par étapes :

*   Le SGBD commence par effectuer la jointure entre la **Table 1** et la **Table 2** selon la première condition spécifiée.
*   Le résultat intermédiaire (une table temporaire combinant les colonnes des deux premières) est ensuite joint à la **Table 3** selon la seconde condition.

### 7.3. Exemple
Si l'on considère une base de données de bibliothèque avec les tables `Abonne`, `Emprunt` et `Livre`, la requête pour lier les trois et savoir quel abonné a emprunté quel titre est la suivante :

```sql
SELECT *
FROM Abonne
JOIN Emprunt ON Abonne.ida = Emprunt.ida
JOIN Livre ON Emprunt.idL = Livre.idL;
```

Dans cet exemple :

*   On lie d'abord l'abonné à ses emprunts via l'identifiant de l'abonné (`ida`).
*   On lie ensuite l'emprunt au livre correspondant via l'identifiant du livre (`idL`).

### 7.4. Points d'attention

*   **Conditions de jointure** : Il est impératif de définir précisément les attributs de liaison (souvent des clés étrangères faisant référence à des clés primaires) pour éviter de créer un produit cartésien, ce qui générerait une table immense et incohérente.
*   **Ambiguïté des noms** : Si deux tables possèdent des colonnes avec le même nom, il faut les préfixer par le nom de la table (ex: `Abonne.nom`) pour que le SGBD puisse les distinguer.
*   **Nombre de lignes** : Le résultat final ne contiendra que les lignes qui satisfont **toutes** les conditions de jointure simultanément. Par exemple, si on joint trois tables, seules les données ayant des correspondances dans les trois seront affichées.

---

## 8. Complément : Fonctions d'aggrégation

Les fonctions d'**agrégation** en SQL permettent de résumer un ensemble de données en une seule valeur numérique, comme une somme, une moyenne ou un décompte.

Voici trois exemples de requêtes utilisant l'agrégation, les deux premiers exemples utilisent la relation `Eleves (id, nom, prenom, age, classe)`.

### 8.1. Exemple sur les abonnés
Pour obtenir des statistiques sur l'âge des abonnés, on peut utiliser la requête suivante :
```sql
SELECT COUNT(*) AS nb_total, 
       COUNT(DISTINCT age) AS nb_ages_differents, 
       AVG(age) AS age_moyen, 
       SUM(age) AS somme_ages
FROM Abonne;
```

*   **`COUNT(*)`** : Compte le nombre total de lignes (abonnés).
*   **`COUNT(DISTINCT age)`** : Compte le nombre de valeurs d'âge différentes.
*   **`AVG(age)`** : Calcule la moyenne d'âge.
*   **`SUM(age)`** : Calcule la somme de tous les âges.

### 8.2. Exemple sur les auteurs
Pour trouver les bornes alphabétiques des auteurs présents dans la base :
```sql
SELECT MIN(auteur), MAX(auteur)
FROM Livre;
```

*   **`MIN(auteur)`** et **`MAX(auteur)`** : Retournent respectivement le premier et le dernier auteur dans l'ordre alphabétique.

### 8.3. Exemple avec jointure (Cas d'une agence de voyage)
L'agrégation peut aussi s'appliquer après une jointure entre deux tables pour obtenir des statistiques croisées. 

Soit deux tables liées par une relation *"un-à-plusieurs"* (un vol peut avoir plusieurs passagers) :

* Table `Vols` (renommée `V` dans la requête) :
   * `id` : La clef primaire identifiant de manière unique chaque vol.
   * `depart` : L'aéroport de départ (ex: 'CdG').
   * `arrivee` : L'aéroport de destination (ex: 'JFK').
* Table `Passagers` (renommée `P` dans la requête) :
   * `idV` : Une clef étrangère qui fait référence à `V.id`. C'est elle qui permet de savoir dans quel `vol se trouve chaque passager.
   * `prix` : L'attribut stockant le montant payé pour le billet.

Par exemple, pour compter le nombre de passagers et la somme des prix des billets pour un vol spécifique :
```sql
SELECT COUNT(*), SUM(P.prix)
FROM Vols AS V
JOIN Passagers AS P ON V.id = P.idV
WHERE depart = 'CdG' OR arrivee = 'JFK';
```

Dans cet exemple, le SGBD calcule le nombre de billets vendus et le chiffre d'affaires total pour les trajets sélectionnés.

**Note importante :** Lorsqu'on utilise une fonction d'agrégation dans une clause `SELECT`, on ne peut pas afficher en même temps un attribut individuel (comme le nom d'un abonné) sans utiliser de clause de groupement (comme `GROUP BY`), car l'agrégation renvoie une seule ligne alors que l'attribut pourrait en avoir plusieurs.

---

## 9. Complément : La clause `GROUPE_BY` avec les aggrégations

La clause **`GROUP BY`** permet de partitionner les lignes d'une table en groupes ayant des valeurs identiques pour une ou plusieurs colonnes données, afin d'appliquer une fonction d'agrégation à chaque groupe séparément.

### 9.1. Fonctionnement logique
Alors qu'une agrégation classique (comme `SELECT AVG(age) FROM Abonne`) renvoie une **valeur unique** pour toute la table, le `GROUP BY` permet d'obtenir un résultat par "catégorie". 

*   **Partitionnement** : Le SGBD rassemble toutes les lignes qui partagent la même valeur dans la colonne spécifiée.
*   **Calcul** : La fonction d'agrégation (`COUNT`, `SUM`, `AVG`, etc.) est calculée pour chaque groupe d'enregistrements ainsi formé.

### 9.2. Syntaxe SQL
La structure standard d'une telle requête est la suivante :

```sql
SELECT colonne_de_groupement, FONCTION_AGREGATION(colonne_calculée)
FROM Nom_Table
GROUP BY colonne_de_groupement;
```

### 9.3. Exemples d'application

*   **Compter les abonnés par âge** (en utilisant la table `Abonne`) :
    ```sql
    SELECT age, COUNT(*) 
    FROM Abonne 
    GROUP BY age;
    ```
    *Résultat : Une liste affichant chaque âge présent dans la table et le nombre d'abonnés correspondant.*

*   **Calculer le prix total des billets par ville de départ** (en utilisant la table `Vols`) :
    ```sql
    SELECT depart, SUM(prix)
    FROM Vols
    JOIN Passagers ON Vols.id = Passagers.idV
    GROUP BY depart;
    ```

### 9.4. La clause `GROUP BY` associée à la fonction `COUNT(*)`

La clause **`GROUP BY`** associée à la fonction **`COUNT(*)`** permet de partitionner les lignes d'une table en groupes et de compter le nombre d'enregistrements dans chaque groupe.

### Exemple : Compter le nombre d'abonnés par âge

La table **Abonne** contient les colonnes `ida`, `nom` et `age`.

Si on souhaite savoir combien d'abonnés ont 17 ans, 18 ans, etc., on peut utiliser la requête suivante :

```sql
SELECT age, COUNT(*) AS nombre_abonnes
FROM Abonne
GROUP BY age;
```

**Explication du fonctionnement :**

1.  **Groupement** : Le SGBD parcourt la table et rassemble tous les n-uplets (lignes) qui ont la même valeur dans la colonne `age`.
2.  **Comptage** : Pour chaque groupe formé (par exemple, le groupe des "17 ans"), la fonction `COUNT(*)` calcule le nombre de lignes présentes.
3.  **Résultat** : La requête affiche une ligne pour chaque âge distinct, accompagnée du nombre total d'abonnés correspondant.

### Point de vigilance (Standard SQL)
Il est impératif que chaque attribut figurant dans la clause `SELECT` soit soit une fonction d'agrégation (comme `COUNT`), soit mentionné explicitement dans la clause `GROUP BY`. Dans l'exemple ci-dessus, `age` est dans le `SELECT` et est donc obligatoirement utilisé pour le groupage. 

Bien que SQLite puisse parfois tolérer des écarts, le respect de cette règle est essentiel pour garantir que la requête ait un sens logique et soit portable sur d'autres systèmes.

*Le programme de Terminale NSI précise que l'on peut manipuler les fonctions d'agrégation sans nécessairement utiliser les clauses `GROUP BY` et `HAVING` pour rester sur des cas simples de traitement global de table.*

---

## 10. Complément : Gestion de l'ambiguïté des noms de colonnes

Pour gérer l'ambiguïté des noms de colonnes, particulièrement lors de requêtes impliquant plusieurs tables (comme les jointures), il est nécessaire de **qualifier les attributs** ou d'utiliser des **alias**.

Voici quelques méthodes :

### 10.1. La qualification des noms (Préfixage)
Dès qu'une requête manipule plusieurs tables, il est préférable de faire précéder le nom de la colonne par le nom de la table, séparés par un point.

*   **Format** : `NomTable.NomAttribut`
*   **Exemple** : `Abonne.ida` au lieu de simplement `ida`.
*   **Pourquoi ?** Sans cela, le SGBD (comme SQLite) risque de renvoyer une erreur du type **"ambiguous column name"** s'il trouve le même nom d'attribut dans plusieurs tables jointes.

### 10.2. Les alias de tables
Pour rendre les requêtes plus lisibles et plus courtes, on peut donner un **alias** (un surnom) à une table dans la clause `FROM` ou `JOIN` à l'aide du mot-clé `AS` (optionnel mais recommandé).

*   **Exemple** : `FROM Abonne AS A, Emprunt AS E`.
*   Une fois l'alias défini, on peut l'utiliser pour qualifier les colonnes : `SELECT A.nom, E.idL`.

### 10.3. Les alias de colonnes
Il arrive que l'on veuille distinguer deux colonnes portant le même nom dans le **résultat final** de la requête, ou simplement renommer le titre d'une colonne calculée.

*   **Usage** : On utilise `AS` dans la clause `SELECT`.
*   **Exemple** : Si on joint deux versions de la table `Abonne` (auto-jointure), on écrit : `SELECT A1.nom AS nom1, A2.nom AS nom2`. Cela permet d'avoir des en-têtes clairs dans le tableau de résultats.

### En résumé

*   **Qualification** : Indispensable techniquement pour que le SGBD sache de quelle colonne on parle.
*   **Alias de table** : Pratique pour raccourcir l'écriture des préfixes.
*   **Alias de colonne** : Utile pour la clarté de l'affichage des résultats.

---

## 11. Complément : Les contraintes d'intégrité

Une **contrainte d'intégrité** est une règle que l'on définit sur les colonnes ou les lignes d'une table pour garantir la cohérence, la validité et la qualité des données stockées dans une base de données. Si une opération (insertion ou mise à jour) ne respecte pas ces règles, le SGBD la refuse.

Voici quelques contraintes d'intégrité.

### 11.1. La contrainte de vérification (`CHECK`)
Il s'agit d'une **condition booléenne** que les valeurs d'une colonne doivent impérativement respecter.

*   **Exemple** : Dans une table d'abonnés, on peut imposer que l'âge soit toujours un nombre positif et cohérent : `CHECK (0 < AGE)` ou `CHECK (AGE <= 130)`.

### 11.2. La contrainte de non-nullité (`NOT NULL`)
Cette contrainte force un attribut à être **obligatoirement renseigné** ; il ne peut pas être laissé vide (valeur `NULL`).

*   **Exemple** : Dans une table `LIVRE`, on peut décider que le titre doit toujours être présent : `TITRE VARCHAR NOT NULL`.

### 11.3. La contrainte d'unicité (`UNIQUE`)
Elle garantit que deux lignes différentes d'une table ne peuvent pas avoir la même valeur pour un attribut donné.

*   **Exemple** : On peut imposer que chaque livre ait un titre unique dans la base de données : `TITRE VARCHAR UNIQUE`.

### 11.4. La clé primaire (`PRIMARY KEY`)
C'est la contrainte la plus importante. Elle identifie chaque enregistrement de manière **unique** et ne peut jamais être nulle.

*   **Exemple** : L'attribut `IDL` (identifiant du livre) dans la table `LIVRE`.

### 11.5. La clé étrangère (`FOREIGN KEY`)
Elle sert à maintenir la **cohérence entre deux tables** en s'assurant qu'une valeur fait bien référence à une clé primaire existante dans une autre table.

*   **Exemple** : Dans la table `EMPRUNT`, l'identifiant du livre (`IDL`) est une clé étrangère qui doit obligatoirement correspondre à un identifiant présent dans la table `LIVRE`.

En résumé, ces contraintes permettent d'éviter les **erreurs de saisie** (comme un âge négatif) ou les **incohérences logiques** (comme supprimer un livre alors qu'il est encore noté comme emprunté).

---

## 12. Complément : Clé primaire sur plusieurs colonnes

Pour définir une **clé primaire sur plusieurs colonnes** (également appelée clé primaire composée), on ne peut pas utiliser le mot-clé `PRIMARY KEY` directement à côté de la définition d'un attribut. On doit utiliser une instruction spécifique à la fin de la création de la table,.

### 12.1. Syntaxe SQL
Dans l'instruction `CREATE TABLE`, après avoir listé tous les attributs (colonnes), on ajoute une virgule suivie de la clause `PRIMARY KEY` contenant la liste des colonnes entre parenthèses,.

**Modèle général :**
```sql
CREATE TABLE NomDeLaTable (
    attribut1 TYPE,
    attribut2 TYPE,
    attribut3 TYPE,
    PRIMARY KEY (attribut1, attribut2)
);
```

### 12.2. Exemple concret
Si l'on veut créer une table `T` où la clé primaire est l'association des colonnes `A` et `C`, la syntaxe est la suivante :
```sql
CREATE TABLE T (
    A TYPE,
    B TYPE,
    C TYPE,
    PRIMARY KEY(A, C)
);
```

### 12.3. Règles d'intégrité
Lorsqu'une clé primaire est définie sur plusieurs colonnes :

*   **Unicité du couple** : C'est la combinaison des valeurs des colonnes citées qui doit être unique pour chaque ligne de la table. Par exemple, vous pouvez avoir deux lignes avec la même valeur pour `A`, tant que leurs valeurs pour `C` sont différentes.
*   **Non-nullité** : Comme pour toute clé primaire, aucun des attributs composant cette clé ne peut contenir la valeur `NULL`.
*   **Identification** : Ce groupe d'attributs (n-uplet de valeurs) permet d'identifier de manière unique chaque enregistrement de la table.

### 13. Complément : Injection SQL

Une **injection SQL** est une faille de sécurité qui se produit lorsqu'une application interagit avec une base de données de manière mal sécurisée, permettant à un utilisateur malveillant d'injecter du code SQL dans une requête. Cela peut compromettre la **confidentialité** ou l'**intégrité** des données.

#### Exemple d'injection SQL

Prenons l'exemple d'un formulaire de connexion où le programme Python construit la requête par **concaténation de chaînes** (méthode à proscrire) :
`requete = "SELECT * FROM Client WHERE nom = '" + username + "' AND passwd = '" + password + "';"`

1.  **Détournement par commentaire** : Si un utilisateur saisit l'identifiant `Gargamel ' #` et laisse le champ mot de passe vide, la requête générée devient :
    `SELECT * FROM Client WHERE nom = 'Gargamel' # ' AND passwd = '';`.
    Le caractère `#` (ou `--` selon le SGBD) indique que tout ce qui suit est un **commentaire**. Le SGBD exécute donc uniquement `SELECT * FROM Client WHERE nom = 'Gargamel'`, ce qui permet de se connecter au compte de "Gargamel" sans connaître son mot de passe !

2.  **Injection d'une condition toujours vraie (Tautologie)** : Si l'utilisateur saisit `' OR 1 #` dans une zone de texte, la requête devient :
    `SELECT * FROM Client WHERE nom = '' OR 1 # ...`.
    Comme la condition `OR 1` est **toujours vraie**, le SGBD renvoie les données de la table, permettant de récupérer des informations de manière illégitime.

#### Comment s'en protéger ?

La règle d'or est de **ne jamais concaténer naïvement les paramètres** saisis par l'utilisateur directement dans le texte de la requête SQL.

*   **Utiliser des requêtes paramétrées** : Il faut relier l'ordre SQL à des variables en utilisant un **symbole substitut `?`** à chaque endroit où une valeur est nécessaire. 
*   **Exécution sécurisée avec Python** : Au lieu de fusionner les chaînes soi-même, on passe la requête avec les `?` et une liste de valeurs séparée à la méthode `execute()`.

**Exemple de code sécurisé :**
```python
# Méthode sûre utilisant le paramétrage
gestionnaire.execute("SELECT * FROM Client WHERE nom = ? AND passwd = ?", (username, password))
```
Dans ce cas, le gestionnaire de base de données traite les entrées comme de simples valeurs et non comme du code exécutable, neutralisant ainsi toute tentative d'injection. De plus, il est conseillé de préférer la méthode `execute` à `executescript` (qui permet d'enchaîner plusieurs ordres séparés par des points-virgules) pour limiter les risques de manipulations complexes par un tiers.