# 1. Având lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’. ● Fă același lucru cu un for each. ● Fă același lucru cu un while.
●
for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}')
●
for masina in masini: # for each
    print(f'Masina mea preferata este {masina}')
●
i=0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i += 1

# 2. Aceeași listă: Folosește un for else ; În for - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul. În else: Printează lista.

for i in range(1,len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print(f'Lista mea de masini este: {masini}')

# 3. Aceeași listă: Vine un cumpărător care dorește să cumpere un Mercedes. Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes: Printează ‘am găsit mașina dorită de dvs’ Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel: Printează ‘Am găsit mașina X. Mai căutam‘

index = 0
while index < len(masini):
    if masini[index] == 'Mercedes':
        break
    print(f'Am găsit mașina {masini[index]}. Mai căutam')
    index += 1
print('Am gasit masina dorita de dvs')

# 4. Aceași listă; Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun: Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# - Printează S-ar putea să vă placă mașina x.

index = 0
while index < len(masini):
    if masini[index] == 'Trabant' or masini[index] == 'Lastun':
        index += 1
        continue
    print(f'S-ar putea sa va placa masina: {masini[index]} ')
    index += 1

# 5. Modernizează parcul de mașini: Crează o listă goală, masini_vechi. ● Itereaza prin mașini. ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x. ● Modele noi: x.

masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# 6. Având dict:
pret_masini = {'Dacia': 6800,'Lastun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
# Vine un client cu un buget de 15000 euro. ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul. ● Printează Pentru un buget de sub 15000 euro puteți alege mașină Lastun
# ● Iterează prin listă.

for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de sub {buget} euro puteți alege mașina: {masina}')

# 7. Având lista: numere; ● Iterează prin ea. ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor = 0
for numar in numere:
  if numar == 3:
    contor += 1
print(f'Numărul 3 apare de {contor} ori în listă.')

# 8. Aceeași listă: ● Iterează prin ea ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
s=0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s=s + numar
print(f'Suma este {s}')

# 9. Aceeași listă: ● Iterează prin ea. ● Afișază cel mai mare număr (nu ai voie să folosești max).
numere.sort() # supracrie lista initiala
print(numere)
for i in range(len(numere)-1):
    for j in range(len(numere)-1):
        if numere[j] > numere[j+1]:
            numere[j],numere[j+1]=numere[j+1],numere[j]
print(numere)
print(f'Numarul maxim este {numere[-1]}')

# 10. Aceeași listă: ● Iterează prin ea.● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă. Ex: dacă e 3,să devină -3 ● Afișază noua listă.
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)

# TEMA OPTIONALA
# 1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Itereaza prin listă alte_numere # Populează corect celelalte liste # Afișeaza cele 4 liste la final
for numar in alte_numere:
    if numar % 2 == 0 :
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar >= 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# 2. Aceeași listă: Ordonează crescător lista fară să folosești sort. Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4
for i in range(len(alte_numere)-1):
    for j in range(len(alte_numere)-1):
        if alte_numere[j] > alte_numere [j+1]:
            alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
print(alte_numere)

# 3. Ghicitoare de număr: # numar_secret = Generați un număr random între 1 și 30 # Numar_ghicit = None
# Folosind un while User alege un număr Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
import random
numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_ghicit != numar_secret:
    numar_ghicit = int(input("Alegeți un număr între 1 și 30: "))
    if numar_ghicit > numar_secret:
        print("Numărul secret este mai mic.")
    elif numar_ghicit < numar_secret:
        print("Numărul secret este mai mare.")
    else:
        print("Felicitări! Ai ghicit!")

# 4. Alege un număr de la tastatură Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
nr_introdus = int(input('Introduceti un numar de la 1 la 9: '))
nr_initial = 1
while nr_initial <= nr_introdus:
    print(str(nr_initial)*nr_initial)
    nr_initial += 1

# 5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
# Iterează prin listă 2d Printează ‘Cifra curentă este x’ (hint: nested for - adică for în for)
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Numarul curent este {tastatura_telefon[i][j]}')
