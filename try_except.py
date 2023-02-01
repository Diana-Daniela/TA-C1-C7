'''
Exceptie = clase speciale din Python folosite atunci cand ceva nu merge bine in cod
Folosim try-except pt a gestiona posibilele exceptii(erori) aruncate in codul nostru
astfel incat programul sa NU se opreasca
'''

lista_numere = [1,2,3,4,5]
# print(lista_numere[10]) # va sari de eroare pentru ca in lista nu exista indexul 10
# print("Am trecut de exceptie") # nu se executa acest cod

try:
    print(lista_numere[10])
except Exception as e:
    print(e)
print("Am trecut de exceptie")

try:
    print(lista_numere[10])
except IndexError as error:
    print("Index Error: ", error)

try:
    print(lista_numere[10])
except NotImplementedError as e: # aceasta exceptie nu este prinsa in try
    # codul din try nu va arunca niciodata exceptia NotImplementedError - nu e specifica erorii de index inexistent intro lista
    print(e)
print("Am trecut de exceptie") # codul nu va ajunge aici; NotImplementedError nu este specifica erorii de inexistenta index in lista

numar_studenti = int(input("Introduceti numarul de studenti: "))
lista_studenti = []

for student in range(numar_studenti):
    if student > 5:
        print(lista_studenti)
        raise IndexError("Nr de stundeti sa nu fie peste 5")
    lista_studenti.append("Vlad")
    print(student)

print(lista_studenti) # de ce apare Vlad de 6 ori??


