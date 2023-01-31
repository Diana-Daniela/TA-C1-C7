''''
Incapsulare = posibilitatea de a proteja atributele/metodele unei clase, folosind modificatorii de vizibilitate
- private (privat, adica atributul/metoda poate fi accesata doar in interiorul clasei in care a fost definit)
            -- se defineste cu underscore (__) in fata: (__variabila sau __metoda(): )
- protected (protejat, atributul poate fi accesat doar din clasa in care a fost definita, dar si din clasele copil ale acesteia, insa NU din exterior)

Atunci cand avem un atribut ascuns putem folosi metode speciale pt a interactiona cu el:
numite getter si setter, delter
getter -> pt a-l vedea a avea accea la atribut
setter -> pt a-i schimba valoarea
delter - pt a sterge valoarea

Conventie: aceste metode trebuie denumite cu set_,delete_ si get_ + numele variabilei

'''

class Car:

    __variabila_privata = "privat"
    _variabila_protected = "protected"

    def __init__(self,var_protected):
        self._variabila_protected = var_protected
    #getter
    def get_variabila_privata(self):
        return self.__variabila_privata
    #setter
    def set_variabila_privata(self,var):
       self.__variabila_privata = var

    #deleter
    def delete_variabila_privata(self):
        self.__variabila_privata = None


masina = Car('Update Protected')
# print(masina._variabila_protected)   # convetie ca aceasta variabila sa nu fie accesata.

# print(masina.__variabila_privata)   #-> eroare, variabilele private nu avem acces

print(masina.get_variabila_privata())
masina.set_variabila_privata("Update Private")

print(masina.get_variabila_privata())
masina.delete_variabila_privata()

print(masina.get_variabila_privata())


# "------------------------------------------------------------------"
# Getter, setter, delete intr-un mod pythonic

class CarPy:

    def __init__(self,color):
        self.__color = color
        self.__nr_roti = 0
    @property
    def color(self):
        return self.color

    @property
    def nr_roti(self):
        return self.nr_roti

    @color.getter
    def color(self):
        print(f"Getter: Culoare {self.__color}")
        return self.__color

    @color.setter
    def color(self,color):
        print(f"setter: Setam culoarea in {color}")
        self.__color = color

    @color.deleter
    def color(self):
        self.__color =None


car_py = CarPy("negru")
car_py.color
car_py.color = "Albastru"
car_py.color
del car_py.color
car_py.color