import pytest

from tests.conftest import grass1, grass2, product1


def test_grass(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_smartphone_error(grass1):
    with pytest.raises(TypeError):
        grass1 + product1  # noqa


def test_smartphone_add(grass1, grass2):
    total_value = grass1 + grass2
    expected_value = (grass1.price * grass1.quantity) + (grass2.price * grass2.quantity)
    assert total_value == expected_value
