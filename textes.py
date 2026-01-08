def doba(vek):
    if vek >= 18:
        print("jsi zletilý")
    else:
        print("jsi nezletilý")


vek = 17
#for i in range(5):
    #doba(vek)
    #vek += 1

def sude_liche(cislo):
    if cislo % 2 == 0:
        print(f"{cislo} je sude")
    else:
        print(f"{cislo} je liché")


for i in range(11):
    sude_liche(i)



def je_prvocislo(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


