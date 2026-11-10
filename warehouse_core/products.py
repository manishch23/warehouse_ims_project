# [WAREHOUSE CORE: PRODUCT / INVENTORY MANAGEMENT]

products = {
    "P101": {
        "name": "Laptop",
        "quantity": 25,
        "price": 55000.00,
        "location": "LOC001",
    },
    "P102": {
        "name": "Keyboard",
        "quantity": 40,
        "price": 1200.00,
        "location": "LOC002",
    },
}


def add_product(product_id: str, name: str, quantity: int,
                price: float, location_id: str) -> bool:
    """Register a new product in the inventory."""
    if product_id in products:
        print("Product ID already exists.")
        return False
    if quantity <= 0 or price < 0:
        print("Quantity must be positive and price cannot be negative.")
        return False

    products[product_id] = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "location": location_id,
    }
    print("Product added successfully.")
    return True


def display_products() -> None:
    """Display all products and their current stock."""
    print("\n--- Inventory ---")
    if not products:
        print("No products available.")
        return

    for product_id, details in products.items():
        print(
            f"{product_id} | {details['name']} | "
            f"Stock: {details['quantity']} | "
            f"Price: Rs. {details['price']:.2f} | "
            f"Location: {details['location']}"
        )


def add_stock(product_id: str, quantity: int) -> bool:
    """Increase the stock of an existing product."""
    if product_id not in products:
        print("Product ID not found.")
        return False
    if quantity <= 0:
        print("Stock quantity must be positive.")
        return False

    products[product_id]["quantity"] += quantity
    print("Stock updated successfully.")
    return True
