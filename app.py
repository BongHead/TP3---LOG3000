"""
Calculatrice web simple utilisant Flask.
Ce module définit une application web qui permet à l'utilisateur d'entrer une expression arithmétique
simple (contenant exactement un opérateur) et d'obtenir le résultat du calcul.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique simple contenant exactement un opérateur.

    La fonction reçoit une chaîne de caractères représentant une expression
    binaire (ex. : "3+4", "10.5/2"). Les espaces sont ignorés. Un seul
    opérateur, défini dans le dictionnaire global OPS, est autorisé.

    L'expression doit respecter le format suivant :
        <nombre><opérateur><nombre>

    Paramètres
    ----------
    expr (str) : Chaîne représentant une expression arithmétique simple contenant exactement un opérateur.

    Retour
    ----------
    float : Résultat de l'application de l'opérateur aux deux opérandes.

    Exceptions
    ----------
    ValueError : Si l'expression est vide.
    ValueError : Si l'expression n'est pas une chaîne de caractères.
    ValueError : Si plus d'un opérateur est présent.
    ValueError : Si l'opérateur est absent ou mal positionné.
    ValueError : Si les opérandes ne peuvent pas être converties en float.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gère la route principale de l'application web.

    Cette fonction affiche l'interface de la calculatrice et traite
    les soumissions du formulaire. 

    - En méthode GET : elle affiche simplement la page avec un résultat vide.
    - En méthode POST : elle récupère l'expression envoyée via le formulaire,
      tente de l'évaluer à l'aide de la fonction `calculate`, puis retourne
      le résultat ou un message d'erreur en cas d'exception.

    Retour
    ----------
    Response : Page HTML générée à partir du template 'index.html', incluant le résultat du calcul ou un message d'erreur.

    Exceptions
    ----------
        Les erreurs générées par la fonction `calculate` sont interceptées et converties en message d'erreur affiché à l'utilisateur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)