""""
Clasa Masina
Atribute: marca, culoare, motor_pornit, viteza
Metode: start, stop, accelereaza, incetineste, vopseste
"""
class Masina():
    def __init__(self,marca,culoare):  #acesta este constructorul, se creaza
        self.marca = marca   # atributele clasei, cu self inainte sau variabilele??
        self.culoare = culoare
        self.motor_pornit = False
        self.viteza = 0

    def prezentare_masina(self):
        print(self.marca,self.culoare,self.motor_pornit,self.viteza)

    def start(self):
        self.motor_pornit = True

    def stop(self):
        self.viteza = 0
        self.motor_pornit = False

    def accelereaza(self,accelereaza_cu):
        if self.motor_pornit == True:
            self.viteza += accelereaza_cu
            print(f'Masina a ajuns la {self.viteza} km/h')
        else:
            print('Nu se poate accelera. Motorul nu este pornit.')

    def incetineste(self,incetineste_cu):
        if self.motor_pornit == True and self.viteza > 0:
            if incetineste_cu < self.viteza:
                self.viteza -= incetineste_cu
            else:
                self.viteza = 0
            print(f'Masina a ajuns la {self.viteza} km/h')
        else:
            print('Nu se poate incetini. Motorul nu este pornit sau viteza e deja 0.')

    def vopseste(self,culoare):
        self.culoare = culoare

masina_test = Masina('Volvo','Albastru')
masina_test.prezentare_masina()
masina_test.accelereaza(30)
masina_test.start()
masina_test.accelereaza(30)
print(masina_test.viteza)
masina_test.accelereaza(70)
# masina_test.stop()
print(masina_test.viteza)
masina_test.incetineste(90)
masina_test.incetineste(30)
print(masina_test.culoare)
masina_test.vopseste("Rosu")
print(masina_test.culoare)