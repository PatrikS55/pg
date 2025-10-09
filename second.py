def cislo_text(cislo):
    # funkce zkonvertuje číslo do jeho textové reprezentace (0–100)
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    x = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    y = ["dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    z = ["deset", "jedenáct", "dvaná"
    "ct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    

    if cislo <= 9:
        return x[cislo]
    elif 10 <= cislo <= 19:
        return z[cislo - 10]
    elif cislo == 100:
        return "sto"
    else:
        a = cislo // 10
        b = cislo % 10
        if b == 0:
            return y[a - 2]
        else:
            return y[a - 2] + " " + x[b]




if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)
