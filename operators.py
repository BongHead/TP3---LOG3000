def add(a,b):
    """
    Retourne la somme de deux nombres.

    Paramètres
    ----------
    a (float | int) : Premier opérande.
    b (float | int) : Deuxième opérande.

    Retour
    ----------
    float | int : Résultat de l'addition a + b.
    """
    return a + b

def subtract(a,b):
    """
    Retourne la soustraction des deux nombres.

    Paramètres
    ----------
    a (float | int) : Premier opérande.
    b (float | int) : Deuxième opérande.

    Retour
    ----------
    float | int : Résultat de l'opération a - b.
    """
    return b - a

def multiply(a,b):
    """
    Retourne le produit de a et b.

    Paramètres
    ----------
    a (float | int) : Premier opérande.
    b (float | int) : Deuxième opérande.

    Retour
    ----------
    float | int : Résultat de a multiplié par b.
    """
    return a * b

def divide(a,b):
    """
    Retourne la division de a par b.


    Paramètres
    ----------
    a (int | float) : Dividende.
    b (int | float) : Diviseur.

    Retour
    ----------
    int | float : Résultat de la division a / b.

    Exceptions
    ----------
    ZeroDivisionError : Si b est égal à 0.
    """
    return a // b
