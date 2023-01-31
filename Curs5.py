# Functia = zona de cod cu o mica logica proprie care poate fi folosita /refolosita (apelata)de oricate ori avem nevoie
# functie simpla (fara parametrii si return)
def hello_world():
    print('Hello World!')
hello_world()
hello_world() # nu putem apela functia fara paranteze
# daca o functie nu este apelata, codul din interiorul ei nu va fi executat
x = hello_world() # codul din functie va fi executat si x va lua valoarea None (functia nu returneaza nimic) - variabila x
print(x)
def say_hi_name(name): # name este un parametru
    print(f'Hi! My name is {name}')
say_hi_name('Ion') # Ion este un argument al parametrului name/functiei respective
lista_nume = ['Iuliana','Cosmin','Andrei']
say_hi_name(lista_nume)
for nume in lista_nume:
    say_hi_name(nume)

# definim o functie care sa returneze daca un numar de la tastatura este par sau impar
def is_even():
    numar = int(input('Introduceti numarul: '))
    if numar %2 == 0:
        return True
    else:
        return False
is_even() #nu are rost sa definim un parametru la functie daca apoi o sa atribuim o valoare in interiorul functiei respective

def is_even2(numar):
    if numar %2 == 0:
        return True
    else:
        return False
argument_numar = int(input('Introduceti numarul: '))
y = is_even2(argument_numar)
print(y) # printam ce ne returneaza functia prin return - afiseaza True sau False
if is_even2(10) == True:
    print('10 este par')

# o functie care sa returnam suma tuturor elementelor dintro lista:
def suma_numere (lista_numere):
    suma = 0
    for numar in lista_numere:
        suma += numar
    return suma
lista_1 = [1,2,3,4]
print(suma_numere(lista_1))
lista_2 = [7,10,3,4]
print(suma_numere(lista_2))

# sa cream o functie care ne returneaza valoarea maxima dintro lista
def nr_maxim (lista):
    maxim = 0
    for numere in lista:
        if maxim < numere:
            maxim = numere
    return maxim
lista_2 = [7,10,3,4]
print(f'Numarul maxim este {nr_maxim(lista_2)}')

def numar_maxim2 (*numere): # steluta ne ofera posibilitatea sa introducem mai multe argumente atribuite aceleiasi variabile
    maxim = 0
    for numere in numere:
        if maxim < numere:
            maxim = numere
    return maxim
print(numar_maxim2(1,2,3,4,5,6,30))

def numar_maxim2 (*numere): # steluta ne ofera posibilitatea sa introducem mai multe argumente atribuite aceleiasi variabile
    maxim = 0
    for numere in numere:
        if maxim < numere:
            maxim = numere
    return maxim, 'numar maxim'
m = numar_maxim2(1,2,3,4,5)
print(m)
SAU
m,string = numar_maxim2(1,2,3,4,5)
print(numar_maxim2(1,2,3,4,5,6,30))
print(m)
print(string)

# variabila globala = variabila definita in afara functiei care poate fi folosita in interiorul oricarei functii
var_globala = 30
print(str(var_globala),'din afara functiei')
def dummy ():
    # var_globala = 60
    # print(str(var_globala), 'din interiorul functiei') # valoarea variabilei globale ramane nemodificata in afara functiei
    # pentru a modifica valoarea variabilei globale in interiorul unei functii folosim key-wordul .global
    global var_globala
    # var_globala = 70
    print(var_globala)
dummy()
print(var_globala)

def say_my_age(age):
    print(age)
    # return 'Sunt aici'
print(say_my_age(5))

def say_my_age(age=10):
    print(age)
say_my_age() # returneaza 10, valoarea setata default de noi
say_my_age(30) # returneaza 30, valoarea data de noi ca si argument la functie

# cand apelam o functie care nu are return, ea cand e apelata afiseaza None
'''
def - key word care anunta inceputul definirii unei functii
say_my_age - numele functiei - este dat de catre user, poate fi orice nume, dar sa fie sugestiv pt actiunea pe care o facem
() - reprezentant al zonei in care putem sa specificam parametrii (parametrii sunt optionali)
: - repreziinta inceputul corpului functiei 
corpul functiti (asemanator structurilor if / while / for)

'''