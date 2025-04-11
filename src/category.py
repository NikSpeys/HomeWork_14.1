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


    def add_product(self, product):  # метод дл добавления атрибута  в продукт
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        list_products = ""
        for item in self.__products:
            list_products += f"Название продукта {item.name}, {item.price} руб. Остаток {item.quantity}\n"
        return list_products
