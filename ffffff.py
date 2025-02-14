class cbrking:
    def __init__(self, species):
        self.species = species


class Plavat:
    def __init__(self, swim_speed):
        self.swim_speed = swim_speed

    def swim(self):
        return f"Плывёт со скоростью {self.swim_speed} км в миллисекунду"


class Letat:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed

    def fly(self):
        return f"Летит со скоростью {self.fly_speed} км в миллисекунду"


class cbrk(cbrking, Plavat, Letat):
    def __init__(self, name, swim_speed, fly_speed):
        cbrking.__init__(self, "Чебурек с вокзала")
        Plavat.__init__(self, swim_speed)
        Letat.__init__(self, fly_speed)
        self.name = name

    def make_sound(self):
        return "Ай лев тигр"


cheburek = cbrk("Чебурек", 49, 52)

print(f"{cheburek.name} — это {cheburek.species}")
print(cheburek.make_sound())
print(cheburek.swim())
print(cheburek.fly())
