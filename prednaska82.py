from abc import ABC, abstractmethod

class Tvar(ABC):

    @abstractmethod
    def spocitej_obsah(self):
        pass

    def __str__(self):
        return f"Tento geometrický tvar má obsah: {self.spocitej_obsah()}"


class Obdelnik(Tvar):
    def __init__(self, sirka, delka):
        self.sirka = sirka
        self.delka = delka

    def spocitej_obsah(self):
        return self.sirka * self.delka


class Ctverec(Tvar):
    def __init__(self, strana):
        self.strana = strana

    def spocitej_obsah(self):
        return self.strana ** 2


if __name__ == "__main__":

    

    o = Obdelnik(3, 5)
    c = Ctverec(4)

    print(o)
    print(c)
