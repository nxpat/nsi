# Les Tours de Hanoï

Le problème des **Tours de Hanoï** est un casse-tête classique utilisé en informatique pour illustrer la puissance de la **récursivité**.

## 1. Principe et règles du jeu
Le jeu se compose de trois piquets (souvent notés $X, Y, Z$) et de $n$ disques de diamètres différents, initialement empilés par taille décroissante sur le premier piquet. L'objectif est de déplacer toute la pile vers un autre piquet en respectant trois règles strictes :

*   On ne peut déplacer qu'**un seul disque à la fois**.
*   On ne peut déplacer que le disque situé au **sommet** d'une pile.
*   On ne peut jamais poser un disque sur un **disque plus petit** que lui.

## 2. La légende de la Tour de Brahma
Le problème est souvent associé à une légende indienne : dans le temple de Bénarès, des moines déplacent 64 disques d'or pur. Selon la prophétie, lorsque les moines auront terminé le transfert des 64 disques vers la destination finale en respectant les règles, le temple s'écroulera et ce sera la fin du monde.

## 3. Stratégie récursive (Diviser pour régner)
La résolution repose sur une logique de décomposition du problème. Pour transférer $n$ disques du piquet **début** vers le piquet **fin** en utilisant un piquet de **transit** :

1.  **Déplacer** récursivement les $n-1$ disques supérieurs du piquet *début* vers le piquet *transit*.
2.  **Déplacer** le $n$-ième disque (le plus grand) directement du piquet *début* vers le piquet *fin*.
3.  **Déplacer** récursivement les $n-1$ disques du piquet *transit* vers le piquet *fin*.

**Le cas de base** survient lorsque $n=0$ (ou $n=1$) : il n'y a plus rien à déplacer, ou le déplacement est direct.

## 4. Implémentation en Python
Voici un algorithme utilisant des listes pour modéliser les piquets :

```python
def hanoi(n, debut, fin, transit):
    """Déplace n disques de debut à fin en passant par transit"""
    if n > 0:
        # Étape 1 : on déplace n-1 disques vers le piquet de transit
        hanoi(n - 1, debut, transit, fin)
        
        # Étape 2 : on déplace le disque restant vers la fin
        fin.append(debut.pop())
        
        # Étape 3 : on déplace les n-1 disques du transit vers la fin
        hanoi(n - 1, transit, fin, debut)
```

## 5. Complexité
Ce problème a une **complexité exponentielle**. Le nombre de mouvements nécessaires pour $n$ disques est de **$2^n - 1$** :

*   Pour 3 disques, il faut **7** mouvements.
*   Pour 64 disques (la légende), le nombre de mouvements est astronomique ($2^{64}-1$), ce qui explique pourquoi le monde n'est pas près de s'arrêter.