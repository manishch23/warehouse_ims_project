# warehouse_ims_project
# Warehouse IMS (Inventory Management System)

A beginner-friendly Python project that demonstrates basic warehouse inventory management using a modular structure.

## Features

- View products currently stored in inventory.
- Add a new product with its ID, name, quantity, price, and warehouse location.
- Increase the stock quantity of an existing product.
- View and register warehouse locations.
- Validate numeric input and reject zero, negative, or non-numeric quantities.
- Retrieve an API token from an environment variable and display it in masked form.

## Project Structure

```text
warehouse_ims_project/
├── warehouse_core/
│   ├── __init__.py
│   ├── location.py
│   ├── products.py
│   └── security.py
├── main.py
└── README.md
```

## Requirements

- Python 3.8 or newer
- No third-party packages are required.

## How to Run

1. Open the `warehouse_ims_project` folder in VS Code.
2. Open the terminal in that folder.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py` instead.

## Security Demonstration

The `security.py` module contains:

- `read_positive_int()`: accepts only positive whole numbers.
- `get_api_key()`: reads `WAREHOUSE_API_KEY` from the environment.
- `display_masked_api_key()`: displays only the first four characters followed by a mask.
- `run_validation_demo()`: demonstrates valid and invalid numeric inputs.

For local development, the program uses a clearly labelled placeholder if the environment variable is not set. Never put a real API key directly in source code or commit it to GitHub.

To set an environment variable in Windows PowerShell for the current terminal session:

```powershell
$env:WAREHOUSE_API_KEY="your-real-api-key"
python main.py
```

## Important Note

This is an educational demonstration. Product and location data are stored in Python dictionaries, so changes are lost when the program closes. A future version could use SQLite or another database for permanent storage.

## Example Test Cases

| Input | Expected result |
|---|---|
| `25` | Accepted |
| `-10` | Rejected |
| `0` | Rejected |
| `abc` | Rejected safely |

## Learning Outcomes

- Python functions and modules
- Importing code between files
- Dictionaries and basic inventory operations
- Input validation and exception handling
- Environment variables and basic credential protection
