# 1. o variabila este o zona de memorie care tine date
# 2. am declarat si initializat variabilele string, int, float, boolean
numele_meu = 'Diana'
varsta = 38
pretul_vacantei = 1515.55
nume_de_baiat = False

# 3. am folosit functia type() pt a verifica tipul de date
print(type(numele_meu))
print(type(varsta))
print(type(pretul_vacantei))
print(type(nume_de_baiat))

'''
4. rotunjeste float-ul folosind functia round() si salveaza aceasta modificare in aceeasi variabila(suprascriere); 
verifica tipul acesteia
'''
pretul_vacantei=round(pretul_vacantei)
print(f'Vacanta a costat {pretul_vacantei} euro') # linie scrisa doar pt verificare
print(type(pretul_vacantei))

'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolva nepotrivirile de tip prin ce modalitate doresti
'''
print(f'Numele meu este {numele_meu}')
print(f'Diana are {varsta} de ani')
print(f'Vacanta a costat {pretul_vacantei} euro')
print(f'{numele_meu} este nume de baiat? {nume_de_baiat}')

# 6. Citește de la tastatură: numele; prenumele. Afișează: 'Numele complet are x caractere'.
numele=input('Scrieti numele: ')
prenumele=input('Scrieti prenumele: ')
numele=len(numele)
prenumele=len(prenumele)
lungimea = numele+prenumele
print(f'Numele complet are {lungimea} caractere')
SAU
numele=input('Scrieti numele: ')
prenumele=input('Scrieti prenumele: ')
print (f'Numele complet are {int(len(numele)) + int(len(prenumele))} caractere')

# 7. Citește de la tastatură:lungimea;lățimea. Afișează: 'Aria dreptunghiului este x'.
lungimea=input('Scrieti lungimea: ')
latimea=input('Scrieti latimea: ')
lungimea=int(lungimea)
latimea=int(latimea)
aria=lungimea*latimea
print(f'Aria dreptunghiului este {aria}')
SAU
lungimea=input('Scrieti lungimea: ')
latimea=input('Scrieti latimea: ')
print(f'Aria dreptunghiului este {int(lungimea)+int(latimea)}')

# 8.Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# afișează de câte ori apare cuvântul 'the';

string = 'Coral is either the stupidest animal or the smartest rock'
print(string.count('the'))

# 9.  Același string. Afișează de câte ori apare cuvântul 'the';Printează rezultatul.

 pare acelasi ca ex 8, nu inteleg diferenta

# 10.Același string.Folosiți un assert ca să verificați dacă acest string conține doar numere.

string = 'Coral is either the stupidest animal or the smartest rock'
assert string.isdigit(), 'Stringul nu contine doar numere'
print('Stringul contine doar numere')

# TEMA 1 OPTIONALA

#??? 1. citește de la tastatură un string de dimensiune impară;afișează caracterul din mijloc.
import math
x = input('textul este: ')
assert len(x)%2 != 0, 'Lungimea stringului este para'
caracter_mijloc = math.floor(len(x)/2)
print(x[caracter_mijloc])

#2.Folosind assert, verifică dacă un string este palindrom.
text=input('Stringul meu este: ' )   sau text=str(input('Stringul meu este: '))
assert text == text[::-1], 'Stringul nu este palindrom'
print('Stringul este palindrom')


#3.3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

print('alabala portocala'.split())

# 4.citește un string de la tastatură (ex: alabala portocala);
# salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

text = str(input('Scrie un string: '))
prima_litera = text[0]
x=text[1:-1]
string_modificat = text[0]+text[1:len(text)-1].replace(x,x.upper())+text[len(text)-1]
print(string_modificat)

# 5.- citește un user de la tastatură;citește o parolă;afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
# eg: parola abc => *** # parola abcd => ****

username = input("username: ")
parola = (input("parola: "))
lungimea = '*' * len(parola)
print(f'Parola pt user {username} este {lungimea} si are {len(lungimea)} caractere')

# SAU VARIANTA fara STELUTE

username = input("username: ")
parola = (input("parola: "))
numar_caractere = int(len(parola))
print(parola.replace('numar_caractere',''))
print(f'Parola pt user {username} este {parola} si are {int(len(parola))} caractere')









