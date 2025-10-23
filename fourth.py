
def pesec(start, cil, obsazene):
    r, s = start
    cr, cs = cil
    obsazene = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}
    if cs != s:
        return False

    if cil in obsazene:
        return False

    if cr == r + 1:
        return True

    if r == 2 and cr == r + 2:
        if (r + 1, s) not in obsazene:
            return True

    return False

def strelec(start, cil, obsazene):
    r, s = start
    cr, cs = cil
    obsazene = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}
    
    if cil in obsazene:
        return False
    

    if 





def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    r, s = cilova_pozice

    if not (1 <= r <= 8 and 1 <= s <= 8):
        return False

    if figurka["typ"] == "pěšec":
        return pesec(figurka["pozice"], cilova_pozice, obsazene_pozice)

    return False


if __name__ == "__main__":
    pesec_fig = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec_fig, (3, 2), obsazene_pozice))
    print(je_tah_mozny(pesec_fig, (4, 2), obsazene_pozice))
    print(je_tah_mozny(pesec_fig, (1, 2), obsazene_pozice))

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))
