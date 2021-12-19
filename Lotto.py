import random

print("""Witaj w grze Duży Lotek.
Wybierz 6 liczb od 1 do 49\n""")
typy = set()

liczba_1 = int(input("Wprowadź 1 z 6 liczb: "))
typy.add(liczba_1)
liczba_2 = int(input("Wprowadź 2 z 6 liczb: "))
typy.add(liczba_2)
liczba_3 = int(input("Wprowadź 3 z 6 liczb: "))
typy.add(liczba_3)
liczba_4 = int(input("Wprowadź 4 z 6 liczb: "))
typy.add(liczba_4)
liczba_5 = int(input("Wprowadź 5 z 6 liczb: "))
typy.add(liczba_5)
liczba_6 = int(input("Wprowadź 6 z 6 liczb: "))
typy.add(liczba_6)

lista = [i for i in range(1, 50)]
random.shuffle(lista)
x = lista[0:6]
y = set(x)
print(f"Wybrane liczby to: {typy}\n")
print(f"Wylosowane liczby to: {y}\n")
trafione = y & typy

if trafione:
    print(f"Trafione liczby to: {trafione}")
else:
    print("Tym razem nie trafiłeś żadnej liczby")


