def prace_se_seznamem():

    seznam = [100, 5, 3,]

    seznam[2] *= 2
    
    seznam.append(55)

    seznam.sort()

    print(seznam)

def vrat_treti_prvek(seznam):
    if len(seznam) >= 3:
        return seznam[2]
    else:
        return None
    
def prumer(cisla):
    return sum(cisla) / len(cisla)

def naformatuj_text(zak):
    jmeno = zak["jemno"]
    prijmeni = zak["prijmeni"]
    vek = zak["vek"]
    znamky = ["znamky"]
    prumer_znamek = round(prumer(znamky))
    #text = f"student: {zak}(

if __name__ == "__main__":
    #prace_se_seznamem()
    print(vrat_treti_prvek([1,2,3]))
    #print(prumer(cisla))
    



    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1,2,3,1,4]
 }
        
    
     
    student["vek"] += 1
    student["obor"] = "AEFP"
    #print(naformatuj_text(student))

