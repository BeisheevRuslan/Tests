import pytest
from tasks.discr import quadratic_equation_solution, find_discriminant


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 8, 15, (-3.0, -5.0)),
        (1, -13, 12, (12.0, 1.0)),
        (-4, 28, -49, 3.5),
        (1, 1, 1, 'корней нет'),
    ],
)
def test_quadratic_equation_solution(a, b, c, expected):
    assert quadratic_equation_solution(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected_condition",
    [
        (1, 1, 1, "< 0"),
        (-4, 28, -49, "== 0"),
        (1, -13, 12, "> 0"),
    ],
)
def test_find_discriminant(a, b, c, expected_condition):
    D = find_discriminant(a, b, c)
    if expected_condition == "< 0":
        assert D < 0
    elif expected_condition == "== 0":
        assert D == 0
    else:
        assert D > 0
