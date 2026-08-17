# L'exponentiation rapide

L'**exponentiation rapide** est un algorithme récursif particulièrement efficace pour calculer de grandes puissances entières d'un nombre. Contrairement à la méthode naïve qui multiplie $x$ par lui-même $n$ fois (complexité linéaire), cette méthode réduit drastiquement le nombre de multiplications nécessaires en divisant l'exposant par deux à chaque étape (complexité logarithmique).

## Principe mathématique
L'algorithme repose sur les identités suivantes :

1.  **Cas de base :** $x^0 = 1$
2.  **Si $n$ est pair :** $x^n = (x^{n/2})^2$
3.  **Si $n$ est impair :** $x^n = x \times (x^{(n-1)/2})^2$

### Implémentation en Python
Voici une version possible de la fonction, utilisant une fonction auxiliaire `carre` pour optimiser le calcul et éviter de répéter l'appel récursif inutilement :

```python
def carre(x):
    return x * x

def puissance_rapide(x, n):
    if n == 0:
        return 1 # Condition d'arrêt
    else:
        if n % 2 == 0:
            # Si n est pair, on calcule (x^(n/2))^2
            return carre(puissance_rapide(x, n // 2))
        else:
            # Si n est impair, on calcule x * (x^((n-1)/2))^2
            return x * carre(puissance_rapide(x, (n - 1) // 2))
```

## Exemple détaillé : Calcul de $3^5$
En suivant l'algorithme pour $x=3$ et $n=5$ :

1.  **Appel initial :** `puissance_rapide(3, 5)`
    *   $5$ est **impair**.
    *   Formule : $3 \times (3^{(5-1)/2})^2 = 3 \times (3^2)^2$.
    *   On appelle `puissance_rapide(3, 2)`.

2.  **Deuxième appel :** `puissance_rapide(3, 2)`
    *   $2$ est **pair**.
    *   Formule : $(3^{2/2})^2 = (3^1)^2$.
    *   On appelle `puissance_rapide(3, 1)`.

3.  **Troisième appel :** `puissance_rapide(3, 1)`
    *   $1$ est **impair**.
    *   Formule : $3 \times (3^0)^2$.
    *   On appelle `puissance_rapide(3, 0)`.

4.  **Quatrième appel (Cas de base) :** `puissance_rapide(3, 0)`
    *   $n=0$, la fonction renvoie **1**.

**Remontée des résultats (dépilage) :**
*   Le 3ème appel renvoie $3 \times 1^2 = \mathbf{3}$.
*   Le 2ème appel renvoie $3^2 = \mathbf{9}$.
*   L'appel initial renvoie $3 \times 9^2 = 3 \times 81 = \mathbf{243}$.

On obtient bien $3^5 = 243$. Cet exemple montre que nous n'avons eu besoin que de quelques étapes pour arriver au résultat, là où une boucle simple aurait nécessité 5 itérations de multiplication.

## Complexité

La complexité de l'algorithme d'**exponentiation rapide** est **logarithmique**, ce qui se note généralement **$O(\log_2 n)$** :

*   **Réduction de la taille du problème :** Contrairement à la méthode naïve qui effectue $n$ multiplications (complexité linéaire en $O(n)$), cet algorithme divise l'exposant par deux à chaque appel récursif.
*   **Nombre d'appels :** La relation de récurrence pour le nombre d'opérations (ou d'appels) est de la forme $C(n) = C(n//2) + 1$. Les sources associent explicitement ce type d'équation à une complexité en **$\log(n)$**.
*   **Efficacité :** Ce passage d'un coût linéaire ($n$) à un coût logarithmique ($\log_2 n$) est ce qui rend l'algorithme particulièrement efficace pour calculer de très grandes puissances entières.

En résumé, si vous voulez calculer $x^{1024}$, la méthode naïve demande 1024 multiplications, tandis que l'exponentiation rapide n'en demande qu'environ 10 (puisque $2^{10} = 1024$).