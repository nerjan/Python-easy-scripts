def CzyLiczbaJestPodzielnaPrzezTrzyOrazCztery(liczba):
    print("Liczba ", liczba)
    if liczba%3==0:
        print("jest  podzielna przez 3")
    if liczba%4==0:
        print("jest podzielna przez 4")
    if liczba%3==0 and liczba%4==0:
        print("podzielna przez 3 i 4")
    elif liczba%3!=0 and liczba%4!=0:
        print("nie jest podzielna przez 3 i 4")

powtorz = int(input("Ile razy chcesz wykonać zadanie? "))
for x in range(1, powtorz+1):
    CzyLiczbaJestPodzielnaPrzezTrzyOrazCztery(x)
