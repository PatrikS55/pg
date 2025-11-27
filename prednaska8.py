import json

class InvalidData(Exception):
    pass


class Car:
    def __init__(self, znacka, model, barva):
        self.znacka = znacka
        self.model = model
        self.barva = barva

    def __str__(self):
        return f"Auto: {self.znacka} / {self.model} / {self.barva}"


if __name__ == "__main__":

    jdata1 = '{"znacka": "bmw", "model": "x5", "barva": "modra"}'   # řetězec!
    jdata2 = '{"znacka": "bmw", "model": "x6", "barva": "cerna"}' 
    data = json.loads(jdata1)

    # Validace
    for key in ["znacka", "model", "barva"]:
        if key not in data:
            raise InvalidData(f"Invalid data: missing {key}")

    # Přiřazení
    znacka = data["znacka"]
    model = data["model"]
    barva = data["barva"]

    car = Car(znacka, model, barva)
    print(car)
