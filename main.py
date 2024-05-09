# main.py

from interface.cli import CLI
from interface.gui import GUI
from inventory.inventory_management import InventoryManagement
from security.authentication import Authentication
from security.authorization import Authorization
from transportation.transportation_management import TransportationManagement
from database.database import Database


def main():
    db_file = 'database/inventory_management.db'
    database = Database(db_file)
    table_file = 'database/create_table.sql'
    database.create_tables(table_file)

    inventory_manager = InventoryManagement(db_file)
    Authorization(db_file)
    Authentication(db_file)
    transportation_manager = TransportationManagement(db_file)

    user_interface = input("Choose interface CLI or GUI: ").lower()
    if user_interface == 'gui':
        gui_interface = GUI(inventory_manager, transportation_manager, db_file)
        gui_interface.run()
    elif user_interface == 'cli':
        cli_interface = CLI(inventory_manager, transportation_manager)
        cli_interface.start()
    else:
        print("Invalid choice. Please choose CLI or GUI.")


if __name__ == "__main__":
    main()
