from datetime import datetime

from models.movement import Movement
from models.product import Product


class InventoryManager:
    def __init__(self):
        self.products = []
        self.history = []

    def new_product(self, name, price):
        self._validate_name(name)
        self._validate_price(price)

        name = name.strip().title()
        new_product = Product(self._find_new_identifier(self.products), name, price)

        self.products.append(new_product)
        return new_product

    def list_products(self, status="all"):
        if status not in ["all", "active", "inactive"]:
            raise ValueError("The status is not valid.")

        if status == "all":
            products_list = self.products.copy()
        else:
            products_list = [
                product for product in self.products if product.status == status
            ]

        return products_list

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

        if product.quantity != 0:
            raise ValueError(
                "The product cannot be deactivated because it has quantity in stock."
            )

        if product.status == "inactive":
            raise ValueError(
                "The product cannot be deactivated because it is already inactive."
            )

        product.status = "inactive"

    def reactivate_product(self, identifier):
        product = self.view_product(identifier)

        if product.status == "active":
            raise ValueError(
                "The product cannot be activated because it is already active."
            )

        product.status = "active"

    def register_entry(self, identifier, quantity):
        self._validate_quantity(quantity)

        product = self.view_product(identifier)
        self._validate_movement(product, "ENTRY", quantity)

        product.quantity += quantity

        # Saving ENTRY Movement
        self._register_movement(product, "ENTRY", quantity)

    def register_exit(self, identifier, quantity):
        self._validate_quantity(quantity)

        product = self.view_product(identifier)
        self._validate_movement(product, "EXIT", quantity)

        product.quantity -= quantity

        # Saving EXIT Movement
        self._register_movement(product, "EXIT", quantity)

    def list_movements(self):
        return self.history.copy()

    def list_low_stock_products(self):
        low_stock_products = [
            product
            for product in self.products
            if product.quantity < 4 and product.status == "active"
        ]

        return low_stock_products

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

    # Validating Business Rules
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

    def _validate_movement(self, product, movement_type, quantity):
        if product.status == "inactive":
            raise ValueError("The product contains inactive status.")

        if movement_type == "EXIT" and product.quantity < quantity:
            raise ValueError("The product does not have the necessary quantity.")
