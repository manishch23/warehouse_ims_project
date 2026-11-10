import os

# [SECURE PYTHON: SAFE INPUT VALIDATION]

def read_positive_int(prompt: str):
    """Read a strictly positive integer. Return None if the input is invalid."""
    raw = input(prompt).strip()

    try:
        value = int(raw)
        if value <= 0:
            print("[Security Alert] Number must be strictly positive.")
            return None
        return value
    except ValueError:
        print("[Security Alert] Invalid numeric format. Rejected safely.")
        return None


# [SECURE PYTHON: CREDENTIAL PROTECTION]

def get_api_key() -> str:
    """Read the API key from an environment variable.

    The fallback is only a local-development placeholder, not a real secret.
    """
    return os.getenv("WAREHOUSE_API_KEY", "FALLBACK_LOCAL_DEV_KEY")


def display_masked_api_key() -> None:
    """Display only a masked version of the API key."""
    api_key = get_api_key()
    if len(api_key) >= 4:
        masked_key = f"{api_key[:4]}****"
    else:
        masked_key = "****"
    print(f"API Token safely retrieved: {masked_key}")


def run_validation_demo() -> None:
    """Demonstrate how valid and invalid quantity inputs are handled."""
    print("\\n--- Secure Input Validation Demo ---")
    for test_input in ["25", "-10", "abc"]:
        print(f"Testing input: {test_input}")
        try:
            value = int(test_input)
            if value > 0:
                print("Result: Accepted")
            else:
                print("Result: Rejected - number must be positive")
        except ValueError:
            print("Result: Rejected safely by ValueError catch")
