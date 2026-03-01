# Dossier Tests
Ce dossier contient la suite de tests unitaires pour l'application calculatrice.
## Raison d'être
Ce répertoire contient tous les tests automatisés de l'application calculatrice. Les tests permettent de :

- Vérifier que chaque opérateur mathématique fonctionne correctement
- Détecter les bogues et régressions dans le code
- S'assurer que l'application web répond correctement aux requêtes
- Valider la gestion des erreurs et des cas limites

## Fichiers de tests
### `test_operators.py`
Tests unitaires pour les fonctions de calcul de `operators.py`.
<br>
**Fonctions à tester: **
- `add(a, b)`: Addition
- `subtract(a, b)`: Soustraction
- `multiply(a, b)`: Multiplication
- `divide(a, b)`: Division

### `test_app.py`
Tests unitaires pour l'application serveur `Flask` de `app.py`.
<br>
**Fonctions à tester: **
- `calculate(expr)`: Fonction de calcul d'expression
- `index()`: Route principale GET et POST

## Exécution des tests
### Installation du module pytest
```bash
py -m pip install pytest
```
### Lancement des tests
```bash
py -m pytest
```
## Exécuter un fichier de tests spécifique

```bash
py -m pytest tests/test_operators.py
py -m pytest tests/test_app.py
```

## Dépendances
- pytest : Framework de tests principal
- Flask : Requis pour les tests d'intégration de l'application