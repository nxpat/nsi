## Introduction au Terminal et aux Commandes Unix/Linux

Le terminal est un outil puissant qui permet aux utilisateurs d'interagir avec leurs systèmes informatiques en utilisant des commandes basées sur du texte. Contrairement aux interfaces graphiques (GUI), qui utilisent des fenêtres et des icônes, le terminal repose uniquement sur des commandes saisies. Cela peut sembler intimidant au départ, mais cela offre un grand contrôle et flexibilité pour effectuer des tâches efficacement.

Unix/Linux est une famille de systèmes d'exploitation largement utilisés dans les serveurs, les mainframes et les systèmes embarqués. Apprendre les commandes les plus courantes peut aider à gérer des fichiers, naviguer dans les répertoires et résoudre des problèmes efficacement.

Voici un aperçu des commandes Unix/Linux essentielles :

| **Commande** | **Description** |
|--------------|------------------|
| **cd**       | Changer le répertoire courant. Par exemple, `cd Documents` vous déplace dans le dossier Documents. |
| **pwd**      | Affiche le répertoire de travail actuel, montrant où vous êtes dans le système de fichiers. |
| **ls**       | Lister le contenu d'un répertoire. Utiliser `ls -l` fournit des informations détaillées. |
| **history**  | Afficher les commandes précédemment saisies, facilitant leur réutilisation. |
| **chmod**    | Modifier les permissions d'un fichier ou d'un répertoire. Par exemple, `chmod 755 fichier.txt` définit des permissions spécifiques. |
| **chown**    | Changer le propriétaire d'un fichier ou d'un répertoire. Utile pour gérer l'accès des utilisateurs. |
| **grep**     | Rechercher un texte spécifique dans des fichiers. Par exemple, `grep 'mot-clé' fichier` trouve 'mot-clé' dans le fichier. |
| **find**     | Rechercher des fichiers et des répertoires à un chemin spécifié. Par exemple, `find . -name '*.txt'` trouve tous les fichiers texte. |
| **cp**       | Copier des fichiers ou des répertoires. Par exemple, `cp source.txt destination.txt` crée une copie. |
| **mkdir**    | Créer un nouveau répertoire. Par exemple, `mkdir nouveau_dossier` crée un dossier nommé nouveau_dossier. |
| **mv**       | Déplacer des fichiers ou des répertoires, également utilisé pour renommer. Par exemple, `mv ancien_nom.txt nouveau_nom.txt` renomme un fichier. |
| **cat**      | Afficher le contenu d'un fichier. Par exemple, `cat fichier.txt` montre le contenu du fichier à l'écran. |
| **touch**    | Créer un nouveau fichier vide ou mettre à jour l'horodatage d'un fichier existant. |
| **wc**       | Compter les lignes, les mots et les caractères dans un fichier. Par exemple, `wc fichier.txt` affiche ces comptages. |
| **sort**     | Trier les lignes de texte d'un fichier. Par exemple, `sort fichier.txt` trie le contenu par ordre alphabétique. |
| **uniq**     | Filtrer les lignes répétées dans un fichier. Souvent utilisé avec `sort`. |
| **more**     | Voir le contenu d'un fichier page par page, utile pour les fichiers volumineux. |
| **less**     | Semblable à more, mais permet la navigation en arrière dans le fichier. |
| **tail**     | Voir les dernières lignes d'un fichier. Par exemple, `tail -n 10 fichier.txt` montre les dix dernières lignes. |
| **diff**     | Comparer deux fichiers ligne par ligne et montrer les différences. Par exemple, `diff fichier1.txt fichier2.txt`. |
| **top**      | Afficher les processus en cours en temps réel, utile pour surveiller les performances du système. |
| **ps**       | Afficher des informations sur les processus actifs. |
| **kill**     | Terminer un processus par son ID. Par exemple, `kill 1234` arrête le processus avec l'ID 1234. |
| **man**      | Accéder aux pages de manuel pour les commandes, fournissant une documentation détaillée. Par exemple, `man ls` montre le manuel de la commande `ls`. |

La pratique de ces commandes dans un terminal favorise la compréhension des systèmes informatiques et améliore les compétences en résolution de problèmes dans des scénarios réels.

## Vue Détailée des Commandes Unix/Linux

Voici des descriptions étendues de chaque commande Unix/Linux, y compris les options courantes et des exemples typiques.

### 1. **cd**
**Description :** Changer le répertoire de travail courant.

**Options Communes :**
- `cd ..` – Monter d'un répertoire.
- `cd ~` – Se déplacer vers le répertoire personnel.
- `cd -` – Revenir au répertoire précédent.

**Exemples :**
- `cd Documents` – Change pour le répertoire Documents.
- `cd /usr/local/bin` – Navigue directement vers le chemin spécifié.

---

### 2. **pwd**
**Description :** Afficher le répertoire de travail actuel.

**Options Communes :**
- Aucune option n'est généralement utilisée.

**Exemples :**
- En tapant simplement `pwd`, cela affiche le chemin complet du répertoire courant, e.g., `/home/user/Documents`.

---

### 3. **ls**
**Description :** Lister le contenu d'un répertoire.

