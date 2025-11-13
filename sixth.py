import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne obsah stránky zadané v parametru url
    a vrátí seznam všech odkazů (href) nalezených v HTML.
    """

    # Stáhne stránku
    response = requests.get(url)

    # Ověří, že se stránka načetla úspěšně
    if response.status_code != 200:
        raise Exception(f"Chybný status kód: {response.status_code}")

    # Načte textový obsah stránky
    html = response.text

    # Najde všechny výskyty <a href="něco">
    hrefs = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]+)"', html)

    return hrefs


if __name__ == "__main__":
    try:
        # Získá URL z argumentu příkazové řádky
        url = sys.argv[1]

        # Zavolá funkci
        hrefs = download_url_and_get_all_hrefs(url)

        # Vypíše všechny odkazy
        print("Nalezené odkazy:")
        for h in hrefs:
            print(h)

    except Exception as e:
        print(f"Program skončil chybou: {e}")
