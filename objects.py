class Tomas:
    def __init__(self,nombre,estado):
        self.nombre=nombre
        self.estado="apagada"

    def enceder(self):
        self.estado="funcionando"
    
    def apagar(self):
        self.estado= "apagada"
    

    def reportar(self):
        print(f"{self.nombre} esta {self.estado}")
    
torno1= Tomas("Torno CNC 1", "apagada")
torno1.reportar()
torno1.enceder()
torno1.reportar()

class Hija(Tomas):
    def __init__(self,nombre,velocidadrpm):
        super().__init__(nombre,"apagada")
        self.velocidadrpm=velocidadrpm

    def reportar(self):
        print(f"{self.nombre} esta {self.estado} a {self.velocidadrpm} RPM")

torno2 = Hija("Torno CNC 2", 1200)
torno2.reportar()
torno2.enceder()   # ojo, heredado de Tomas, con esa ortografía
torno2.reportar()


class Fresadora(Tomas):
    def __init__(self,nombre,velocidadfresa):
        super().__init__(nombre,"apagada")
        self.velocidadfresa= velocidadfresa
    
    def reportar(self):
        print(f"{self.nombre} esta {self.estado} a {self.velocidadfresa}")

try:
    valor= int(input("ingresa la velocidad en rpm"))
    print(f"La velocidad es {valor} RPM")
except ValueError:
    print("No es un numero valido")


