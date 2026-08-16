# Comment insérer une clé dans un ABR ?

L’insertion d’une nouvelle clé dans un **Arbre Binaire de Recherche (ABR)** consiste à ajouter un nœud tout en préservant la propriété structurelle de l'arbre : pour chaque nœud, les clés du sous-arbre gauche sont inférieures ou égales à la sienne, et celles du sous-arbre droit lui sont supérieures ou égales.

### Principe de l'insertion aux feuilles
La méthode la plus simple et la plus courante est l'**insertion aux feuilles**. Elle suit une logique de recherche :

1.  **Parcours descendant :** On commence à la racine et on compare la clé à insérer avec la valeur du nœud courant.
2.  **Choix de la branche :** Si la nouvelle clé est plus petite, on se dirige vers le fils gauche ; si elle est plus grande, vers le fils droit.
3.  **Placement :** On répète l'opération jusqu'à atteindre un emplacement vide (`None` ou `null`).
4.  **Création du nœud :** On remplace cet emplacement vide par le nouveau nœud, qui devient alors une nouvelle feuille de l'arbre.

### Implémentation en Python
Selon les sources, l'implémentation repose généralement sur une structure récursive utilisant une classe `ABR` (pour l'arbre) et une classe `Noeud`.

```python
# Exemple d'implémentation récursive (basé sur les sources)
def inserer(self, valeur):
    if self.est_vide():
        # Cas où l'arbre est initialement vide
        self.racine = Noeud(valeur)
    else:
        # Appel de la méthode récursive sur le nœud racine
        self.racine.inserer(valeur)

# Dans la classe Noeud
def inserer(self, valeur):
    if valeur < self.valeur:
        if self.noeud_gauche is None:
            self.noeud_gauche = Noeud(valeur)
        else:
            self.noeud_gauche.inserer(valeur)
    elif valeur > self.valeur:
        if self.noeud_droit is None:
            self.noeud_droit = Noeud(valeur)
        else:
            self.noeud_droit.inserer(valeur)
```

### Points importants à retenir

*   **Doublons :** Selon les conventions, on peut soit refuser d'insérer une clé déjà présente pour simplifier, soit l'accepter (elle sera alors placée dans le sous-arbre correspondant au test $\le$ ou $\ge$).
*   **Complexité :** Le temps nécessaire pour insérer une clé est proportionnel à la profondeur du nouvel emplacement. Dans le pire des cas, la complexité est de **$O(h)$**, où $h$ est la hauteur de l'arbre.
*   **Équilibre :** Si l'arbre est équilibré, l'insertion se fait en $O(\log n)$. S'il est "dégénéré" (en forme de liste), elle peut monter jusqu'à $O(n)$.
*   **Structure :** L'ordre dans lequel les clés sont insérées détermine la forme finale de l'arbre ; un même ensemble de clés peut donc produire des ABR de structures très différentes.