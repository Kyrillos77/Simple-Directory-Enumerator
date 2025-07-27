import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python dir_enum.py <target-domain>")
        sys.exit(1)

    target = sys.argv[1]
    
    try:
        with open("wordlist.txt", "r") as f:
            directories = f.read().splitlines()
    except FileNotFoundError:
        print("[-] wordlist.txt not found.")
        sys.exit(1)

    print(f"[+] Starting directory enumeration on {target}...\n")

    for dir in directories:
        url = f"http://{target}/{dir}/"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 404:
                print(f"[+] Valid directory found: {url}")
        except requests.RequestException as e:
            print(f"[-] Error requesting {url}: {e}")

if __name__ == "__main__":
    main()


