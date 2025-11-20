class osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    
    def __str__(self):
        return f"Osoba: {self.jmeno}"
    
    def pridat_rok(self):
        pass
    

class student(osoba):
    def __init__(self, jmeno, rocnik):
        super().__init__(jmeno)
        self.rocnik = rocnik
    
    def __str__(self):
        return f"Student: {self.jmeno} studuje {self.rocnik}"
    
    def pridat_rok(self):
        self.rocnik += 1

class ucitel(osoba):
    def __init__(self, jmeno, praxe):
        super().__init__(jmeno)
        self.praxe = praxe

    def __str__(self):
        return f"Ucitel: {self.jmeno} ma {self.praxe} let praxe"
    
    def pridat_rok(self):
        self.praxe += 1


if __name__ == "__main__":
    student1 = student("Alice", 2)
    student2 = student("Bob", 1)

    ucitel1 = ucitel("Prof", 10)

    print(ucitel1)
    for i in range(20):
        ucitel1.pridat_rok()
    print(ucitel1)



    osoby = [student1, ucitel1, student2]
    for osoby in osoby:
        for i in range(10):
            osoba.pridat_rok(1)

    print(ucitel1)
    print(student1)
    print(student2)
