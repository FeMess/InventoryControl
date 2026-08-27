class Product:
    def __init__(self, identifier: int, name: str, price: float):
        self.id = identifier
        self.name = name
        self.price = price
        self.quantity = 0
        self.status = "active"
