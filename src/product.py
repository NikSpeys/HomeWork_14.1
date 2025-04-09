class Product:
    name: str
    description: str
    price: float
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict):
        return cls(
            name=new_product.get("name"),
            description=new_product.get("description"),
            price=new_product.get("price"),
            quantity=new_product.get("quantity"),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        print("Цена не должна быть нулевая или отрицательная")
