# Heuristique

## Définition

Une **heuristique** est une règle simplifiée ou une méthode de calcul rapide utilisée par un algorithme pour effectuer des choix et orienter sa recherche vers un objectif. 

Dans le contexte des graphes, une **heuristique** est une méthode de calcul simplifiée utilisée pour guider un algorithme vers une solution plus rapidement qu'une recherche exhaustive. On parle alors d'**algorithmes informés**.

Voici les points clés à retenir sur l'utilisation des heuristiques :

*   **Rôle de guidage :** L'heuristique sert à "guider" la recherche vers le sommet cible plutôt que d'explorer toutes les directions possibles de manière exhaustive. Elle permet à l'algorithme d'évaluer quel chemin semble le plus prometteur à un instant donné.
*   **Exemple courant (Distance euclidienne) :** Dans les réseaux routiers ou les graphes euclidiens, l'heuristique la plus classique consiste à évaluer la distance restant à parcourir jusqu'à la cible **« à vol d'oiseau »**.
*   **Rapidité d'exécution :** L'utilisation d'une heuristique rend les algorithmes (comme le *Best-First Search*) très rapides car ils explorent beaucoup moins d'arêtes que des méthodes non informées.
*   **Le compromis optimalité / vitesse :** 
    *   Une heuristique simple utilisée seule (dans le *Best-First Search*) **ne garantit pas** de trouver le chemin le plus court ; l'algorithme peut se laisser "piéger" par la configuration du graphe.
    *   En revanche, combinée à la rigueur de l'algorithme de Dijkstra, l'heuristique permet à l'algorithme **A\*** de garantir l'optimalité tout en étant beaucoup plus efficace.

En résumé, l'heuristique est une estimation du coût restant qui permet de privilégier les sommets qui se rapprochent géographiquement de la destination.

## Quelques exemples d'heuristique

### 1. La distance euclidienne (« à vol d'oiseau »)
C'est l'exemple le plus classique pour les réseaux routiers ou les graphes euclidiens.

*   **Principe :** On calcule la distance en ligne droite entre un sommet actuel et le sommet cible en utilisant les coordonnées cartésiennes des points.
*   **Utilisation :** Elle sert de guide dans l'algorithme **Best-First Search** et l'algorithme **A*** pour évaluer quel sommet de la « frontière » semble le plus prometteur à explorer.

### 2. L'estimation du coût total dans l'algorithme A*
L'algorithme A* utilise une heuristique combinée pour évaluer chaque sommet :

*   **Formule :** $f(n) = g(n) + h(n)$.
*   **$g(n)$ :** Le poids réel déjà parcouru depuis le départ (`poids_est`).
*   **$h(n)$ :** L'heuristique, qui est une **estimation du poids restant** pour atteindre la cible, généralement basée sur la distance euclidienne.

### 3. Autres exemples d'approches heuristiques mentionnés
Bien que moins détaillés comme « heuristiques » au sens strict de l'algorithme A*, d'autres méthodes simplifiées de choix sont évoquées pour orienter la navigation :

*   **La méthode de la « main gauche » :** Utilisée pour sortir d'un labyrinthe, elle consiste à suivre systématiquement le mur à sa gauche. C'est une règle simple qui permet de naviguer sans explorer toutes les possibilités.
*   **Le nombre d'étapes (nombre d'arcs) :** Dans certains contextes, on peut utiliser le nombre minimal d'arêtes entre deux points comme une estimation simplifiée du trajet le plus court, bien que cela ne soit pas toujours optimal par rapport à la distance réelle.

**Point important :** Une heuristique simple utilisée seule (comme dans le parcours *Best-First*) ne garantit pas l'optimalité du chemin trouvé et peut se laisser « piéger » par la configuration du graphe. C'est son couplage avec la rigueur de Dijkstra dans l'algorithme **A*** qui permet d'obtenir un résultat à la fois **optimal et rapide**.

## Heuristique "admissibles"

Une **heuristique "admissible"** est une fonction d'estimation qui possède des caractéristiques précises permettant à l'algorithme de garantir l'optimalité (trouver le chemin le plus court).


### 1. La sous-estimation du coût réel (Propriété de base)
Pour qu'une heuristique soit admissible, elle ne doit **jamais surestimer** le coût réel pour atteindre la cible. 

*   **Exemple des sources :** La **distance euclidienne** (« à vol d'oiseau ») est l'heuristique classique utilisée pour les réseaux routiers. Elle est admissible car la distance en ligne droite est mathématiquement toujours inférieure ou égale à la distance réelle parcourue sur des routes (qui peuvent faire des détours).
*   **Conséquence :** Si l'heuristique sous-estime le coût, l'algorithme ne risque pas d'ignorer un chemin potentiellement plus court, ce qui permet à A\* de **garantir l'optimalité** contrairement au parcours *Best-First Search* simple.

### 2. L'estimation du coût restant vers la cible
L'heuristique doit fournir une valeur $h(n)$ qui représente une estimation du **poids de la fin du chemin** entre le sommet actuel et le sommet cible spécifique.

Dans l'algorithme A\*, cette estimation est additionnée au poids déjà parcouru depuis le départ ($g(n)$ ou `poids_est`) pour obtenir une estimation du coût total du chemin passant par ce sommet.

### 3. Une valeur nulle à la destination
Bien que non détaillé formellement, il découle de la logique de calcul de la distance euclidienne (utilisée en exemple) que l'heuristique doit être égale à **0** lorsque le sommet actuel est le sommet cible lui-même.

### 4. Son rôle dans l'efficacité (Algorithme « informé »)

*   **Guidage :** L'heuristique « guide » la recherche vers la cible en évaluant quels sommets de la frontière semblent les plus prometteurs.
*   **Réduction de l'exploration :** Une bonne heuristique admissible permet d'explorer **beaucoup moins d'arêtes** que l'algorithme de Dijkstra tout en arrivant au même résultat optimal.

En résumé, pour être considérée comme admissible, l'heuristique doit être une estimation **optimiste** (sous-estimant le coût réel) qui permet de diriger l'algorithme efficacement vers le but sans compromettre la découverte du chemin le plus court.