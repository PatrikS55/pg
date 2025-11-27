class InvalidData(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"Osoba({self.jmeno}, {self.telefon}, {self.email})"
#jmeno 
    @property
    def jmeno(self):
        return self.__jmeno
    
    @jmeno.setter
    def jmeno(self, hodnota: str):
        if not isinstance(hodnota, str):
            raise InvalidData("Jméno musí být text!")

        for c in hodnota:
            if not c.isalpha() and not c.isspace():
                raise InvalidData(f"Chybně zadané jméno: {hodnota}")

        self.__jmeno = hodnota

#telefon
    @property
    def telefon(self):
        return self.__telefon

    @telefon.setter
    def telefon(self, hodnota: str):

        if not isinstance(hodnota, str):
            raise InvalidData("Telefon musí být textový řetězec!")

            cislo = hodnota

        
        if not cislo.isdigit():
            raise InvalidData(f"Telefon může obsahovat jen číslice: {hodnota}")

        
        MAX_DELKA = 12   
        if len(hodnota) > MAX_DELKA:
            raise InvalidData(f"Telefon je příliš dlouhý! Max {MAX_DELKA} znaků.")

        self.__telefon = hodnota

#mail
    @property
    def emmail(self, hodnota, str):
        if "@" not in hodnota:
            raise InvalidData(f"není @")
        if not hodnota.endswith(".cz"):
            raise InvalidData(f"není cz")
        if not hodnota.replace("@")
if __name__ == "__main__":
    o1 = Osoba("Tomáš", "+42015745578", "ahoj@email.cz") 
    print(o1)