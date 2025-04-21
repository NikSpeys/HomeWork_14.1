import pytest

from tests.conftest import product1, smartphone1, smartphone2


def test_smart(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_error(smartphone1):
    with pytest.raises(TypeError):
        smartphone1 + product1  # noqa


def test_smartphone_add(smartphone1, smartphone2):
    total_value = smartphone1 + smartphone2
    expected_value = (smartphone1.price * smartphone1.quantity) + (smartphone2.price * smartphone2.quantity)
    assert total_value == expected_value
