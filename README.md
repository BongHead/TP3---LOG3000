# Calculatrice Web – TP3 LOG3000

- Groupe 21
- Membres: Song Ning Lan, Sheng He Ge

## Description

Une simple application web de calculatrice utilisant Flask, créée dans le cadre du cours LOG3000.
L'application peut calculer des expressions arithmétiques simples à l'aide d'un formulaire web. Elle inclut aussi une suite de tests.

## Objectifs

Ce travail pratique poursuit trois objectifs clés :

1. Créer et configurer un dépôt GitHub : Mise en place d'une collaboration en équipe avec Git.
2. Documenter la base de code : Ajouter des docstrings, commentaires et documentation au niveau des modules
3. Tester et corriger les bogues : Implémenter un pipeline de tests et un processus de correction documenté

## Fonctionnalités

### L’application permet :

- L’entrée d’une expression arithmétique simple
- Le traitement côté serveur via Flask
- L’affichage du résultat ou d’un message d’erreur

### Fonctionnalités supportées

- Addition
- Soustraction
- Multiplication
- Division

### Limitations

- Une seule opération par expression
- Format requis : <nombre><opérateur><nombre>
- Pas de gestion d’expressions complexes ou de parenthèses multiples

## Prérequis

- Python 3.10 ou version ultérieure
- `pip` pour installer les dépendances

Les dépendances sont listées dans `requirements.txt` :

```text
Flask
pytest
```

Installez-les avec :

```bash
pip install -r requirements.txt
```

---

## Exécution
1. Clonez le dépôt
    ```bash
    git clone https://github.com/BongHead/TP3---LOG3000.git
    cd TP3---LOG3000
    ```
2. Installez les dépendances
    ```bash
    pip install -r requirements.txt
    ```
    ou encore
    ```bash
    py -m pip install -r requirements.txt
    ```
3. Démarrez le serveur Flask
    ```bash
    py app.py
    ```
4. Ouvrez dans votre navigateur web préféré `http://127.0.0.1:5000/`

---

## Tests

Des tests unitaires simples se trouvent dans le répertoire `tests/`. Ils couvrent actuellement le module `operators` et la logique principale `calculate`.

Exécutez les tests avec pytest :

```bash
pip install pytest            # si ce n’est pas déjà installé
pytest
```

Ajoutez des tests supplémentaires en modifiant ou en développant les fichiers dans `tests/`.

---
## Structure du projet

```
app.py                # Application Flask et logique de calcul
operators.py          # Fonctions d’opérateurs arithmétiques
static/               # Ressources statiques (CSS)
templates/            # Modèles HTML pour l’interface web
tests/                # Squelettes de tests unitaires
README.md             # Cette documentation
requirements.txt      # Dépendances Python
```
---

## Flux de contribution
