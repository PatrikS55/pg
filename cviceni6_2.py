import requests

def download_rates(url):
    response = requests.get(url)

    if response.ok:
        radky = response.text.splitlines()  # rozdělí text na jednotlivé řádky

        for radka in radky[2:]:  # přeskočí první dva řádky (hlavičky)
            parts = radka.split('|')  # rozdělí řádek podle svislítka
            if len(parts) >= 5:
                mena = parts[1]      # název měny
                kurz = parts[4]      # kurz
                print(f"{mena}: {kurz}")
                
    else:
        print(f"Nastala chyba: {response.status_code}")

if __name__ == "__main__":
    listek = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    download_rates(listek)

    
