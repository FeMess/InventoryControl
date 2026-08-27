from datetime import datetime

from models.movement import Movement
from models.product import Product


class InventoryManager:
    def __init__(self):
        self.products = []
        self.history = []

    # Public Methods

    def new_product(self, name, price):
        self._validate_name(name)
        self._validate_price(price)

        name = name.strip().title()
        new_product = Product(self._find_new_identifier(self.products), name, price)

        self.products.append(new_product)
        return new_product

    def list_products(self):
        return self.products.copy()

    def view_product(self, identifier):
        self._validate_identifier(identifier)

        for product in self.products:
            if product.id == identifier:
                return product

        raise ValueError("The product ID does not exist.")

    def update_product(self, identifier, name, price):
        self._validate_name(name)
        self._validate_price(price)

        product = self.view_product(identifier)
        name = name.strip().title()

        product.name = name
        product.price = price

    def deactivate_product(self, identifier):
        product = self.view_product(identifier)

        product.status = "inactive"

    def register_entry(self, identifier, quantity):
        self._validate_quantity(quantity)

        product = self.view_product(identifier)

        product.quantity += quantity

        # Saving ENTRY Movement
        self._register_movement(product, "ENTRY", quantity)

    def register_exit(self, identifier, quantity):
        self._validate_quantity(quantity)

        product = self.view_product(identifier)

        if product.quantity < quantity:
            raise ValueError("The product does not have this quantity.")

        product.quantity -= quantity

        # Saving EXIT Movement
        self._register_movement(product, "EXIT", quantity)

    # Internal Methods
    def _register_movement(self, product, movement_type, quantity):
        new_movement = Movement(
            self._find_new_identifier(self.history),
            datetime.now(),  # noqa: DTZ005
            product.id,
            movement_type,
            quantity,
        )

        self.history.append(new_movement)

    def _find_new_identifier(self, list_objects):
        biggest_id = 0

        for item in list_objects:
            biggest_id = max(biggest_id, item.id)

        return biggest_id + 1

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
