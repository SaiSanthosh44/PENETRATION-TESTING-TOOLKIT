import requests
from concurrent.futures import ThreadPoolExecutor

# Define common DVWA paths to check
DVWA_PATHS = [
    "", "login.php", "setup.php", "index.php", "security.php",
    "vulnerabilities/xss/", "vulnerabilities/sqli/",
    "vulnerabilities/csrf/", "vulnerabilities/fi/",
]

def check_url(base_url, path):
    """Attempts to access a given URL path on DVWA."""
    url = f"{base_url}/{path}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            return f"[+] Found: {url} (Status: {response.status_code})"
    except requests.exceptions.RequestException:
        pass
    return None

def dvwa_scanner(base_url, paths):
    """Scans DVWA for accessible pages using multithreading."""
    print(f"Scanning {base_url}...\n")

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda path: check_url(base_url, path), paths)

    for result in results:
        if result:
            print(result)
    
    print("\nScan complete.")

# Example usage
if __name__ == "__main__":
    target_url = "http://localhost/DVWA-master"
    dvwa_scanner(target_url, DVWA_PATHS)