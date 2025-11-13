import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} prefix")
        sys.exit(1)

    prefix = sys.argv[1]
    print(f"Download models for prefix: {prefix}")

    response = requests.get("https://www.seznam.cz")

    if response.ok:
        print(response.text)
    else:
        print(f"Nastala chyba: {response.status_code}")
