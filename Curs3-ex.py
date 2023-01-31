# avem o lista cu diferite tipuri de date
list1 = ['Maria', 32, True, 12.5]
print(type(list1))
print(list1)

# printeaza nr de elemente din lista de mai sus
print(len(list1))
print(list1[0])
print(list1[-1])

# stergem primul element din lista
list1.remove(list1[0])
print(list1)
list1.pop(0)
print(list1)
first_element = list1.pop(0)
print(first_element)

# adaugam un element nou la finalul listei
list1 = list1 + ['Ion']
print(list1)
list1.append(21)
print(list1)
list1.extend([1,2,3,4])
print(list1)

# adaugam un element pe pozitia cu indexul 2
list1.insert(2,'32')
print(list1)
verificam daca nr 32 apare de mai mult de 1 singura data cu fct assert
assert list1.count(32) > 1, 'Numarul 32 nu apare de mai mult de o singura data'
# verificam daca nr 32 apare de mai mult de 1 singura data cu IF
if list1.count(32) > 1:
    print ('Numarul 32 apare de mai mult de o singura data')
else:
    print('Numarul 32 nu apare de mai mult de o singura data')
# printam inversul listei
list1.reverse()
print(list1)

# DICTIONAR
# cream un dictionar cu 2 elemente; cheile sunt nr intregi, iar valorile zile ale saptamanii
dictionar1 = {0: 'Luni' , 1: 'Marti'}
print(dictionar1)
print(dictionar1.keys())
print(dictionar1.values())
adaugam cheia 2 cu valoarea miercuri
dictionar1 = dictionar1 + {2: 'Miercuri'} # arunca o eroare
print(dictionar1.update({2:'Miercuri'})) # nu returneaza nimic, dar scrie ultimul element la finalul dictionarului

# MAI CLAR LA CURS DE FUNCTII
dictionar1.update({2:'Miercuri'})
print(dictionar1)
eliminam un element, e nevoie sa cunoastem cheia
dictionar1.pop(0)
print(dictionar1)
print(dictionar1.popitem()) # returneaza ultimul element (elimina elementul din dictionarul respectiv)
print(dictionar1)

# verificam daca cheia 0 se afla in dictionar
print(dictionar1[0])
if 0 in dictionar1.keys():
    print(f'Cheia 0 exista si contine valoarea {dictionar1.get(0)}' )
else:
    print('Cheia 0 nu exista')
if 1 in dictionar1.keys():
    print(f'Cheia 1 exista si contine valoarea {dictionar1.get(1)}' )
else:
    print('Cheia 0 nu exista')

# verificam daca valoarea luni se afla in dictionar
if 'Luni' in dictionar1.values():
    print(f'Valoarea Luni exista in dictionar' )
else:
    print('Valoarea Luni nu exista')

# SETURI
new_set = set() # metoda de a declara un set gol
new_set2 = {1,2,3} # stie ca e un set, dar doar cand avem valori
atentie = {} # se declara un dictionar
print(type(new_set))
print(type(new_set2))
print(type(atentie))

# adaugam elemente in set
new_set.update([1,2,3,4,5,6,1]) # nu accepta duplicate
print(new_set)
# adaugam un singur element cu add
new_set.add(7)
print(new_set)
new_set.add(0) # a adaugat elem 0 - pune elementele in ordine - a adaugat pe 0 la inceput
print(new_set)
new_set2 = {'martie', 'aprilie', 1, 2}
print(new_set2)
new_set.update(new_set2)
print(new_set)
print(new_set.difference(new_set2))
print(new_set2.difference(new_set))
print('new_set - new_set2 ' + str(new_set.difference(new_set2))) # returneaza un al 3-lea set ce contine valorile care sunt in new_Set2 si nu sunt in new_set
print('new_set2 - new_set ' + str(new_set2.difference(new_set)))

# intersectia a doua seturi
intersection_set=new_set.intersection(new_set2) # returneaza un al 3-lea set cu valorile comune
print(new_set.intersection(new_set2))
# difference si intersection returneza un SET NOU , NU suprascrie
print(intersection_set)

# verificam daca elementul cu valoarea 3 exista in set
if 3 in new_set:
    print('este')
else:
    print('nu este')

# TUPLE
# creare de tuple:
tupla=tuple()
tupla2=()
print(type(tupla))
print(type(tupla2))
tupla = (10, 20, 30, 40)
print(tupla)
print(tupla.count(30))
print(tupla.index(40)) # returneaza indexul valorii respective
# accesam elementul de pe ultima pozitie
print(tupla[-1])
tupla_nested = (10,20,30,40,(1,2,('ian','feb'),3,4))
print(tupla_nested)
# accesam elementul 3 din tupla
print(tupla_nested[4][3])
# accesam elementul 3 din tupla 3
print(tupla_nested[4][2][1])
if 40 in tupla_nested:
    print ('40 este')
else:
    print ('40 nu este')

if (1,2,('ian','feb'),3,4) in tupla_nested:
    print ('YES')











