# Arbre binaire de recherche (ABR) dégénéré

Un **arbre binaire de recherche (ABR) dégénéré**, également qualifié d'arbre **« filiforme »**, est un arbre dans lequel chaque nœud interne possède exactement un seul fils.

Voici ses principales caractéristiques et conséquences :

*   **Structure linéaire :** Contrairement à un arbre équilibré qui s'étale en largeur, l'arbre dégénéré s'étire tout en longueur, ressemblant visuellement à une **liste chaînée**.
*   **Hauteur maximale :** Pour un nombre de nœuds \\(n\\) donné, sa hauteur \\(h\\) atteint sa valeur maximale, soit **\\(h = n - 1\\)** (si l'on considère que la racine est à la profondeur 0).
*   **Efficacité algorithmique médiocre :** C'est la configuration la moins performante pour un ABR. Alors qu'un arbre équilibré permet des recherches en temps logarithmique \\(O(\log n)\\), un arbre dégénéré impose un temps de recherche proportionnel au nombre de nœuds, soit une **complexité linéaire en \\(O(n)\\)**.
*   **Origine :** Cette structure survient généralement lorsque les données sont insérées dans l'arbre déjà triées (par exemple, si on insère successivement 1, 2, 3, 4, 5, chaque nouveau nœud devient systématiquement le fils droit du précédent).

En résumé, l'arbre dégénéré fait perdre tout l'intérêt de la structure d'arbre de recherche, car il se comporte comme une simple structure linéaire tout en étant plus complexe à manipuler.