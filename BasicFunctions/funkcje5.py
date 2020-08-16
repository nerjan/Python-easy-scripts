def Mnozenie():
    wynik=0
    liczba_1 = int(input("Liczba 1 "))
    liczba_2 = int(input("Liczba 2 "))
    liczba_3 = int(input("Liczba 3 "))
    for l1 in range(liczba_1):
        for l2 in range(liczba_2):
            wynik+=liczba_3
    print(wynik)
Mnozenie()