**Options Communes :**
- `-l` – Format de listing long (informations détaillées).
- `-a` – Lister tous les fichiers, y compris les fichiers cachés (commençant par un point).
- `-h` – Tailles lisibles par l'homme (lorsqu'il est utilisé avec `-l`).

**Exemples :**
- `ls` – Liste les fichiers dans le répertoire courant.
- `ls -la` – Montre tous les fichiers en format long, y compris les fichiers cachés.

---

### 4. **history**
**Description :** Afficher l'historique des commandes.

**Options Communes :**
- `!n` – Réexécuter la commande du numéro n dans l'historique.
- `-c` – Effacer l'historique.

**Exemples :**
- `history` – Affiche la liste des commandes précédemment saisies.
- `!5` – Exécute la cinquième commande de la liste d'historique.

---

### 5. **chmod**
**Description :** Modifier les permissions d'un fichier ou d'un répertoire.

**Options Communes :**
- Paramètres numériques (`755`, `644`) pour définir des permissions spécifiques.
  - `u+x` – Ajoute des permissions d'exécution pour le propriétaire.
  - `g-w` – Enlève les permissions d'écriture pour le groupe.
- `-R` – Appliquer les changements de manière récursive aux répertoires.

**Exemples :**
- `chmod 755 script.sh` – Définit les permissions pour le propriétaire à lire, écrire et exécuter, et pour les autres à lire et exécuter.
- `chmod u+x fichier.sh` – Ajoute les permissions d'exécution pour le propriétaire.
- `chmod -R 700 dossier` – Donne toutes les permissions au propriétaire pour tous les fichiers d'un dossier.

---

### 6. **chown**
**Description :** Changer le propriétaire d'un fichier ou d'un répertoire.

**Options Communes :**
- `--recursive` ou `-R` – Changer le propriétaire de manière récursive.

**Exemples :**
- `chown utilisateur1:fichier1.txt` – Change le propriétaire du fichier à utilisateur1 et le groupe à fichier1.txt.
- `chown -R nom_utilisateur:groupe /chemin/vers/dossier` – Change le propriétaire de manière récursive pour tous les fichiers.

---

### 7. **grep**
**Description :** Rechercher un motif spécifique dans des fichiers.

**Options Communes :**
- `-i` – Ignorer la distinction entre majuscules et minuscules.
- `-r` – Rechercher de manière récursive à travers les répertoires.
- `-v` – Inverser la correspondance (montrer les lignes qui ne correspondent pas).

**Exemples :**
- `grep 'erreur' log.txt` – Recherche le mot "erreur" dans log.txt.
- `grep -r 'TODO' /chemin/vers/projet/` – Recherche récursivement "TODO" dans tous les fichiers d'un répertoire.

---

### 8. **find**
**Description :** Rechercher des fichiers et des répertoires dans une hiérarchie de répertoires.

**Options Communes :**
- `-name` – Rechercher par nom de fichier.
- `-type` – Spécifier le type (e.g., `f` pour fichier, `d` pour répertoire).
- `-exec` – Exécuter une commande sur les fichiers trouvés.

**Exemples :**
- `find . -name '*.txt'` – Trouve tous les fichiers texte dans le répertoire courant et les sous-répertoires.
- `find /chemin -type d -exec ls -l {} \;` – Liste les détails de tous les répertoires dans un chemin spécifié.

---

### 9. **cp**
**Description :** Copier des fichiers et des répertoires.

**Options Communes :**
- `-r` – Copier les répertoires de manière récursive.
- `-i` – Demander une confirmation avant d'écraser les fichiers existants.
- `-u` – Copier uniquement lorsque la source est plus récente que la destination ou lorsque le fichier de destination est manquant.

**Exemples :**
- `cp fichier.txt /chemin/vers/destination/` – Copie fichier.txt vers le chemin spécifié.
- `cp -r dossier/ /chemin/vers/destination/` – Copie récursivement un dossier entier.

---

### 10. **mkdir**
**Description :** Créer un nouveau répertoire.

**Options Communes :**
- `-p` – Créer les répertoires parents si nécessaire.

**Exemples :**
- `mkdir nouveau_dossier` – Crée un nouveau répertoire appelé nouveau_dossier.
- `mkdir -p parent/enfant` – Crée les répertoires parent et enfant si ils n'existent pas.

---

### 11. **mv**
**Description :** Déplacer ou renommer des fichiers et des répertoires.

**Options Communes :**
- `-i` – Demander une confirmation avant d'écraser les fichiers existants.

**Exemples :**
- `mv ancien_nom.txt nouveau_nom.txt` – Renomme le fichier ancien_nom.txt en nouveau_nom.txt.
- `mv fichier.txt /chemin/vers/destination/` – Déplace fichier.txt vers le chemin spécifié.

---

### 12. **cat**
**Description :** Afficher le contenu d'un fichier.

**Options Communes :**
- `-n` – Numéroter les lignes dans la sortie.
- `-b` – Numéroter les lignes non vides.

**Exemples :**
- `cat fichier.txt` – Affiche le contenu de fichier.txt à l'écran.
- `cat -n fichier.txt` – Affiche le contenu avec les lignes numérotées.

