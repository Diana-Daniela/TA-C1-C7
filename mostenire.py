''''
Mostenire: Capacitatea unei clase de a impartasi atat metode cat si atribute din alta clasa.
Clasa copil mosteneste clasa parinte, astfel clasa copil preia metodele si atributele din clasa parinte.
Clasa copil poate avea oricate metode sau atribute in plus fata de clasa parinte.
!!! (Clasa Parinte nu mosteneste nimic de la clasa/clasele copil)
!!! IN Python O clasa copil poate mosteni mai multe clase parinte - class copil(Parinte1,Parinte2,Parinte3...)
in clasa copil putem apela clasa parinte folosind super()
'''

class Person: # clasa Parinte
    def __init__(self,nume,varsta,adresa):
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa

    def anul_nasterii(self):
        return 2023 - self.varsta

    def descriere(self):
        print(self.nume,self.varsta,self.adresa)

class Student(Person):
    def __init__(self,nume,varsta,adresa,facultate,an_studiu):
        # super() - reprezinta clasa parinte - person in cazul nostru
        # cu super() apelam constructorul clasei parinte
        super().__init__(nume,varsta,adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu
    def descriere(self): # fac suprascriere la metoda "descriere" din clasa parintelui
        super().descriere()
        print(self.facultate,self.an_studiu)


class Angajat(Person):
    def __init__(self,nume,varsta,adresa,companie,salariu):
        super().__init__(nume,varsta,adresa)
        self.companie = companie
        self.salariu = salariu

    def descriere(self):
        super().descriere()
        print(self.companie,self.salariu)

    def salariu_anual(self):
        return self.salariu * 12

class Profesor(Angajat):

    def __init__(self,nume,varsta,adresa,companie,salariu,curs,nr_ore):
        super().__init__(nume,varsta,adresa,companie,salariu)
        self.curs = curs
        self.nr_ore = nr_ore

    def descriere(self):
        super().descriere()
        print(self.curs,self.nr_ore)

# student = Student("Vlad",22,"adresa 1","UTCN",5)
# # print(student.nume)
# # print(student.facultate)
# student.descriere()

profesor = Profesor("vlad",33,"Adresa1","IT Factory", 1000, "Testare Automata", 160)
profesor.descriere()
# print(str(profesor.salariu_anual()) + " Euro")

# persoana = Person("Ana",22,"adresa1")