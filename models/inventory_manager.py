from models.product import Product


class InventoryManager:
    def __init__(self):
        self.products = []

    # Public Methods

    def new_product(self, name, price):
        self._validate_name(name)
        self._validate_price(price)

        new_identifier = self._find_new_identifier()
        name = name.strip().title()

        new_product = Product(new_identifier, name, price)
        self.products.append(new_product)

        return new_product

    def list_products(self):
        return self.products.copy()

    def view_product(self, identifier):
        self._validate_identifier(identifier)

        for product in self.products:
            if product.ID == identifier:
                return product

        raise ValueError("The product ID does not exist.")

    def update_product(self, identifier, name, price):
        self._validate_name(name)
        self._validate_price(price)

        product = self.view_product(identifier)
        name = name.strip().title()

        product.name = name
        product.price = price

    def remove_product(self, identifier):
        product = self.view_product(identifier)

        self.products.remove(product)

    def register_entry(self, identifier, quantity):
        self._validate_quantity(quantity)

        product = self.view_product(identifier)

        product.quantity += quantity

    def register_exit(self, identifier, quantity):
        self._validate_quantity(quantity)

        product = self.view_product(identifier)

        if product.quantity < quantity:
            raise ValueError("The product does not have this quantity.")

        product.quantity -= quantity

    # Internal Methods
    def _find_new_identifier(self):
        biggest_ID = 0

        for product in self.products:
            biggest_ID = max(biggest_ID, product.ID)

        return biggest_ID + 1

    def _validate_identifier(self, identifier):
        if not isinstance(identifier, int):
            raise TypeError("The identifier must be a integer numeric value.")

        if not identifier > 0:
            raise ValueError("The identifier must be a positive value.")

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("The product name must be a string value.")

        if not name.strip():
            raise ValueError("The product must have a name.")

    def _validate_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("The price must be a numeric value.")

        if not price >= 0:
            raise ValueError("The price must be a positive or neutral value.")

    def _validate_quantity(self, quantity):
        if not isinstance(quantity, (int, float)):
            raise TypeError("The quantity must be a numeric value.")

        if not quantity > 0:
            raise ValueError("The quantity must be a positive value.")
