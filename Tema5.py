# Exerciții obligatorii
# 1.Funcție care să calculeze și să returneze suma a două numere
def suma_douanumere(a,b):
    return a + b
print(f'Suma numerelor a si b este {(suma_douanumere(15,25))}')

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def numar_par(numar):
    if numar %2 == 0:
        return True
    else:
        return False
print(f'Numarul meu este par? {numar_par(27)}')

# 3. Funcție care returnează numărul total de caractere din numele tău complet.(nume, prenume, nume_mijlociu)
def numar_caractere(nume, prenume, nume_mijlociu):
    nume = len(nume)
    prenume = len(prenume)
    nume_mijlociu = len(nume_mijlociu)
    return nume + prenume + nume_mijlociu
print(numar_caractere('Lacatusu','Daniela','Diana'))

# 4. Funcție care returnează aria dreptunghiului
def aria_dreptunghiului(lungime,latime):
    return int(lungime)*int(latime)
print(f'Aria dreptunghiului este {aria_dreptunghiului(25,20)}')

# 5. Funcție care returnează aria cercului
def aria_cercului(raza):
    return 3.14*int(raza)*int(raza)
print(f'Aria cercului este {aria_cercului(35)}')

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
def caracter_in_string(x,string):
    if x in string:
        return True
    else:
        return False
print(caracter_in_string('a','xena'))

# 7. Funcție fără return, primește un string și printează pe ecran: Nr de caractere lower case este x Nr de caractere upper case exte y
def lower_upper_string(string):
    lower_case = 0
    upper_case = 0
    for char in string:
        if char.islower():
            lower_case = lower_case + 1
        elif char.isupper():
              upper_case = upper_case + 1
    print(f'Nr de caractere lower case este {lower_case} Nr de caractere upper case este {upper_case}')
lower_upper_string('Avem de NUMARAT literele MICI SI MARI')

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive
def numere_pozitive_din_lista(lista):
    numere_pozitive = []
    for numar in lista:
        if numar >= 0:
            numere_pozitive.append(numar)
    return numere_pozitive
print(numere_pozitive_din_lista([-5,3,8,-6]))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.
def comparare_numere(x,y):
    if x > y:
        print('Primul număr x este mai mare decat al doilea nr y')
    elif x < y:
        print('Al doilea nr y este mai mare decat primul nr x')
    else:
        print('Numerele sunt egale')
comparare_numere(25,50)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
def numar_in_set(numar,set_de_numere):
    if numar in set_de_numere:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        set_de_numere.add(numar)
        print('am adaugat numărul nou în set')
        return set_de_numere
print(numar_in_set(7,{5,7,-20}))

# EXERCITII OPTIOANLE
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
def numar_zile_in_luna(luna):
    if luna in ('Ianuarie','Martie','Mai','Iulie','August','Octombrie','Decembrie'):
        return 31
    elif luna in ('Aprilie','Iunie','Septembrie','Noiembrie'):
        return 30
    elif luna in ('Februarie'):
        return 28
    else:
        return 'Luna invalida'
print(numar_zile_in_luna('Ianuarie'))

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face: a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
def calculator(x, y):
    a = x + y
    print(f'Suma: {a}')
    b = x - y
    print(f'Diferenta: {b}')
    c = x * y
    print(f'Inmultirea: {c}')
    d = x / y
    print(f'Impartirea: {d}')
calculator(10, 2)

# 3. Funcție care primește o lista de cifre (adică doar 0-9) Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
def functie_dict():
    dictionar = {}
    lista = [1, 3, 1, 6, 9, 7, 7, 5, 5]
    for i in range(0, 10):
        contor = 0
        for j in range(0, len(lista)):
            if i == lista[j]:
                contor += 1
                dictionar.update({i: contor})
            else:
                dictionar.update({i: contor})
    return dictionar
a = functie_dict()
print(a)
# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def maxim(a,b,c):
    return max(a,b,c)
print(f'Valoarea maxima dintre ele este {maxim(4,5,6)}')

# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
def suma_de_la_zero_la_numar(n):
    suma = 0
    for i in range(n+1):
        suma += i
    return suma
print(suma_de_la_zero_la_numar(5))

#EXERCITII OPTIONALE BONUS
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
def numere_comune(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)
print(numere_comune([1, 1, 2, 3],[2, 2, 3, 4]))

# 2.Funcție care să aplice o reducere de preț Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.
def pret_cu_reducere(pret_intreg):
    reducere = 100-int(input('Introduceti reducerea: '))
    pret_redus = pret_intreg / 100 * reducere
    while reducere < 0:
        print('suma invalida')
        break
    else:
        return pret_redus
print(pret_cu_reducere(1500))

# 3. Funcție care să afișeze data și ora curentă din ro (bonus: afișați și data și ora curentă din China)
import datetime
def afiseaza_data_ora_curenta():
    data_ora_curenta = datetime.datetime.now()
    print(data_ora_curenta.strftime("%d/%m/%Y %H:%M:%S"))
afiseaza_data_ora_curenta()

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
import datetime
def zile_pana_la_craciun():
    data_curenta = datetime.datetime.now()
    data_craciun = datetime.datetime(2023, 12, 25)
    zile_ramase = (data_craciun - data_curenta).days
    print(f'Mai sunt {zile_ramase} zile pana la Craciun')
zile_pana_la_craciun()





