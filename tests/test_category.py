from src.category import Category


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



