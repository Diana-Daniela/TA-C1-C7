
# LISTA e o structura de date care pastreaza mai multe valori intro singura variabila
# lista poate sa cuprinda elemente de diferite tipuri de date - in Python
# lista are index incepand de la 0 ca string-urile
# lista este ordonata, adaugam element nou => acesta se pune la final
# lista este mutabila => putem adauga, sterge sau schimba elemente
# in lista putem pune valori duplicate
# len() ne va da dimensiune listei -> cate elemente avem in lista

# declaram si initializam lista:
list1 = ["abc", 34, True, 40, "male", "male"]
fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element care se adauga la final
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print('ultimul element: ', last)
print(fructe)

# de cate ori apare un element
print(fructe.count(3))

# adaugam o lista la lista noastra
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)

# DICTIONAR - cuvantul in STANGA (CHEIA) -> valoarea asociata in dreapta
# DICTIONAR - este ordonat, mutabil (valorile pot si schimbate)
# Cheile sunt unice, nu putem avea chei duplicate, ar crea confuzie
# Cheile sunt ca niste porecle pentru index-uri
# putem folosi len() pt a afla dimensiunea

# declaram si initializam un dictionar
thisdict = {"brand" = "Volvo", "model" = "XC 60", "year" = "2011"}
note_elevi = {'Gigel': 10 , 'Costel':9 , 'Ana' :10}

# adaugam elemente
note_elevi['Sebi'] = 7

# printam dictul
print(note_elevi)

# aflam note (elemente din interior)
print(note_elevi['Sebi'])
print(note_elevi.get('Gigel'))

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# sterg valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'Nu mai avem acest element' ))
print(note_elevi)

# returneaza doar cheile
print(note_elevi.keys())

# SETURI - pastreaza mai multe valori UNICE intro variabila (nu se accepta duplicate)
# NU sunt ordonate sau indexate
# Sunt IMUTABILE - nu putem schimba locatia elementelor
# Se pot DOAR adauga sau sterge elemente
# Putem folosi len() pentru a afla dimensiunea

culori = {'alb', 'rosu', 'galben'}
print(culori)
print(len(culori))

# TUPLU - pastreaza mai multe valori imutabile intro singura variabila
# Valorile sunt ordonate, incep de la index 0
# Valorile sunt imutabile, o data definite, asa raman, nu se mai pot adauga/sterge valori
# Accepta valori duplicate
# Putem folosi len() pentru a afla dimensiunea

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))


# INTREBARI:
# Care este diferenta dintre un set si o tupla?
# Setul nu contine indecsi si nu putem avea duplicate, la tuple e invers
# Cand folosm Dict? Atunci cand avem un context in care avem nevoie de cheie si valoare si de obicei noi stim cheia

'''
RECAPITULARE PE SCURT
tupla = structura de date care se defineste intre 2 paranteze (2,5) - 
        are indecsi
        sunt imutabile
dictionar = structura de date cu cheie si valoare {cheie:valoare} - Ex - aplicatie pt masini - tip, caroserie, marca, tip
            sunt mutabile
            cheile sunt unice
            ordonate
set = structura de date care are elemente unice - aplicatie de tip calendar - lunile anului
      nu sunt ordonate sau indexate
      nu putem schimba locatia elementelor
      se pot adauga sau sterge elemente
liste = structura de date care pastreaza mai multe valori intro singura variabila
        in Python pastreaza diferite tipuri de date
        fiecare element are index
        este mutabila            
'''
