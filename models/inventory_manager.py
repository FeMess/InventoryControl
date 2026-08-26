from models.product import Product


class InventoryManager:
    def __init__(self):
        self.products = []

    def new_product(self, name, price):

        if not name or not price:
            return False

        new_ID = self.find_new_ID()
        new_product = Product(new_ID, name, price)

        self.products.append(new_product)

        return True

    def list_products(self):
        return self.products

    def view_product(self, ID):
        pass

    def update_product(self, name, price):
        pass

    def remove_product(self, ID):
        pass

    def register_entry(self, ID):
        pass

    def register_exit(self, ID):
        pass

    def find_new_ID(self):
        biggest_ID = 0

        for product in self.products:
            biggest_ID = max(biggest_ID, product.ID)

        return biggest_ID + 1
