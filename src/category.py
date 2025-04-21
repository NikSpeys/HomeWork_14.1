from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity_products = 0
        for item in self.__products:
            total_quantity_products += item.quantity

        return f"Название категории: {self.name}, количество продуктов: {total_quantity_products} шт\n"

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        else:
            self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        list_products = ""
        for item in self.__products:
            list_products += f"Название продукта {item.name}, {item.price} руб. Остаток {item.quantity}\n"
        return list_products
