from přednáška6fibac import fibac
import random

def gamba():
#random.seed(10)
    vysledek = []
    #print(random.choice(symboly))
    symboly = ["🍒", "🍋", "🍉"]
    for i in range(3):
        vysledek.append(random.choice(symboly))
    print(vysledek)
    if len(set(vysledek)) == 1:
        print(f"VYHRÁL SI")
    else:
        print (f"Love budou my nebudem")

if __name__ == "__main__":
    #fib = fibac(10)
    #print(fib)
    gamba()
    