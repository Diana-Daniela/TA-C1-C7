""""
Clasa CursProgramare - in numele claselor se foloseste camel case
Atribute: companie, nume_curs, nr_locuri_maxime, studenti
Metode: inscriere_student, descriere_curs, get_locuri_disponibile
"""
from persoana import Persoana


class CursProgramare():
    def __init__(self,companie,nume_curs,nr_locuri_max): # studenti nu avem la inceput, e lista goala la inceput
        self.companie = companie
        self.nume_curs = nume_curs
        self.nr_locuri_max = nr_locuri_max
        self.studenti = []

    def inscriere_student(self, nume_student):
        if self.get_locuri_disponibile() > 0:
            self.studenti.append(nume_student)
        else:
            print('Nu mai sunt locuri disponibile')

    def descriere_curs(self):
        print (f'{self.companie} - {self.nume_curs}')
        print (30*"*")
        if len(self.studenti) > 0:
            print(f'Lista studenti')
            for student in self.studenti:
                print(student.nume, student.prenume)
        else:
            print('Nu sunt studenti inscrisi')

    def get_locuri_disponibile(self):
        return self.nr_locuri_max - len(self.studenti)


student1 = Persoana('Matei', 'Vlad',33)
curs_Python = CursProgramare('IT Factory','Introducere in Python',10)
curs_Python.descriere_curs()
curs_Python.inscriere_student(student1)
curs_Python.descriere_curs()
curs_Python.inscriere_student(student1)
curs_Python.inscriere_student(student1)
curs_Python.inscriere_student(student1)
student2 = Persoana('Luiza', 'Diana',29)
curs_Python.inscriere_student(student2)
curs_Python.inscriere_student(student2)
curs_Python.inscriere_student(student2)
curs_Python.inscriere_student(student2)
curs_Python.inscriere_student(student2)
curs_Python.inscriere_student(student2)
curs_Python.inscriere_student(student2)
curs_Python.inscriere_student(student2)
curs_Python.inscriere_student(student2)
print(curs_Python.get_locuri_disponibile())
curs_Python.descriere_curs()
print(curs_Python.get_locuri_disponibile())