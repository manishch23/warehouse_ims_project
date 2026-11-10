from warehouse_core.products import add_product, add_stock, display_products
from warehouse_core.location import add_location, display_locations
from warehouse_core.security import (
    read_positive_int,
    display_masked_api_key,
    run_validation_demo,
)


def show_menu() -> None:
    print("\n========== WAREHOUSE IMS ==========")
    print("1. View all products")
    print("2. Add a new product")
    print("3. Add stock to a product")
    print("4. View warehouse locations")
    print("5. Add a warehouse location")
    print("6. Security validation demo")
    print("7. Display masked API token")
    print("8. Exit")


def main() -> None:
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            display_products()

        elif choice == "2":
            product_id = input("Enter product ID: ").strip().upper()
            name = input("Enter product name: ").strip()
            quantity = read_positive_int("Enter opening quantity: ")
            if quantity is None:
                continue

            try:
                price = float(input("Enter product price: ").strip())
                if price < 0:
                    print("Price cannot be negative.")
                    continue
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue

            location_id = input("Enter location ID: ").strip().upper()
            add_product(product_id, name, quantity, price, location_id)

        elif choice == "3":
            product_id = input("Enter product ID: ").strip().upper()
            quantity = read_positive_int("Enter quantity to add: ")
            if quantity is not None:
                add_stock(product_id, quantity)

        elif choice == "4":
            display_locations()

        elif choice == "5":
            location_id = input("Enter new location ID: ").strip().upper()
            name = input("Enter warehouse name: ").strip()
            city = input("Enter city: ").strip()
            if location_id and name and city:
                add_location(location_id, name, city)
            else:
                print("All location fields are required.")

        elif choice == "6":
            run_validation_demo()

        elif choice == "7":
            display_masked_api_key()

        elif choice == "8":
            print("Thank you for using Warehouse IMS.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
