from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self):
        self.PI = 3.14
    @abstractmethod
    def aria(self):
        raise NotImplementedError
    @classmethod
    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        super().__init__()
        self.__latura = latura
    # getter
    def get_latura(self):  # asa putem accesa variabila privata
        return self.__latura
    # setter
    def set_latura(self, latura2): # asa putem accesa schimba variabila privata
        self.__latura = latura2
    # deleter
    def delete_latura(self):
        self.__latura = None  # asa stergem valoarea respectiva
    def aria(self):
        return self.__latura * self.__latura
class Cerc(FormaGeometrica):
    def __init__(self,raza):
        super().__init__()
        self.__raza = raza
    # getter
    def get_raza(self):
        return self.__raza
    # setter
    def set_raza(self, raza2):
        self.__raza = raza2
    # delter
    def delete_raza(self):
        self.__raza = None
    def aria(self):
        return self.PI * self.__raza * self.__raza
    def descrie(self):
        print('Eu nu am colturi')

Patrat.descrie()  # descrie simplu merge
FormaGeometrica.descrie()
patrat = Patrat(15)
print(patrat.aria())
print((patrat.get_latura()))
print((patrat.set_latura(8)))

Cerc.descrie("self.__raza")
cerc = Cerc(5)
print(cerc.aria())
print((cerc.get_raza()))
print((cerc.set_raza(8)))