import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5), (3, 7, 10), (-2, 5, 3),
    (2, 10, 12), (0.1, 0.2, 0.3)])
def test_add(a, b, expected):
    from calculate import add
    result = add(a, b)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize("c, d, expected2", ([
    (4, 2, 2), (5, 1, 4), (8, 2, 6)]))
def test_sub(c, d, expected2):
    from calculate import sub
    result = sub(c, d)
    assert result == expected2
