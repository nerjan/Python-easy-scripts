# nom to ilosci danych bankotow o nominalach: [500, 200, 100, 50, 20, 10, 5, 2, 1]
def kasa(kwota, nom):
    wydawanie = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    w_kasie = {500: nom[0], 200: nom[1], 100: nom[2], 50: nom[3], 20: nom[4], 10: nom[5], 5: nom[6], 2: nom[7], 1: nom[8]}
    for nominal, ilosc in w_kasie.items():
        while ilosc and nominal <= kwota:
            kwota -= nominal
            ilosc -= 1
            wydawanie[nominal] += 1
    print("zostało do wydania ", kwota)
    return wydawanie


print(kasa(5648, [3, 12, 30, 5, 12, 4, 8, 3, 16]))
