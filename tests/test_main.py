from typing import Type

from src.main import Calculator
from contextlib import nullcontext as dose_not_raise
import pytest


class TestCalculator:
    @pytest.mark.parametrize(
        'x, y, res, exception',
        [
            (1, 2, 3, dose_not_raise()),
            (1.0, 2.0, 3.0, dose_not_raise()),
            (1, "1", 2, pytest.raises(TypeError))
        ]
    )
    def test_add(self, x, y, res, exception):
        with exception:
            assert Calculator.add(x, y) == res

    @pytest.mark.parametrize(
        'x, y, res, exception',
        [
            (1, 2, 0.5, dose_not_raise()),
            (4, 2, 2, dose_not_raise()),
            (4, "2", 2, pytest.raises(TypeError)),
            (4, 0, 0, pytest.raises(ZeroDivisionError))
        ]
    )
    def test_divide(self, x, y, res, exception):
        with exception:
            assert Calculator.divide(x, y) == res
