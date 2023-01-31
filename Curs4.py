'''
STRUCTURI REPETITIVE = modalitati in care putem executa un cod in mod repetat pana cand o anumita conditie nu mai e indeplinita
Exista 4 tipuri de structuri repetitive:
1. while
2. do while (nu este scopul cursului - adaptare in Python)
3. for
4. for each
Modalitati de control al structurilor repetitive:
1.Break (opreste executarea structurii repetitive)
2.Continue (face skip la o iteratie)
'''
'''
while = structura repetitiva in care executam o serie de instructiuni atata timp cat conditia este adevarata
        elementul sau variabila de control a while-ului se declara inainte de acesta
'''
# Ex 1. Printeaza pe ecran toate numerele de la 1 la 10
i=1
while i <= 10:
    print (i)
    i += 1
# debugging = proces prin care analizam codul pentru a vedea cum circula datele
# de fiecare data cand vrem sa facem debugging putem sa punem breaking point (bulina rosie)

# Ex 2. Suma numerelor de la 1 la 500
suma = 0
i = 1
while i <= 500:
    i += 1
    suma += i
print (suma)

# Ex 3. lista cu lunile anului, parcurgem lista si printam fiecare valoare din lista
list1 = ['Ianuarie','Februarie','Martie','Aprilie','Mai','Iunie','Iulie']
index = 0
while index < len(list1):
    print(list1[index])
    index += 1
# parcurgem lista fara a afisa luna Martie si luna Mai
while index < len(list1):
    if list1[index] == 'Martie' or list1[index] == 'Mai':
        index += 1
        continue
    print(list1[index])
    index += 1
# parcurgem lista pana ajungem la luna Aprilie
while index < len(list1):
    if list1[index] == 'Aprilie':
        break
    print(list1[index])
    index += 1
# inlocuim luna Mai cu luna Noiembrie (presupunem ca e o singura luna de Mai)
while index < len(list1):
    if list1[index] == 'Mai':
        list1[index] = 'Noiembrie'
        break
    index += 1
print(f'Lista finala este urmatoarea {list1}')
'''
for = structura repetitiva care este utilizata atunci cand vrem sa parcurgem o structura de date 
cu scopul de a prelucra datele din acea structura de date
poate fi folosit sa executam un set de instructiuni de un numar definit de ori (range)
structura unui for:
-inceputul structurii repetitive 'for'
-variabila de iteratie
-inceputul range-ului de parcurs (default este 0 si optional )
-sfarsitul range-ului de parcurs (obligatoriu) - capatul superior nu este luat in considerare
-pas-ul rangelui (default este 1)
'''
# EX 4. parcurgem toate nr de la 0 la 10; printam separat numerele impare si pare
for i in range(0,10):
    if i %2 == 0:
        print(f'Numarul {i} este par')
    else:
        print(f'Numarul {i} este impar')
# Ex 5. Nested list sau embedded list sau lista imbricata sau matrice
matrice = [
    [1,'test1'],
    [2,'test2',3],
    [5,6,7]
]
# for - primul for va parcurge linie cu linie , al doilea interiorul elementului
for i in range (len(matrice)):
    for j in range(len(matrice[i])):
        print(f'Valoarea de pe pozitia [{i}][{j}] este {matrice[i][j]} ')

luni = ['Ianuarie','Februarie','Martie','Aprilie','Mai','Iunie','Iulie']
for i in range(len(list1)):
    print(list1[i])
for luna in luni: # for each
    print(luna)

lista_culori_disponibile = ["rosu", "galben", "albastru", "fuchsia", "magenta", "roz", "violet", "maro", "negru",
                            "orange", "verde", "indigo"]
liste_culori_de_exclus = ["rosu", "galben", "roz"]
lista_culori_neexcluse = []

for culoare in lista_culori_disponibile:
    if culoare in liste_culori_de_exclus:
        continue
    lista_culori_neexcluse.append(culoare)
print(lista_culori_neexcluse)

# Ex 6. Vrem sa sortam o lista mergesort bubblesort hipsort (!!! Algoritmi de sortare)
lista_nesortata = [1,5,10,2,50,11,20,12]
lista_nesortata.sort() # supracrie lista initiala
print(lista_nesortata)
for i in range(len(lista_nesortata)-1):
    for j in range(len(lista_nesortata)-1):
        if lista_nesortata[j] > lista_nesortata[j+1]:
            lista_nesortata[j],lista_nesortata[j+1]=lista_nesortata[j+1],lista_nesortata[j]
print(lista_nesortata)

# CURS INTRO IN PROGRAMARE = CICLURI REPETITIVE
litri_benzina = 10
while litri_benzina > 0:
    # acceleram
    print('Vrum vrum!')
    # scadem benzina
    litri_benzina -= 1
    if litri_benzina <= 3:
        print('Becul rosu e aprins')
print('STOP! Nu mai avem benzina!')

# dalmatienii
for i in range (1,102):
    print(f'Dalmatianul cu nr {i}')
for i in range (1,102,2): # pasul este 2 - afiseaza dalmatienii din 2 in 2
    print(f'Dalmatianul cu nr {i}')

numere = [3,7,10,20,30]
# parcurgere lista cu for prin intermediul indexului
for i in range(0,len(numere)):
    print(f'Indexul curent este {i}')
    print(f'Numarul curent este {numere[i]}')

# for each
s=0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s=s + numar
print(f'Suma este {s}')
# de cate ori apare 3 in [3,2,3,5,3,3]

















