# Dossier Static

Ce dossier contient toutes les ressources statiques de l'application (fichiers CSS, JavaScript, images, etc.).
## Raison d'être
Ce répertoire contient les fichiers statiques servant à la présentation et à l'interface utilisateur de l'application web. Ce sont les ressource statiques qui ne changent pas d'un site à l'autre.
## Contenu

### `style.css`
Feuille de style CSS principale pour l'interface utilisateur de la calculatrice web. Contient les règles de mise en page et de styling pour une meilleure expérience utilisateur.

## Notes

- Les fichiers CSS et JavaScript dans ce dossier sont servis directement par Flask.
- Assurez-vous que tous les fichiers statiques sont correctement référencés dans les templates HTML.
- Pour ajouter de nouvelles ressources, créez des fichiers dans ce répertoire et référencez-les à partir de `templates/index.html`

## Utilisation

Les fichiers statiques sont accessibles à partir du navigateur via des chemins relatifs comme :
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

Cela permet d'utiliser un lien dynamique pour le fichier stylesheet.


## Dépendances et hypothèses

- Flask : L'application configure automatiquement les fichiers statiques dans le répertoire static/ via Flask(__name__)
- HTTP : Les fichiers sont servis avec les en-têtes HTTP appropriés pour le cache et la compression
- CSS : La feuille de style utilise les normes CSS modernes (CSS3)