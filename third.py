def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    for i in range(2, cislo):
        if cislo % i == 0:
            return False
    return True
            

def vrat_prvocisla(maximum):
    result = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            result.append(i)
    return result



    

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
    if je_prvocislo(cislo):
        print(f"{cislo} je prvočíslo.")
    else:
        print(f"{cislo} není prvočíslo.")
