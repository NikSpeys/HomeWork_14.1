class PrintMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        super().__init__()
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
