# from models.inventory_manager import InventoryManager
import os
from time import sleep


class CLI:
    def __init__(self, manager):
        self.manager = manager

    def present_system(self):
        while True:
            self._show_header()

            print("\n[0] - Exit")
            print("[1] - New Product")
            print("[2] - Deactivate Product")
            print("[3] - Update Product")
            print("[4] - View Product")
            print("[5] - List Products")
            print("[6] - Register Entry")
            print("[7] - Register Exit")

            user_choice = input("\nWhich option would you like to do? ")

            try:
                self._validate_choice(user_choice)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                continue

            response = self._process_choice(user_choice)

            if response == "EXIT":
                break

    # Internal Methods (User Input)
    def _show_header(self):
        os.system("clear")
        print("-" * 30)
        print("| Inventory Control, Welcome! |")
        print("-" * 30)

    def _validate_choice(self, user_choice):
        if not user_choice in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            raise ValueError("This option is not allowed.")

    def _validate_price(self, price):
        try:
            price = float(price)
        except ValueError:
            raise ValueError("The price must be a integer value.")

        return price

    def _validate_identifier(self, identifier):
        try:
            identifier = int(identifier)
        except ValueError:
            raise ValueError("The identifier must be a integer value.")

        return identifier

    def _validate_quantity(self, quantity):
        try:
            quantity = float(quantity)
        except ValueError:
            raise ValueError("The quantity must be a integer value.")

        return quantity

    def _process_choice(self, user_choice):
        if user_choice == "0":
            return "EXIT"

        elif user_choice == "1":
            self._show_header()

            print("\nSelected option: New Product\n")

            product_name = input("Product Name: ")
            product_price = input("Product Price: ")

            try:
                product_price = self._validate_price(product_price)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            product = self.manager.new_product(product_name, product_price)
            print(
                f"\nThe material {product.name} ({product.id}) has been created successfully."
            )
            sleep(2)

        elif user_choice == "2":
            self._show_header()

            print("\nSelected option: Deactivate Product\n")

            products_list = self.manager.list_products()

            for product in products_list:
                print(f"[{product.id}] {product.name} ({product.status.title()})")

            product_identifier = input("\nProduct ID: ")

            try:
                product_identifier = self._validate_identifier(product_identifier)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            try:
                self.manager.deactivate_product(product_identifier)
                print(
                    f"\nThe product ({product_identifier}) has been inactivated successfully."
                )
                sleep(2)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

        elif user_choice == "3":
            self._show_header()

            print("\nSelected option: Update Product\n")

            products_list = self.manager.list_products()

            for product in products_list:
                print(f"[{product.id}] {product.name} ({product.status.title()})")

            product_identifier = input("\nProduct ID: ")
            try:
                product_identifier = self._validate_identifier(product_identifier)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            print("\nNew Values")
            new_product_name = input("Product Name: ")
            new_product_price = input("Product Price: ")

            try:
                new_product_price = self._validate_price(new_product_price)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            try:
                self.manager.update_product(
                    product_identifier, new_product_name, new_product_price
                )
                print(
                    f"\nThe product ({product_identifier}) has been updated successfully."
                )
                sleep(2)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

        elif user_choice == "4":
            self._show_header()

            print("\nSelected option: View Product\n")

            products_list = self.manager.list_products()

            for product in products_list:
                print(f"[{product.id}] {product.name} ({product.status.title()})")

            product_identifier = input("\nProduct ID: ")
            try:
                product_identifier = self._validate_identifier(product_identifier)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            try:
                product = self.manager.view_product(product_identifier)
                print(
                    f"\n[{product.id}] {product.name} ({product.status.title()}) | {product.quantity:.2f} | R${product.price:.2f} | R${product.price * product.quantity:.2f}"
                )
                input("\n[Press Enter]")
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

        elif user_choice == "5":
            self._show_header()

            print("\nSelected option: List Products\n")

            products_list = self.manager.list_products()

            for product in products_list:
                print(f"[{product.id}] {product.name} ({product.status.title()})")

            input("\n[Press Enter]")

        elif user_choice == "6":
            self._show_header()

            print("\nSelected option: Registry Entry\n")

            products_list = self.manager.list_products()

            for product in products_list:
                print(
                    f"[{product.id}] {product.name} ({product.status.title()}) | {product.quantity:.2f}"
                )

            product_identifier = input("\nProduct ID: ")
            try:
                product_identifier = self._validate_identifier(product_identifier)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            product_quantity = input("Product Quantity: ")
            try:
                product_quantity = self._validate_quantity(product_quantity)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            try:
                self.manager.register_entry(product_identifier, product_quantity)
                print("\nThe quantity has been added to this product successfully.")
                sleep(2)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

        elif user_choice == "7":
            self._show_header()

            print("\nSelected option: Registry Exit\n")

            products_list = self.manager.list_products()

            for product in products_list:
                print(
                    f"[{product.id}] {product.name} ({product.status.title()}) | {product.quantity:.2f}"
                )

            product_identifier = input("\nProduct ID: ")
            try:
                product_identifier = self._validate_identifier(product_identifier)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            product_quantity = input("Product Quantity: ")
            try:
                product_quantity = self._validate_quantity(product_quantity)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return

            try:
                self.manager.register_exit(product_identifier, product_quantity)
                print("\nThe quantity has been removed to this product successfully.")
                sleep(2)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                return
