class Equipo:
    def __init__(self, tipo, marca, nums):
        self.tipo = tipo
        self.marca = marca
        self.nums = nums

    def printinfo(self):
        print(self.tipo, self.marca, self.nums)
primero = Equipo("CPU", "Asus", "DFGFG43455D")
primero.printinfo()
