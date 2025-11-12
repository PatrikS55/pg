
def deleni(citatel, jmenovatel):
    return citatel / jmenovatel

if __name__ == "__main__":

    try:

        cislo1 = int(input("zadej čitatele: "))
        while cislo1 is None:
            try:

                cislo2 = int(input("zadej jmenovatele: "))
            except Exception:
                print("zadej validní číslo")

                výsledek = deleni(cislo1, cislo2)

                print(výsledek)

             except Exception:

                print("v nasem programu nastala chyba") 