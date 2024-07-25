import random

###### Definicje klas

lista_bestii = ["Mysz", "Kot", "Smok"]

###### Główne Funkcje i Pętle

def gra():
    czynnik_losowy = random.randint(0,2)
    wybrana_bestia = lista_bestii[czynnik_losowy]

    print(f"Na twojej drodze staje {wybrana_bestia}!")
    print("Giniesz.")

while True:
    operacja = input('Aby zacząć, wpisz START. Aby zakończyć, wpisz END')
    if operacja == "END":
        break
    elif operacja not in ["START", "END"]:
        print("Niepoprawna operacja")
        continue
    else:
        print("test")
        gra()