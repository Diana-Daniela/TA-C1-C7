# 1.Clasa Cerc; Atribute: raza, culoare; Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
class Cerc():
    def __init__(self,raza,culoare):
        self.raza = raza
        self.culoare = culoare
    def descriere_cerc(self):
        print(f'culoarea:{self.culoare}, raza:{self.raza}')
    def aria(self):
        return 3.14 * self.raza * self.raza
    def diametru(self):
        return 2 * self.raza
    def circumferinta(self):
        return 2 * 3.14 * self.raza
cerc1 = Cerc(5,'Negru')
cerc1.descriere_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

cerc2 = Cerc(15,'Rosu')
cerc2.descriere_cerc()
print(cerc2.aria())
print(cerc2.diametru())
print(cerc2.circumferinta())

# 2. Clasa Dreptunghi; Atribute: lungime, latime, culoare; Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie
# atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi():
    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descrie(self):
        print(f'lungimea:{self.lungime},latimea:{self.latime},culoarea:{self.culoare}')
    def aria(self):
        return self.lungime * self.latime
    def perimetru(self):
        return (self.lungime + self.latime) * 2
    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
dreptunghi1 = Dreptunghi(15,5,'Albastru')
dreptunghi1.descrie()
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
print(dreptunghi1.schimba_culoarea('Rosu'))
dreptunghi1.descrie()
dreptunghi2 = Dreptunghi(33,77,'Galben')
dreptunghi2.descrie()
print(dreptunghi2.aria())
print(dreptunghi2.perimetru())
print(dreptunghi2.schimba_culoarea('Verde'))
dreptunghi2.descrie()

# 3. Clasa Angajat; Atribute: nume, prenume, salariu; Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat():
    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def descrie(self):
        print(f'nume:{self.nume},prenume:{self.prenume},salariu:{self.salariu}')
    def nume_complet(self):
        return self.nume + ' ' + self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return self.salariu_lunar() * 12
    def marire_salariu(self):
        self.procent = 1.50
        return self.salariu_lunar() * self.procent

angajat1 = Angajat('Ionescu','Dan',4000)
angajat1.descrie()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
print(angajat1.marire_salariu())

angajat2 = Angajat('Popa','Andrei',5000)
angajat2.descrie()
print(angajat2.nume_complet())
print(angajat2.salariu_lunar())
print(angajat2.salariu_anual())
print(angajat2.marire_salariu())

# 4.Clasa Cont; Atribute: iban, titular_cont, sold; Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
#
class Cont():
    def __init__(self,iban,titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')
    def debitare_cont(self):
        numar_incercari = 3
        while numar_incercari != 0:
            suma_retrasa = int(input('Introduceti suma pe care doriti sa o debitati: '))
            self.sold = 7000
            if suma_retrasa not in range(0, self.sold + 1):
                self.sold = self.sold - suma_retrasa
            if self.sold < 0:
                numar_incercari = numar_incercari - 1
                print(
                    f'Suma pe care doresti sa o retragi este mai mare decat suma din cont, mai aveti {numar_incercari} incercari')
            if numar_incercari == 0:
                print('Nu mai puteti face retrageri, cardul este blocat')
                break
            if suma_retrasa in range(0, self.sold + 1):
                self.sold = self.sold - suma_retrasa
                print(f'Soldul in urma debitarii este {self.sold}')
                break
    def creditare_sold(self):
        self.sold = self.sold + int(input('Introduceti suma pe care doriti sa o depuneti in cont: '))
        print(f'Soldul in urma depunerii este {self.sold}')

persoana1 = Cont(8877, 'Ionescu Dan', 2000)
persoana1.afisare_sold()
persoana1.debitare_cont()
persoana1.creditare_sold()
persoana2 = Cont(55236, 'Popa Andrei', 3300)
persoana2.afisare_sold()
persoana2.debitare_cont()
persoana2.creditare_sold()


# EXERCITII OPTIONALE
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie),număr,nume_produs,cantitate,pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
#
class Factura():
    def __init__(self,numar,nume_produs,cantitate,pret_bucata):
        self.serie = 7525
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata
    def schimba_cantitatea(self):
        self.cantitate = int(input('Introduceti noua cantitate: '))
    def schimba_pretul(self):
        self.pret_bucata = int(input('Introduceti noul pret: '))
    def schimba_nume_produs(self):
        self.nume_produs = input('Introduceti noul nume de produs: ')
    def genereaza_factura(self):
        from datetime import date
        print(f'Factura seria: {self.serie}, numarul: {self.numar}')
        data = date.today()
        print(data)
        total = self.cantitate * self.pret_bucata
        print('Nume Produs | Cantitate | Pret Bucata | Total|')
        print(f'{self.nume_produs} | {self.cantitate} | {self.pret_bucata} | {total} |')

telefon = Factura(15, 'telefon', 7, 700)
telefon.genereaza_factura()
telefon.schimba_cantitatea()
telefon.schimba_pretul()
telefon.schimba_nume_produs()
telefon.genereaza_factura()

# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile,
# altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e negativă-eroare, daca viteza e mai mare decat viteza_max
# - masina va accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
#
class Masina():
    def __init__(self, model, viteza_maxima):
        self.marca = 'VW'
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.culoare = 'Gri'
        self.culori_disponibile = {'Negru', 'Albastru', 'Rosu', 'Verde', 'Galben'}
        self.inmatriculata = False
    def descrie(self):
        print(f'{self.marca} | {self.model} | {self.viteza_maxima} | {self.viteza_actuala} | {self.culoare} | {self.inmatriculata}')
    def inmatriculare(self):
        self.inmatriculata = True
    def vopseste(self,culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print(f'Culoarea aleasa nu este disponibila. Va rugam sa alegeti o culoare din lista: {self.culori_disponibile}')
    def accelereaza(self, viteza):
        if viteza < 0:
            print('Nu se poate accelera la viteza negativa')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza
    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Masina s-a oprit si are viteza: {self.viteza_actuala} Km/H')

masina_1 = Masina('Golf', 190)
masina_1.descrie()
masina_1.accelereaza(80)
masina_1.inmatriculare()
masina_1.vopseste('Rosu')
masina_1.descrie()
masina_1.accelereaza(50)
masina_1.descrie()
masina_1.franeaza()

# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
#
class ToDoList():
    def __init__(self):
        self.todo = {}
    def adauga_task(self):
        nume_task = input('Introduceti noul task: ')
        descriere_task = input('Introduceti descrierea task-ului: ')
        self.todo.update({nume_task: descriere_task})
    def finalizeaza_task(self):
        self.todo.pop(input('Introduceti numele task-ului ce a fost finalizat: '))
    def afiseaza_to_do_list(self):
        print(self.todo.keys())
    def afiseaza_detalii_suplimentare(self):
        nume_task = input('Introduceti numele task-ului caruia doriti sa-i vedeti descrierea: ')
        if nume_task in self.todo.keys():
            print(self.todo[nume_task])
        if nume_task not in self.todo.keys():
            raspuns = input('Task-ul nu se afla in todo list, doriti sa il adaugati? da sau nu: ')
            if raspuns == 'da':
                nume_task = input('Introduceti noul task: ')
                descriere_task = input('Introduceti descrierea task-ului: ')
                self.todo.update({nume_task: descriere_task})
            else:
                print('La revedere!')

activitate1 = ToDoList()
activitate1.adauga_task()
activitate1.finalizeaza_task()
activitate1.adauga_task()
activitate1.afiseaza_to_do_list()
activitate1.afiseaza_detalii_suplimentare()
activitate1.afiseaza_to_do_list()
