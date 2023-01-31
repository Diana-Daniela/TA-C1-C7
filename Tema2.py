1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# if else este o functie stabileste ce se intampla in functie de 1 conditie care imparte rezultatul in 2 fluxuri: daca conditie 1 adevarata se afiseaza un rezultat,
# daca se respecta conditie 2, atunci vom avea al doliea rezultat posibil
2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
x = int(input ("introduceti numarul: "))
if x > 0:
    print ('Numarul este natural')
else:
    print ('Numarul nu este natural')

3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = int(input ("introduceti numarul: "))
if x > 0:
    print ('Numarul este pozitiv')
elif x < 0:
    print ('Numarul este negativ')
else:
    print ('Numarul nu este neutru')

4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
x = int(input ("introduceti numarul: "))
if x >= -2 and x <=13:
    print ('Numarul se gaseste in intervalul (-2,13)')
else:
    print ('Numarul nu se gaseste in intervalul dorit')

#5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
#cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia abs
x = int(input ("introduceti numarul x: "))
y = int(input ("introduceti numarul y: "))
if abs(x-y) < 5:
    print ('Diferenta este mai mica de 5')
else:
    print ('Diferenta nu este mai mica de 5')

#6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
x = int(input ("introduceti numarul x: "))
if not (x>=5 and x<=27 ):
    print('x nu este in intervalul inchis [5,27] ')
else:
    print('x este in intervalul inchis [5,27]')

#7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
#daca nu, afiseaza care din ele este mai mare
x = int(input ("introduceti numarul x: "))
y = int(input ("introduceti numarul y: "))
if x == y:
    print('Numerele sunt egale')
elif x>y:
    print ('x este mai mare decat y')
else:
    print('y este mai mare decat x')

# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).
x = int(input ("introduceti latura 1: "))
y = int(input ("introduceti latura 2: "))
z = int(input ("introduceti latura 3: "))
if x==y==z:
    print ('Triunghiul este echilateral ')
elif x == y or y == z or x == z:
        print ('Triunghiul este isoscel')
else:
    print ('Triunghiul este oarecare')

# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
litera = input('Introduceti o litera: ')
if litera == 'a' or 'A' or 'e' or 'E' or 'i' or 'I' or 'o' or 'O' or 'u' or 'U' or 'â' or 'Â' or 'î' or 'Î':
    print('Litera este vocala')
else:
    print('Litera nu este vocala')

# 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
# a. Peste 9 => A
# b. Peste 8 => B
# c. Peste 7 => C
# d. Peste 6 => D
# e. Peste 4 => E
# f. 4 sau sub => F
nota = float(input('Introduceti nota: '))
if nota >= 9:
    nota = 'A'
    print(f'Nota in sistem american este {nota}')
elif nota >= 8:
    nota = 'B'
    print(f'Nota in sistem american este {nota}')
elif nota >= 7:
    nota = 'C'
    print(f'Nota in sistem american este {nota}')
elif nota >= 6:
    nota = 'D'
    print(f'Nota in sistem american este {nota}')
elif nota >= 4:
    nota = 'E'
    print(f'Nota in sistem american este {nota}')
else:
    nota = 'F'
    print(f'nota ta este {nota}')

TEMA OPTIONALA:
# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input ('Introduceti numarul: '))
if x <= 999:
    print('x nu are minim 4 cifre')
else:
    print('x are minim 4 cifre')

# 2. Verifica daca x are exact 6 cifre
x = int(input ('Introduceti numarul: '))
if 100000 <= x <= 999999:
    print('Numarul are 6 cifre')
else:
    print('Numarul nu are 6 cifre')

# 3. Verifica daca x este numar par sau impar
x = int(input ('Introduceti numarul: '))
if x%2 == 0:
    print ('Numarul este par')
else:
    print('Numarul este impar')

# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele
x = int(input ("introduceti numarul x: "))
y = int(input ("introduceti numarul y: "))
z = int(input ("introduceti numarul z: "))
if x > y and x > z:
    print('Cel mai mare numar este x')
elif y > x and y > z:
    print('Cel mai mare numar este y')
else:
    print('Cel mai mare numar este z')

# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid sau nu
# (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau daca
# suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi)
x = int(input ("introduceti unghiul x: "))
y = int(input ("introduceti unghiul y: "))
z = int(input ("introduceti unghiul z: "))
if (x + y + z) == 180:
    print('triunghiul este valid')
else:
    print('triunghiul nu este valid')

# 6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# citește de la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
# ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'

text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti valoarea lui x: '))
print(text[0:(len(text)-x)])

# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
# din primele 5 caractere + ultimele 5
text = 'Coral is either the stupidest animal or the smartest rock'
text_nou = (text[0:5]+text[len(text)-5:len(text)])
print (text_nou)

# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '
text = 'Coral is either the stupidest animal or the smartest rock'
print(text.find("rock"))
print(text[slice(text.find("rock"))])

# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# functie pentru a face string-ul case insensitive)
text = input("Inroduceti stringul: ")
if text[0].casefold() == text[-1].casefold():
    print('Prima si ultima litera sunt identice')
else:
    print("Prima si ultima litera nu sunt identice")

# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
string = str('0123456789')
print(string[0:len(string)-1:2])
print(string[1:len(string):2])

# Exercitii BONUS
# 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
# inputuri urmatoarele informatii:
# a. Varsta
# b. Insotit de mama
# c. Insotit de tata
# d. Pasaport
# e. Act permisiune mama
# f. Act permisiune tata
# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
# si are permisiune in scris de la celalat parinte
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
# variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
# apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
# Exemple:
# 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca


varsta = int(input("Inroduceti varsta: "))
insotit_de_mama = bool(input('Este insotit de mama? '))
insotit_de_tata = bool(input('Este insotit de tata? '))
pasaport = bool(input('Are pasaport? '))
act_permisiune_mama = bool(input('Are act permsiune mama? '))
act_permisiune_tata = bool(input('Are act permsiune tata? '))
if varsta >= 18 and pasaport == True:
    print('Te poti imbarca')
elif varsta < 18 and pasaport == True and insotit_de_mama == True and insotit_de_tata == True:
    print('Te poti imbarca')
elif varsta < 18 and pasaport == True and insotit_de_mama == True and act_permisiune_tata == True:
    print('Te poti imbarca')
elif varsta < 18 and pasaport == True and insotit_de_tata == True and act_permisiune_mama == True:
    print('Te poti imbarca')
else:
    print('Nu te poti imbarca')

2.S-a facut la curs