---

### 13. **touch**
**Description :** Créer un nouveau fichier vide ou mettre à jour l'horodatage d'un fichier existant.

**Options Communes :**
- Aucun.

**Exemples :**
- `touch nouveau_fichier.txt` – Crée un nouveau fichier vide nommé nouveau_fichier.txt.
- `touch fichier_exist.txt` – Met à jour l'horodatage de fichier_exist.txt.

---

### 14. **wc**
**Description :** Compter les lignes, les mots et les caractères dans un fichier.

**Options Communes :**
- `-l` – Compter seulement les lignes.
- `-w` – Compter seulement les mots.
- `-c` – Compter seulement les caractères.

**Exemples :**
- `wc fichier.txt` – Affiche le nombre de lignes, de mots et de caractères dans fichier.txt.
- `wc -l fichier.txt` – Affiche seulement le nombre de lignes dans fichier.txt.

---

### 15. **sort**
**Description :** Trier les lignes de texte d'un fichier.

**Options Communes :**
- `-r` – Trier en ordre inverse.
- `-n` – Trier numériquement.

**Exemples :**
- `sort fichier.txt` – Trie le contenu de fichier.txt par ordre alphabétique.
- `sort -n nombres.txt` – Trie les lignes numériquement dans nombres.txt.

---

### 16. **uniq**
**Description :** Filtrer les lignes répétées dans un fichier.

**Options Communes :**
- `-c` – Compter le nombre d'occurrences de chaque ligne.
- `-d` – Afficher uniquement les lignes dupliquées.

**Exemples :**
- `uniq fichier.txt` – Affiche les lignes uniques dans fichier.txt.
- `sort fichier.txt | uniq -c` – Trie et compte les occurrences de chaque ligne dans fichier.txt.

---

### 17. **more**
**Description :** Afficher le contenu d'un fichier une page à la fois.

**Options Communes :**
- Aucun.

**Exemples :**
- `more fichier.txt` – Montre le contenu de fichier.txt, page par page.

---

### 18. **less**
**Description :** Similaire à `more`, mais permet la navigation vers l’arrière dans le fichier.

**Options Communes :**
- `-N` – Affiche les numéros de ligne.
- `-S` – Raccourcit les lignes trop longues.

**Exemples :**
- `less fichier.txt` – Ouvre fichier.txt, permettant de naviguer à travers le fichier avec les touches fléchées.
- `less -N fichier.txt` – Ouvre le fichier avec les numéros de ligne affichés.

---

### 19. **tail**
**Description :** Afficher les dernières lignes d'un fichier.

**Options Communes :**
- `-n N` – Affiche les N dernières lignes (pr default, cela affiche 10 lignes).
- `-f` – Suit les ajouts en temps réel à un fichier.

**Exemples :**
- `tail fichier.txt` – Affiche les 10 dernières lignes de fichier.txt.
- `tail -n 20 fichier.txt` – Affiche les 20 dernières lignes de fichier.txt.
- `tail -f fichier.log` – Suivre les nouvelles entrées dans fichier.log en temps réel.

---

### 20. **diff**
**Description :** Comparer deux fichiers ligne par ligne et montrer leurs différences.

**Options Communes :**
- `-u` – Affiche les différences en format "unifié".
- `-i` – Ignore la casse pendant la comparaison.

**Exemples :**
- `diff fichier1.txt fichier2.txt` – Compare fichier1.txt et fichier2.txt et affiche les différences.
- `diff -u fichier1.txt fichier2.txt` – Affiche les différences au format unifié.

---

### 21. **top**
**Description :** Affiche les processus en cours en temps réel.

**Options Communes :**
- `-u utilisateur` – Filtrer par un utilisateur spécifique.
- `-n nombre` – Exécute un certain nombre de mises à jour avant de quitter.

**Exemples :**
- `top` – Ouvre l'interface des processus en temps réel.
- `top -u mon_utilisateur` – Affiche uniquement les processus associés à mon_utilisateur.

---

### 22. **ps**
**Description :** Affiche des informations sur les processus actifs.

**Options Communes :**
- `aux` – Affiche tous les processus sur le système.
- `-ef` – Affiche les processus en format étendu.

**Exemples :**
- `ps aux` – Montre tous les processus en cours avec des détails complets.
- `ps -ef | grep nom_du_processus` – Filtre l'affichage pour montrer uniquement les processus contenant nom_du_processus.

---

### 23. **kill**
**Description :** Terminer un processus par son ID.

**Options Communes :**
- `-9` – Envoie un signal SIGKILL pour forcer l'arrêt du processus.
- `-l` – Liste les signaux disponibles.

**Exemples :**
- `kill 1234` – Tente de terminer le processus avec l'ID 1234.
- `kill -9 1234` – Force l'arrêt du processus avec l'ID 1234 immédiatement.

---

### 24. **man**
**Description :** Accéder aux pages de manuel pour les commandes.

**Options Communes :**
- Aucun.

**Exemples :**
- `man ls` – Affiche le manuel de la commande `ls`.
- `man grep` – Affiche le manuel de la commande `grep`, fournissant des détails et des options.

---
