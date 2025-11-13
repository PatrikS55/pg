from cviceni6_2 import download_rates
import sys

def currencies_amount(amount_czk, rates):
    conversions = {}
    for currency, rate in rates.items():
        conversions[currency] = amount_czk / rate
    return conversions

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} amount_in_CZK")
        sys.exit(1)

    amount = float(sys.argv[1])


    date, rates = download_rates(
        "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    )

    conversions = currencies_amount(amount, rates)

    print(f"Konverze pro {amount} CZK k datu {date}:")
    for currency, value in conversions.items():
        print(f"{currency}: {value:.2f}")
