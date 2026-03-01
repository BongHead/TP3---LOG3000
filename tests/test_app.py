"""
Tests unitaires pour l'application Flask de la calculatrice.

Ce module teste :
- la fonction calculate()
- les différents cas d'erreur
- les routes HTTP GET et POST
"""
import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour importer les modules de l'application
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app import app, calculate

def test_calculate_addition():
    """Test de la fonction calculate pour une addition simple."""
    assert calculate("3 + 4") == 7


def test_calculate_subtraction():
    """Test de la fonction calculate pour une soustraction simple."""
    assert calculate("10 - 5") == 5

def test_calculate_multiplication():
    """Test de la fonction calculate pour une multiplication simple."""
    assert calculate("6 * 7") == 42

def test_calculate_division():
    """Test de la fonction calculate pour une division simple."""
    assert calculate("20 / 4") == 5

def test_calculate_division_by_zero():
    """Test de la fonction calculate pour une division par zéro."""
    with pytest.raises(ZeroDivisionError):
        calculate("10 / 0")

def test_calculate_empty_expression():
    """Test de la fonction calculate pour une expression vide."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate("")

def test_calculate_non_string_expression():
    """Test de la fonction calculate pour une expression non-string."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate(123)

def test_calculate_invalid_operands():
    """Test de la fonction calculate pour des opérandes non numériques."""
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("a + 3")


def test_client_get():
    """Test de la route '/' pour une requête GET."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"display" in response.data

def test_client_post_valid_expression():
    """Test de la route '/' pour une requête POST avec une expression valide."""
    with app.test_client() as client:
        response = client.post('/', data={'display': '3 + 4'})
        assert response.status_code == 200
        assert b"7" in response.data

