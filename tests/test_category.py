import pytest

from src.category import Category
from src.product import Product


def test_category_init(category1):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 185
    assert Category.category_count == 1
    assert Category.product_count == 3


# def test_category2_init(category2):
#     assert category2.name == "Телевизоры"
#     assert (
#         category2.description
#         == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
#     )
#     assert len(category2.products) == 2


def test_products_property(product1, product2, product3):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.price == 210000.0
    assert product3.quantity == 14


def test_str():
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            ["Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5],
            ["Iphone 15", "512GB, Gray space", 210000.0, 8],
            ["Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14],
        ],
    )

    assert category1.name == "Смартфоны"


def test_str_price():
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product3.price == 31000.0


def test_new_product(product_dict, product4):
    product4 = Product.new_product(product_dict)
    assert product4.name == "Стиральная машина"
    assert product4.description == "Описание Стиральной машины"
    assert product4.price == 23450.00
    assert product4.quantity == 5


def test_add_product(product1, category3):
    category3.add_product(product1)
    assert category3.product_count == 9


def test_category_type_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(1)


def test_category_type_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(1)


def test_middle_price(all_products):
    category1 = Category(name="тест", description="тест", products=all_products)
    assert category1.middle_price() == 84423.08

    category2 = Category(name="тест", description="тест", products=[])
    assert category2.middle_price() == 0
