def generate_inventory_report():
    print("Generating inventory report...")


class CLI:
    def __init__(self, inventory_manager, transportation_manager):
        self.db = None
        self.inventory_manager = inventory_manager
        self.transportation_manager = transportation_manager

    def start(self):
        print("Welcome to St. Mary's Logistics Database System")

        while True:
            print("\nPlease select an option:")
            print("1. Add item to inventory")
            print("2. Update item quantity")
            print("3. Add transportation details")
            print("4. Generate inventory report")
            print("5. Register user")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_item_to_inventory()
            elif choice == "2":
                self.update_item_quantity()
            elif choice == "3":
                self.add_transportation_details()
            elif choice == "4":
                generate_inventory_report()
            elif choice == "5":
                self.user_register()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice")

    def update_item_quantity(self):
        item_id = int(input("Enter item ID: "))
        new_quantity = int(input("Enter new quantity: "))

        self.inventory_manager.update_quantity(item_id, new_quantity)
        print("Successfully updated")

    def add_item_to_inventory(self):
        name = input("Enter the name of the item: ")
        quantity = int(input("Enter quantity: "))
        location = input("Enter location: ")

        self.inventory_manager.add_item(name, quantity, location)
        print("successfully item added to inventory")

    def add_transportation_details(self):
        vehicle_id = int(input("Enter vehicle ID: "))
        driver_id = int(input("Enter driver ID: "))
        destination = input("Enter destination: ")
        departure_time = input("Enter departure time: ")
        arrival_time = input("Enter arrival time: ")

        self.transportation_manager.add_transportation(vehicle_id, driver_id, destination, departure_time, arrival_time)
        print("Transportation details added")

    def user_register(self):
        username = input("username:")
        password = input("password:")
        role = input("role:")
        self.user_add_in_db(username ,password, role)

    def user_add_in_db(self, username, password,role):
        self.db.cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                               (username, password, role))
        self.db.conn.commit()


# Usage
db_file = "database/inventory_management.db"
app = CLI(db_file)
app.user_register()


