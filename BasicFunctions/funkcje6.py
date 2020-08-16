from math import pi, sqrt
def PoliczObwodTrojkata():
    obwod_trojkata = 0
    for bok in range(1, 4):
        obwod_trojkata+=float(input("Podaj "+str(bok)+" bok trojkata "))
    return obwod_trojkata
def PoliczObwodOkregu(r):
    return 2*pi*r
def PoliczPoleKola(r):
    return pi*r**2
def ZrobWszystko():
    print("Pierwszy trojkat: ")
    obwod_1=PoliczObwodTrojkata()
    print("Drugi trojkat: ")
    obwod_2=PoliczObwodTrojkata()
    print("Trzeci trojkat: ")
    obwod_3=PoliczObwodTrojkata()
    bok_kwadratu = max(obwod_1, obwod_2, obwod_3)
    print("Bok kwadratu: ", bok_kwadratu)
    pole_kwadratu = bok_kwadratu**2
    przekatna_kwadratu = sqrt(2)*bok_kwadratu
    print("Przekatna kwadratu: ", przekatna_kwadratu)
    if pole_kwadratu<150:
        print("Pole ponizej 150!")
    elif pole_kwadratu>150:
        print("Pole powyzej 150!")
    print("Obwod okregu wpisanego w kwadrat: ", PoliczObwodOkregu(bok_kwadratu/2))
    print("Pole kola wpisanego w kwadrat: ", PoliczPoleKola(bok_kwadratu/2))
    print("Obwod okregu opisanego na kwadracie", PoliczObwodOkregu(przekatna_kwadratu/2))
    print("Pole kola opisanego na kwadracie: ", PoliczPoleKola(przekatna_kwadratu/2))
ZrobWszystko()
