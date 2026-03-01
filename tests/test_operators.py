
"""
Tests unitaires du module operators.py.

Ce fichier vérifie le bon fonctionnement des fonctions arithmétiques définies dans operators.py:
l'addition, la soustraction, la multiplication et la division.

Les tests couvrent :
- les nombres positifs et négatifs
- les valeurs nulles
- les nombres décimaux
- les cas d'erreur

Ces tests garantissent une fiabilité des opérations utilisées par l'application de calculatrice.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from operators import add, subtract, multiply, divide


class TestAdd:
    def test_add_integers(self):
        """Test de la fonction add pour des entiers."""
        assert add(3, 4) == 7

    def test_add_floats(self):
        """Test de la fonction add pour des nombres à virgule flottante."""
        assert add(2.5, 3.5) == 6.0

    def test_add_mixed(self):
        """Test de la fonction add pour un mélange d'entier et de float."""
        assert add(3, 2.5) == 5.5

    def test_add_negative(self):
        """Test de la fonction add pour des nombres négatifs."""
        assert add(-3, 4) == 1

    def test_add_zero(self):
        """Test de la fonction add pour l'addition avec zéro."""
        assert add(0, 5) == 5

class TestSubtract:
    def test_subtract_integers(self):
        """Test de la fonction subtract pour des entiers."""
        assert subtract(3, 4) == -1

    def test_subtract_floats(self):
        """Test de la fonction subtract pour des nombres à virgule flottante."""
        assert subtract(2.5, 3.5) == -1.0

    def test_subtract_mixed(self):
        """Test de la fonction subtract pour un mélange d'entier et de float."""
        assert subtract(3, 2.5) == 0.5

    def test_subtract_negative(self):
        """Test de la fonction subtract pour des nombres négatifs."""
        assert subtract(-3, 4) == -7

    def test_subtract_zero(self):
        """Test de la fonction subtract pour la soustraction avec zéro."""
        assert subtract(0, 5) == -5

class TestMultiply:
    def test_multiply_integers(self):
        """Test de la fonction multiply pour des entiers."""
        assert multiply(3, 4) == 12

    def test_multiply_floats(self):
        """Test de la fonction multiply pour des nombres à virgule flottante."""
        assert multiply(2.5, 3.5) == 8.75

    def test_multiply_mixed(self):
        """Test de la fonction multiply pour un mélange d'entier et de float."""
        assert multiply(3, 2.5) == 7.5

    def test_multiply_negative(self):
        """Test de la fonction multiply pour des nombres négatifs."""
        assert multiply(-3, 4) == -12

    def test_multiply_zero(self):
        """Test de la fonction multiply pour la multiplication avec zéro."""
        assert multiply(0, 5) == 0

class TestDivide:
    def test_divide_integers(self):
        """Test de la fonction divide pour des entiers."""
        assert divide(20, 4) == 5

    def test_divide_floats(self):
        """Test de la fonction divide pour des nombres à virgule flottante."""
        assert divide(7.5, 2.5) == 3.0

    def test_divide_mixed(self):
        """Test de la fonction divide pour un mélange d'entier et de float."""
        assert divide(10, 2.5) == 4.0

    def test_divide_negative(self):
        """Test de la fonction divide pour des nombres négatifs."""
        assert divide(-20, 4) == -5

    def test_divide_by_zero(self):
        """Test de la fonction divide pour une division par zéro."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_remainder(self):
        """Test de la fonction divide pour une division avec reste."""
        assert divide(7, 3) == (7/3)