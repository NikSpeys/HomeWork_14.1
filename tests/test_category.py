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
            ["Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14]]
    )

    assert category1.name == 'Смартфоны'

def test_str_price():
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product3.price == 31000.0
