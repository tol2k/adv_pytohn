import pytest
from contextlib import nullcontext as does_not_raise


class Calculator:
    def add(x: int| float, y: int| float) -> float:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError
        return x + y

    def sub(x: int| float, y: int| float) -> float:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError
        return x - y

    def mult(x: int| float, y: int| float) -> float:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError
        return x * y

    def div(x: int| float, y: int| float) -> float:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError
        return x / y



class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, result, expect",
        [
            (1, 2, 3, does_not_raise()),
            (4, 5, 9, does_not_raise()),
            (-100, 0 , -100, does_not_raise()),
            (3, '5', 0, pytest.raises(TypeError))
        ])
    def test_add(self, x, y, result, expect):
        with expect:
            assert Calculator.add(x, y) == result

    @pytest.mark.parametrize(
        "x, y, result, expect",
        [
            (3, 2, 1, does_not_raise()),
            (9, 5, 4, does_not_raise()),
            (-100, 0, -100, does_not_raise()),
            (3, '5', 0, pytest.raises(TypeError))
        ])
    def test_sub(self, x, y, result, expect):
        with expect:
            assert Calculator.sub(x, y) == result

    @pytest.mark.parametrize(
        "x, y, result, expect",
        [
            (1, 2, 2, does_not_raise()),
            (4, -5, -20, does_not_raise()),
            (-100, 0, 0, does_not_raise()),
            (3, '5', 0, pytest.raises(TypeError))
        ])
    def test_mult(self, x, y, result, expect):
        with expect:
            assert Calculator.mult(x, y) == result

    @pytest.mark.parametrize(
        "x, y, result, expect",
        [
            (1, 2, 0.5, does_not_raise()),
            (4, -5, -0.8, does_not_raise()),
            (-100, 0, 0, pytest.raises(ZeroDivisionError)),
            (3, '5', 0, pytest.raises(TypeError))
        ])
    def test_div(self, x, y, result, expect):
        with expect:
            assert Calculator.div(x, y) == result
