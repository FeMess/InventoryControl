from models.cli import CLI
from models.inventory_manager import InventoryManager

if __name__ == "__main__":
    manager = InventoryManager()
    command_line = CLI(manager)
    command_line.present_system()
