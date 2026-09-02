import os
from time import sleep


class CLI:
    def __init__(self, manager):
        self.manager = manager

    def present_system(self):
        while True:
            self._show_header()
            self._show_low_stock_products()

            print("\n[0] - Exit")
            print("[1] - New Product")
            print("[2] - Deactivate Product")
            print("[3] - Activate Product")
            print("[4] - Update Product")
            print("[5] - View Product")
            print("[6] - List Products")
            print("[7] - Register Entry")
            print("[8] - Register Exit")
            print("[9] - List Movements")

            user_choice = input("\nWhich option would you like to choose? ")

            try:
                self._validate_choice(user_choice)
            except ValueError as e:
                print(f"\n{e}")
                sleep(3)
                continue

            response = self._process_choice(user_choice)

            if response == "EXIT":
                break

    # Internal Methods
    def _show_header(self):
        os.system("clear")
        print("-" * 50)
        print("|           Inventory Control, Welcome!           |")
        print("-" * 50)

    def _show_low_stock_products(self):
        print("-" * 50)
        print("|               Low Stock Products                |")

        low_stock_products = self.manager.list_low_stock_products()

        if not low_stock_products:
            print("|   There are not any product with low stock.     |")
        else:
            for product in low_stock_products:
                defined_size = 49
                product_input = f"{product.name} | {product.quantity:.2f}"
                total_space = defined_size - len(product_input)

                left_space = total_space // 2
                right_space = total_space - left_space

                print(f"|{' ' * left_space}{product_input}{' ' * right_space}|")

        print("-" * 50)

    def _process_choice(self, user_choice):
        if user_choice == "0":
            return "EXIT"

        elif user_choice == "1":
            self._new_product()

        elif user_choice == "2":
            self._deactivate_product()

        elif user_choice == "3":
            self._activate_product()

        elif user_choice == "4":
            self._update_product()

        elif user_choice == "5":
            self._view_product()

        elif user_choice == "6":
            self._list_products()

        elif user_choice == "7":
            self._register_movement_entry()

        elif user_choice == "8":
            self._register_movement_exit()

        elif user_choice == "9":
            self._list_movements()

    def _show_products(self, product_status):
        products_list = self.manager.list_products(product_status)

        if not products_list:
            raise ValueError("There are not any product available.")

        for product in products_list:
            print(
                f"[{product.id}] {product.name} ({product.status.title()}) | {product.quantity:.2f}"
            )

    # Validating User Input
    def _validate_choice(self, user_choice):
        if not user_choice in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            raise ValueError("This option is not allowed.")

    def _parse_price(self, price):
        try:
            price = float(price)
        except ValueError:
            raise ValueError("The price must be a integer value.")

        return price

    def _parse_identifier(self, identifier):
        try:
            identifier = int(identifier)
        except ValueError:
            raise ValueError("The identifier must be a integer value.")

        return identifier

    def _parse_quantity(self, quantity):
        try:
            quantity = float(quantity)
        except ValueError:
            raise ValueError("The quantity must be a integer value.")

        return quantity

    # Manager Methods
    def _new_product(self):
        self._show_header()

        print("\nSelected option: New Product\n")

        product_name = input("Product Name: ")

        try:
            self.manager._validate_name(product_name)
        except ValueError as e:
            print(f"\n{e}")
            sleep(3)
            return

        product_price = input("Product Price: ")

        try:
            product_price = self._parse_price(product_price)
        except ValueError as e:
            print(f"\n{e}")
            sleep(3)
            return

        product = self.manager.new_product(product_name, product_price)
        print(
            f"\nThe material {product.name} ({product.id}) has been created successfully."
        )
        sleep(2)

    def _deactivate_product(self):
        self._show_header()

        print("\nSelected option: Deactivate Product\n")

        try:
            self._show_products("active")
        except ValueError as e:
            print(f"{e}")
            sleep(3)
            return

        product_identifier = input("\nProduct ID: ")

        try:
            product_identifier = self._parse_identifier(product_identifier)
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

    def _activate_product(self):
        self._show_header()

        print("\nSelected option: Activate Product\n")

        try:
            self._show_products("inactive")
        except ValueError as e:
            print(f"{e}")
            sleep(3)
            return

        product_identifier = input("\nProduct ID: ")

        try:
            product_identifier = self._parse_identifier(product_identifier)
        except ValueError as e:
            print(f"\n{e}")
            sleep(3)
            return

        try:
            self.manager.reactivate_product(product_identifier)
            print(
                f"\nThe product ({product_identifier}) has been activated successfully."
            )
            sleep(2)
        except ValueError as e:
            print(f"\n{e}")
            sleep(3)
            return

    def _update_product(self):
        self._show_header()

        print("\nSelected option: Update Product\n")

        try:
            self._show_products("all")
        except ValueError as e:
            print(f"{e}")
            sleep(3)
            return

        product_identifier = input("\nProduct ID: ")

        try:
            product_identifier = self._parse_identifier(product_identifier)
        except ValueError as e:
            print(f"\n{e}")
            sleep(3)
            return

        print("\nNew Values")
        new_product_name = input("Product Name: ")
        new_product_price = input("Product Price: ")

        try:
            new_product_price = self._parse_price(new_product_price)
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

    def _view_product(self):
        self._show_header()

        print("\nSelected option: View Product\n")

        try:
            self._show_products("all")
        except ValueError as e:
            print(f"{e}")
            sleep(3)
            return

        product_identifier = input("\nProduct ID: ")

        try:
            product_identifier = self._parse_identifier(product_identifier)
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

    def _list_products(self):
        self._show_header()

        print("\nSelected option: List Products\n")

        try:
            self._show_products("all")
        except ValueError as e:
            print(f"{e}")
            sleep(3)
            return

        input("\n[Press Enter]")

    def _register_movement_entry(self):
        self._show_header()

        print("\nSelected option: Registry Entry\n")

        try:
            self._show_products("active")
        except ValueError as e:
            print(f"{e}")
            sleep(3)
            return

        product_identifier = input("\nProduct ID: ")

        try:
            product_identifier = self._parse_identifier(product_identifier)
        except ValueError as e:
            print(f"\n{e}")
            sleep(3)
            return

        product_quantity = input("Product Quantity: ")

        try:
            product_quantity = self._parse_quantity(product_quantity)
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

    def _register_movement_exit(self):
        self._show_header()

        print("\nSelected option: Registry Exit\n")

        try:
            self._show_products("active")
        except ValueError as e:
            print(f"{e}")
            sleep(3)
            return

        product_identifier = input("\nProduct ID: ")

        try:
            product_identifier = self._parse_identifier(product_identifier)
        except ValueError as e:
            print(f"\n{e}")
            sleep(3)
            return

        product_quantity = input("Product Quantity: ")

        try:
            product_quantity = self._parse_quantity(product_quantity)
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

    def _list_movements(self):
        self._show_header()

        print("\nSelected option: List Movements\n")

        movements = self.manager.list_movements()

        if not movements:
            print("There are not any movement available.")
            sleep(3)
            return

        for movement in movements:
            product = self.manager.view_product(movement.product_id)

            print(
                f"({movement.id}) {movement.created_on.strftime('%d/%m/%Y %H:%M:%S')} | {product.name} | {movement.movement_type.title()} | {movement.quantity:.2f}"
            )

        input("\n[Press Enter]")
