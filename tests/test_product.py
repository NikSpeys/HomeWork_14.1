from src.product import Product


def test_product1_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product2_init(product2):
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8


def test_product3_init(product3):
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14


def test_new_product_classmethod(new_product):
    assert new_product["name"] == "Samsung Galaxy S23 Ultra"
    assert new_product["description"] == "256GB, Серый цвет, 200MP камера"
    assert new_product["price"] == 180000.0
    assert new_product["quantity"] == 5


def test_price_setter():
    product = Product("Клавиатура", "Механическая клавиатура", 10000.00, 30)
    assert product.price == 10000.00

    product.price = 12000.00
    assert product.price == 12000.00
