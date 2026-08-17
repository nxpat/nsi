# Algorithme A*

L'algorithme **A\*** est un algorithme de recherche de chemin qui combine intelligemment les forces de l'algorithme de **Dijkstra** et du parcours **Best-First Search** (parcours au plus proche).

Voici ses caractéristiques principales :

## 1. Le meilleur des deux mondes

*   **Garantie d'optimalité :** Comme l'algorithme de Dijkstra, A* garantit mathématiquement de trouver le chemin le plus court entre un départ et une arrivée, une capacité que n'a pas le Best-First Search.
*   **Efficacité et guidage :** Comme le Best-First Search, il effectue une recherche **« informée »**. Il utilise une règle simplifiée (**heuristique**) pour orienter sa recherche vers la cible plutôt que d'explorer toutes les directions possibles.

## 2. Le rôle de l'heuristique
La grande innovation de A* réside dans sa manière d'évaluer les sommets dans sa file de priorité :

*   Il calcule une estimation du **coût total** du chemin passant par un sommet donné.
*   Ce calcul additionne la distance déjà parcourue depuis le départ (`poids_est`) et une estimation de la distance restant à parcourir jusqu'à la cible (généralement la **distance euclidienne** à vol d'oiseau).
*   Ce mécanisme permet de « guider » l'algorithme vers la destination, lui évitant d'explorer inutilement des zones du graphe qui s'éloignent de l'objectif.

## 3. Différences avec Dijkstra
Bien qu'ils partagent une structure proche, A* présente des différences fondamentales :

*   **Objectif ciblé :** Alors que Dijkstra calcule les distances vers **tous** les sommets du graphe, A* ne s'intéresse qu'au plus court chemin vers **un seul sommet cible** spécifique.
*   **Terminaison rapide :** A* quitte la boucle de recherche dès qu'il extrait le sommet cible de sa file de priorité, ce qui réduit considérablement le temps de calcul par rapport à un parcours exhaustif.
*   **Moins d'exploration :** Visuellement, A* explore beaucoup **moins d'arêtes** que Dijkstra pour arriver au même résultat optimal.

## 4. Complexité
L'algorithme A* possède une complexité identique à celle de Dijkstra, de l'ordre de **$(p + n) \log(n)$**, où $n$ est le nombre de sommets et $p$ le nombre d'arêtes.

## 5. Applications
L'algorithme A* est extrêmement utilisé dans de nombreux domaines comme la **recherche d'itinéraires sur une carte** ou les systèmes de navigation de jeux vidéo.

## 6. Implémentation en Python
L'implémentation de l'algorithme **A\*** en Python repose sur une structure proche de celle de Dijkstra, mais elle intègre une **heuristique** pour guider la recherche vers une cible unique.

L'algorithme nécessite le module `heapdict` pour gérer la **file de priorité**, car il permet de modifier efficacement la valeur d'un élément déjà présent dans la file. Il utilise également les coordonnées cartésiennes des sommets (`XY`) pour calculer la distance euclidienne servant d'heuristique.

L'algorithme prend en entrée une liste d'adjacence (`adj`) et les coordonnées des sommets (`XY`).

```python
import heapdict
from math import inf, sqrt

def d(p1, p2):
    """Calcule la distance euclidienne entre deux points."""
    return sqrt((p1 - p2)**2 + (p1 - p2)**2)

def Astar(adj, XY):
    n = len(adj)
    poids = calcule_poids(adj, XY) # Matrice des poids réels
    provenance =  * n
    poids_est = [inf] * n # g(n) : coût réel depuis le départ
    poids_est = 0
    
    poids_fp = heapdict.heapdict() # File de priorité
    # f(n) = g(n) + h(n). Au départ, g(0)=0 donc f(0) = h(0)
    poids_fp = d(XY, XY[n - 1]) 
    
    while len(poids_fp) > 0:
        k = poids_fp.popitem()
        
        # Condition d'arrêt : on a atteint la cible
        if k == n - 1:
            break
            
        for j in adj[k]:
            d1 = poids_est[k] + poids[k][j] # Nouveau coût réel g(j)
            d2 = d1 + d(XY[j], XY[n - 1])   # f(j) = g(j) + h(j)
            
            if d1 < poids_est[j]:
                provenance[j] = k
                poids_est[j] = d1
                poids_fp[j] = d2 # On stocke f(j) dans la file de priorité
                
    return provenance
```

## Explication des points clés
*   **La file de priorité (`poids_fp`) :** Contrairement à Dijkstra qui y stocke uniquement la distance depuis le départ, A* y stocke une **estimation du coût total** du chemin passant par le sommet (coût réel déjà parcouru + distance "à vol d'oiseau" vers la cible).
*   **L'arrêt anticipé :** L'algorithme quitte la boucle dès que le sommet cible est extrait de la file de priorité, ce qui le rend beaucoup plus rapide qu'un parcours exhaustif.
*   **L'heuristique :** Elle est visible aux lignes 17 et 18 du code source : `d2 = d1 + d(XY[j], XY[n - 1])`. On ajoute la distance euclidienne (`h`) au coût réel (`g`) pour "guider" la recherche.
*   **Efficacité :** Visuellement, A* explore **beaucoup moins d'arêtes** que Dijkstra pour arriver au même résultat optimal. Sa complexité reste cependant identique à celle de Dijkstra.

Pour reconstituer le chemin final, on utilise le tableau `provenance` en remontant de "père en père" depuis le sommet d'arrivée jusqu'à l'origine.

## 7. Historique de l'algorithme A*

L'histoire de l'algorithme **A\*** s'inscrit dans l'évolution plus large de la théorie des graphes et de la recherche de chemins optimaux, bien que ses créateurs spécifiques ne soient pas nommés dans les sources.

L'histoire des algorithmes de parcours de graphes, dont A* fait partie, trouve sa source originelle en **1735** avec le mathématicien suisse **Leonhard Euler**. En tentant de résoudre le **problème des sept ponts de Königsberg**, Euler a posé les bases de ce qui deviendra la théorie des graphes. Par la suite, d'autres mathématiciens comme **Arthur Cayley** (au milieu du XIXe siècle) ont approfondi ces concepts, notamment en étudiant la structure des **arbres**.

L'algorithme A* est né d'une volonté de combiner deux approches existantes pour la recherche du plus court chemin :

*   **L'influence de Dijkstra :** A* s'appuie sur la rigueur de l'algorithme de Dijkstra pour **garantir l'optimalité** du chemin trouvé (le chemin le plus court possible).
*   **L'influence du Best-First Search :** Il s'inspire du parcours au plus proche (*Best-First*) pour réaliser une **recherche informée**. Cela lui permet d'utiliser une **heuristique** (comme la distance à vol d'oiseau) pour "guider" la recherche et l'accélérer considérablement par rapport à une exploration exhaustive.

L'algorithme A* a été publié pour la première fois en **1968** par **Peter Hart**, **Nils Nilsson** et **Bertram Raphael**, des chercheurs travaillant au Stanford Research Institute (maintenant  SRI International). Ils travaillaient sur le projet **Shakey the robot**, le premier robot mobile capable de raisonner sur ses propres actions. Shakey avait besoin d'un moyen efficace pour naviguer dans son environnement, ce qui a conduit à la création de cette méthode hybride alliant l'efficacité heuristique à la garantie de trouver le chemin le plus court.

Aujourd'hui, il est devenu l'un des algorithmes les plus utilisés dans le monde, notamment pour la **recherche d'itinéraires sur une carte** (GPS) ou les systèmes de navigation dans les jeux vidéo.