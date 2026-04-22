import pytest

from calc import average


def test_average_of_three():
    assert average([1.0, 2.0, 3.0]) == 2.0


def test_average_single():
    assert average([10.0]) == 10.0


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])
