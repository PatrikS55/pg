def pesec1(start, cil, obsazene):
    r, s = start
    cr, cs = cil

    if cs != s:
        return False

    
    if cil in obsazene:
        return False

    
    if cr == r + 1:
        return True


    if r == 2 and cr == r + 2 and (r + 1, s) not in obsazene:
        return True

    return False

def strelec1(start, cil, obsazene):
    r, s = start
    cr, cs = cil

    if abs(cr - r) != abs(cs - s):
        return False
    if cil in obsazene:
        return False

    
    dr = 1 if cr > r else -1
    ds = 1 if cs > s else -1
    rr, ss = r + dr, s + ds
    while (rr, ss) != (cr, cs):
        if (rr, ss) in obsazene:
            return False
        rr += dr
        ss += ds
    return True


def vez1(start, cil, obsazene):
    r, s = start
    cr, cs = cil
    if not (r == cr or s == cs):
        return False
    if cil in obsazene:
        return False

    if r == cr:
        step = 1 if cs > s else -1
        for x in range(s + step, cs, step):
            if (r, x) in obsazene:
                return False
    else:
        step = 1 if cr > r else -1
        for y in range(r + step, cr, step):
            if (y, s) in obsazene:
                return False
    return True


def jezdec1(start, cil, obsazene):
    r, s = start
    cr, cs = cil
    if (abs(cr - r), abs(cs - s)) in [(1, 2), (2, 1)] and cil not in obsazene:
        return True
    return False


def dama1(start, cil, obsazene):
    # dáma = věž nebo střelec
    return vez1(start, cil, obsazene) or strelec1(start, cil, obsazene)


def kral1(start, cil, obsazene):
    r, s = start
    cr, cs = cil
    if max(abs(cr - r), abs(cs - s)) == 1 and cil not in obsazene:
        return True
    return False


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    r, s = cilova_pozice
    if not (1 <= r <= 8 and 1 <= s <= 8):
        return False

    typ = figurka["typ"]
    start = figurka["pozice"]

    if typ == "pěšec":
        return pesec1(start, cilova_pozice, obsazene_pozice)
    elif typ == "střelec":
        return strelec1(start, cilova_pozice, obsazene_pozice)
    elif typ == "věž":
        return vez1(start, cilova_pozice, obsazene_pozice)
    elif typ == "jezdec":
        return jezdec1(start, cilova_pozice, obsazene_pozice)
    elif typ == "dáma":
        return dama1(start, cilova_pozice, obsazene_pozice)
    elif typ == "král":
        return kral1(start, cilova_pozice, obsazene_pozice)
    return False



if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))
