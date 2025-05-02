from modules.brute_forcer import brute_force_login
from modules.payload_generator import generate_payload
from modules.port_scanner import dvwa_scanner, DVWA_PATHS

def display_menu():
    """Displays available toolkit options."""
    print("\nPenetration Testing Toolkit")
    print("---------------------------")
    print("1. Brute-Force Password Tester")
    print("2. Payload Generator")
    print("3. Port Scanner")

    return input("\nSelect a module (1-3): ")

def get_password_list(file_path):
    """Reads passwords from a file safely."""
    try:
        with open(file_path, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Password file '{file_path}' not found.")
        return None

def main():
    """Handles user input and executes the selected penetration testing module."""
    choice = display_menu()

    if choice == "1":
        url = input("Enter login URL: ")
        username = input("Enter username: ")
        password_file = input("Enter path to password file (default: passwords.txt): ") or "passwords.txt"
        password_list = get_password_list(password_file)
        if password_list:
            brute_force_login(url, username, password_list)

    elif choice == "2":
        generate_payload()

    elif choice == "3":
        target_url = input("Enter target URL (e.g., http://localhost/DVWA-master): ")
        dvwa_scanner(target_url, DVWA_PATHS)

    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()