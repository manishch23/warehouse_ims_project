# [WAREHOUSE CORE: LOCATION MANAGEMENT]

locations = {
    "LOC001": {"name": "Main Warehouse", "city": "Delhi"},
    "LOC002": {"name": "Secondary Warehouse", "city": "Noida"},
}


def add_location(location_id: str, name: str, city: str) -> bool:
    """Add a warehouse location if its ID is not already in use."""
    if location_id in locations:
        print("Location ID already exists.")
        return False

    locations[location_id] = {"name": name, "city": city}
    print("Warehouse location added successfully.")
    return True


def display_locations() -> None:
    """Display all registered warehouse locations."""
    print("\n--- Warehouse Locations ---")
    if not locations:
        print("No locations registered.")
        return

    for location_id, details in locations.items():
        print(
            f"{location_id} | {details['name']} | "
            f"{details['city']}"
        )
