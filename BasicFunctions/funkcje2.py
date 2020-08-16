def LiczbyPodzielnePrzezTrzyOrazSzesc(przedzial_poczatek, przedzial_koniec):
    suma_liczb=0
    liczby_podzielne_lista=[]
    for liczba in range(przedzial_poczatek, przedzial_koniec + 1):
        if liczba%3==0 and liczba%6==0:
            suma_liczb+=liczba
            liczby_podzielne_lista.append(liczba)
    print("Lista liczb podzielnych przez 3 i 6: ", liczby_podzielne_lista)
    print("Suma tych liczb: ", suma_liczb)


LiczbyPodzielnePrzezTrzyOrazSzesc(0, 30)
