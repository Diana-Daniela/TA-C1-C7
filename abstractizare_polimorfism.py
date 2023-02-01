''''
Polimorfism = poli (mai multe) morfism (forma/forme) => ceva care poate lua mai multe forme
In cazul OOP, o metoda poate sa aibe acelasi nume in clase diferite, dar implementari /logica diferita in interior

Abstractizare = este un proces prin care putem sa ascundem o anumita functionalitate specifica fata de utilizator
de asemenea putem forta un anumit comportament in clasele copil.

Utilizatorul stie ce face functionalitatea, dar nu si cum.

Clasa parinte care este o clasa abstracta, nu putem sa cream obiecte din ea, ci doar sa o folosim ca un template pentru clasele copil

In abstractizare avem 2 concepte:
 - interfata -> o clasa care contine doar metode abstracte si atat - In JAVA exista interfete propriu-zise (Interface numeInterfata)
 - clasa abstracta care contine atat metode abstracte, cat si metode proprii cu logica in interiorul lor (In JAVA exista Abstract Class numeclasa ....)

Clasa abstracta trebuie sa mosteneasca clasa ABC (Abstract Class Method)
Fiecare metoda a clasei abstracte trebuie sa arunce exceptia NotImplemented Error sau pass
Clasa abstracta NU are constructor pt ca nu cream obiecte din ea.

O metoda abstracta e o metoda care nu are corp (fara logica)

'''

# def add(a,b,c=0):
#     return(a+b+c)
# print(add(1,2,3))
# print(add(1,2))


from abc import ABC, abstractmethod

class Vehicul(ABC): # asa stim ca clasa Vehicul e clasa abstracta mostenind clasa ABC

    @abstractmethod     #decorator ca sa marcam acesta metoda ca abstracta, implementarea lor se face la clasele copil
    def nr_roti(self):
        raise NotImplementedError

    @abstractmethod
    def nr_locuri(self):
        pass                     # metode abstracte neavand logica si pentru a preveni anumite erori,
                                 # scriem in corpul metodelor pass sau NotImplementedError
    @classmethod
    def metoda_logica_proprie(self):
        print("Aici este o metoda cu logica proprie, nu trebuie implementata in clasa copil")
class Masina(Vehicul):
    def __init__(self,culoare):
        self.culoare= culoare
    def nr_roti(self):  # suntem obligati sa implementam toate metodele abstracte din clasa abstracta parinte
        return 4
    def nr_locuri(self):
        return 5
class Bicicleta(Vehicul):
    def __init__(self,culoare,roti_ajutatoare = False):
        self.culoare = culoare
        self.roti_ajutatoare = roti_ajutatoare
    def nr_roti(self):
        if self.roti_ajutatoare: # echivalentul lui: self.roti_ajutatoare == True
            return 4
        else:
            return 2
    def nr_locuri(self):
        return 1

masina = Masina("verde")  # cream un obiect de tipul masina-nu ne lasa pana nu definim metodele abstracte din clasa abstracta
print(masina.nr_roti())
print(masina.nr_locuri())
masina.metoda_logica_proprie() # are logica proprie, nu trebuie implementata in clasa copil

bicicleta = Bicicleta("rosu")
print(bicicleta.nr_roti())
print(bicicleta.nr_locuri())
bicicleta.metoda_logica_proprie()

# vehicul = Vehicul() # NU putem crea un obiect de tipul clasei abstracte.