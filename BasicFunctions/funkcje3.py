def PoliczPlaceNetto():
    placa_brutto = int(input("Twoje zarobki brutto wynosza: "))
    if 1000<=placa_brutto and placa_brutto<=3600:
        placa_netto=placa_brutto-0.24*placa_brutto
    elif placa_brutto>3600:
        placa_netto=placa_brutto-placa_brutto*0.29
    else:
        placa_netto=placa_brutto
    print("Placa netto wynosi: ", placa_netto)


PoliczPlaceNetto()
