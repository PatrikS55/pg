class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"
    
    def __add__(self, other):
         x = self.x + other.x
         y = self.y + other.y
         return Vektor(x, y)
    def __mul__(self, scalar):
         retrun Vektor(self.x * scalar.x, self.y * scalar.y)
         
    
if __name__ == "__main__":
        v1 = Vektor(2,3)
        v2 = Vektor(3,4)

        print(v1)
        print(v2)

        v3 = v1 + v2
        print(v3)

    

        