import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from operators import add, subtract, multiply, divide


class TestAdd:
    def test_add_integers(self):
        assert add(3, 4) == 7

    def test_add_floats(self):
        assert add(2.5, 3.5) == 6.0

    def test_add_mixed(self):
        assert add(3, 2.5) == 5.5

    def test_add_negative(self):
        assert add(-3, 4) == 1

    def test_add_zero(self):
        assert add(0, 5) == 5

class TestSubtract:
    def test_subtract_integers(self):
        assert subtract(3, 4) == -1

    def test_subtract_floats(self):
        assert subtract(2.5, 3.5) == -1.0

    def test_subtract_mixed(self):
        assert subtract(3, 2.5) == 0.5

    def test_subtract_negative(self):
        assert subtract(-3, 4) == -7

    def test_subtract_zero(self):
        assert subtract(0, 5) == -5

class TestMultiply:
    def test_multiply_integers(self):
        assert multiply(3, 4) == 12

    def test_multiply_floats(self):
        assert multiply(2.5, 3.5) == 8.75

    def test_multiply_mixed(self):
        assert multiply(3, 2.5) == 7.5

    def test_multiply_negative(self):
        assert multiply(-3, 4) == -12

    def test_multiply_zero(self):
        assert multiply(0, 5) == 0

class TestDivide:
    def test_divide_integers(self):
        assert divide(20, 4) == 5

    def test_divide_floats(self):
        assert divide(7.5, 2.5) == 3.0

    def test_divide_mixed(self):
        assert divide(10, 2.5) == 4.0

    def test_divide_negative(self):
        assert divide(-20, 4) == -5

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_remainder(self):
        assert divide(7, 3) == (7/3)