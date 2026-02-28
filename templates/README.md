# Dossier templates

Ce dossier contient le fichier squelette pour le site web (html). Il affiche l'inteface de la calculatrice web.

## Raison d’être du module

Le dossier templates/ contient les fichiers HTML utilisés par le moteur de templates Flask (Jinja2) pour générer les pages web de l’application.

Dans ce projet, il fournit l’interface utilisateur de la calculatrice web et permet l’interaction entre le frontend et le backend.

Flask utilise automatiquement ce dossier pour localiser les fichiers HTML à rendre via la fonction render_template().

## Contenu `index.html`

#### Structure

- **Formulaire POST** : Envoie l'expression saisie au serveur Flask pour évaluation
- **Champ d'affichage** : Affiche le résultat du calcul (lecture seule)
- **Grille de boutons** : Contient les chiffres (0-9), les opérateurs (+, -, \*, /), un bouton clear (C) et le bouton égale (=)
- **Fonctions JavaScript** :
  - `appendToDisplay(value)` : Ajoute une valeur au champ d'affichage
  - `clearDisplay()` : Efface le contenu du champ d'affichage

#### Liaison au CSS

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```

Utilise la fonction Jinja2 `url_for()` pour générer le chemin correct vers le fichier CSS.

### Dépendances

- Flask (moteur de template Jinja2)

- Fichiers CSS situés dans le dossier static/

- Fonctions JavaScript intégrées ou liées

### Hypothèses et contraintes

- Un élément HTML avec l’identifiant display doit exister.

- Le formulaire doit utiliser la méthode POST.
