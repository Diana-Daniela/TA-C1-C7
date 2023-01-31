#CURS 1
# simularea unui bancomat
'''
1.sa definim un user si o parola
2.sa definim un sold al contului
3.sa introduce de la tastatura username si parola cont
4.daca username sau parola este gresita sa se opreasca executarea programului
5.dorim sa scoatem o suma de bani si vrem sa stim daca avem fonduri suficiente
'''

user = 'username'
expected_password = '1234'
sold = 100
username = input("username: ")
assert user == username, 'Username gresit'
print("Username corect")
parola = (input("parola: "))
assert expected_password == parola, 'Parola gresita'
print("Parola corecta")
suma = int(input("Introduceti suma dorita: "))
assert suma <= sold, 'Fonduri insuficiente'
print(f'Suma dorita de dvs este {suma}')
print("Plata efectuata")

# printam in consola un mesaj
print('Hello World!')
prima_variabila='string'
print(prima_variabila)
prima_variabila="string2"
print(prima_variabila)
prima_variabila=7
print(prima_variabila)
cifra='3'
print(type(cifra))
adunare = cifra + cifra
print(adunare)
cifra=int(cifra)
print(type(cifra))
adunare = cifra + cifra
print(adunare)
print('Print simplu')
var=5
string = "string"
print("Valoarea variabilei var este: " + str(var))
print(f"Valoarea variabilei var este: {var}")
a=1
assert a==1
print('A este 1 si am ajuns aici')
assert a==2, "A nu este egal cu 2"
print('nu mai ajung aici')

var = input('Introduceti variabila ')
print(type(var))
var = int(input('Introduceti variabila '))
print(type(var))

string = '22 de caractere'
print(len(string)) # lungimea sirului e de 15 caractere
print(string[3]) # care este caracterul a. 3-lea din sir = d
print(string.count('a')) # cate caractere "a" sunt in sirul meu
print(string[2:5]) # caracterele de la 2 la 4 (caracterul 5 nu se afiseaza)
print(string[-1]) # ultimul caracter
print(string.upper())

elevi = "Ana, Andrei, Maria"
print(elevi)
print(elevi.upper())
print(elevi.lower())
print(elevi[2:4])
print(elevi[-3])
print(elevi[::-1]) # afiseaza acelasi string, dar de la dr la st complet
print(len(elevi))

https://www.geeksforgeeks.org/, https://www.w3schools.com/,
https://www.freecodecamp.org/, https://stackoverflow.com/
https://roadmap.sh/