def PoliczPlaceNetto():
    placa_brutto = int(input("Placa brutto: "))
    PP = int(input("Procent podatku pracy: "))
    UZ = int(input("Procent ubezpieczenia zdrowotnego: "))
    PPK = int(input("Procent PPK: "))
    placa_netto = placa_brutto-placa_brutto*((PP + PPK + UZ)/100)
    print("Placa netto wynosi: ", placa_netto)
PoliczPlaceNetto()