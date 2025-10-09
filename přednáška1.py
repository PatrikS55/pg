

if __name__ == "__main__":

    hodnota = input( "zadej číslo")
    hodnota = int(hodnota)

    operator = input( "zadej operátor (+, -, *, /)")

    hodnota2 = input("zadej číslo ")
    hodnota2 = int(hodnota2)

    print(f"operace: {hodnota} {operator} {hodnota2} =")

    výsledek = None

    if operator == "+":
        výsledek = hodnota + hodnota2
    elif operator == "-":
        výsledek = hodnota - hodnota2
    elif operator == "*":
        výsledek = hodnota * hodnota2
    elif operator == "/":
        výsledek = hodnota / hodnota2
    else:
        print(f"neznámý operátor {operator}")

    if výsledek == None:
        print("operace se nezdařila")
    else:
        print(f"výsledek operace: {výsledek}")
    