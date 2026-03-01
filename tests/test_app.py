import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour importer les modules de l'application
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app import app, calculate

def test_calculate_addition():
    """"""
    assert calculate("3 + 4") == 7

def test_calculate_addition_negative_number():
    assert calculate("-3 + 4") == 1

def test_calculate_subtraction():
    assert calculate("10 - 5") == 5

def test_calculate_multiplication():
    assert calculate("6 * 7") == 42

def test_calculate_division():
    assert calculate("20 / 4") == 5

def test_calculate_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("10 / 0")

def test_calculate_empty_expression():
    with pytest.raises(ValueError, match="empty expression"):
        calculate("")

def test_calculate_non_string_expression():
    with pytest.raises(ValueError, match="empty expression"):
        calculate(123)

def test_calculate_invalid_operands():
    with pytest.raises(ValueError, match="could not convert string to float"):
        calculate("a + 3")


def test_client_get():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"display" in response.data

def test_client_post_valid_expression():
    with app.test_client() as client:
        response = client.post('/', data={'display': '3 + 4'})
        assert response.status_code == 200
        assert b"7" in response.data

