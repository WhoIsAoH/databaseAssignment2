from database.database import Database


class InventoryReports:
    def __init__(self, db_file):
        self.db = Database(db_file)


    def generate_inventory_report(self):
        try:
            with self.db.cursor() as cursor:
                cursor.execute("SELECT * FROM inventory")
                inventory_data = cursor.fetchall()

            if not inventory_data:
                print("Inventory is empty.")
                return []

            print("Inventory Report:")
            for item in inventory_data:
                print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Location: {item[3]}")
            return inventory_data

        except Exception as e:
            print(f"Error generating inventory report: {e}")


if __name__ == "__main__":
    db_file = "database/inventory_management.db"
    inventory_reports = InventoryReports(db_file)
    inventory_reports.generate_inventory_report()
