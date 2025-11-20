class bankovniucet1:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0

    def vloz(self, suma):

        if suma >= 0:
             self.__zustatek += suma


    def vyber(self, suma):

        if suma >=0:
            self.__zustatek -= suma


    def __str__(self):
        return f"Ucet vlastni {self.jmeno} a je na nem {self.__zustatek} kc"
    





if __name__ == "__main__":
    ucet = bankovniucet1("Alice")
    ucet.vloz(100)
    ucet.vloz(-50)
    ucet.vyber(25)
    print(ucet)
