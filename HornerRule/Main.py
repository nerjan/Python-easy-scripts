import tkinter
from tkinter import *  # importowanie wszystkiego z biblioteki tkinter
import sys
import horner


# metoda wywoływana w odpowiedzi na guzik 'zakoncz' zamykajaca program
def koniec():
    sys.exit()


def oblicz():
    try:
        # pobierz współczynniki wielomianów podane przez użytkownika
        wielomian = [int(x3Entry.get()), int(x2Entry.get()), int(x1Entry.get()), int(x0Entry.get())]
        wynik = horner.roots(wielomian)
        napis = ""
        for p in wynik:
            napis += "   " + str(p)
        # przypisz wyliczone wspolczynniki do zmiennej wynikText, ktorej uzywa label wynikLabel
        wynikText.set(napis)
    except ValueError:
        wynikText.set("Niepoprawne wartości współczynników")


main = tkinter.Tk()  # tworzenie okna głównego
main.title("PIERWIASTKI ROWNANIA SZEŚCIENNEGO")  # tytul okna
main.geometry('500x360+400+120')  # wymiary okna i polozenie
napis = Label(main, text="Obliczanie pierwiastków równania sześciennego", font=("Times New Roman", 15), bg="#CF0B4E")

# tworzenie odpowiednich label oraz entry do pobierania wspolczynnikow wielomianu od uzytkownika
x3Entry = Entry(main, bd=1)
x3Entry.place(x=10, y=50, width=50, height=30)
x3Label = Label(main, text="x^3 + ", font=("Times New Roman", 15))
x3Label.place(x=60, y=50)

x2Entry = Entry(main, bd=1)
x2Entry.place(x=110, y=50, width=50, height=30)
x2Label = Label(main, text="x^2 + ", font=("Times New Roman", 15))
x2Label.place(x=160, y=50)

x1Entry = Entry(main, bd=1)
x1Entry.place(x=210, y=50, width=50, height=30)
x1Label = Label(main, text="x + ", font=("Times New Roman", 15))
x1Label.place(x=260, y=50)

x0Entry = Entry(main, bd=1)
x0Entry.place(x=300, y=50, width=50, height=30)
# przycisk, po kliknieciu ktorego wywolywana jest metoda oblicz
obliczButton = Button(main, text="Oblicz pierwiastki", command=oblicz)
obliczButton.place(x=10, y=100)
# label 'Pierwiastki: '
pierwiastkiLabel = Label(main, text="Pierwiastki: ", font=("Times New Roman", 15))
pierwiastkiLabel.place(x=10, y=150)
# zmienna wynikText przechowujaca wynikowe pierwiastki
wynikText = StringVar()
wynikLabel = Label(main, textvariable=wynikText, font=("Times New Roman", 15))
wynikLabel.place(x=10, y=200)
# gorna krawedz okna
topFrame = Frame(main)
topFrame.pack()
# dolna krawedz okna
bottomFrame = Frame(main)
# side rozmieszczenie w oknie
bottomFrame.pack(side=BOTTOM)
zakoncz = Button(main, text="Zakończ", command=koniec)

napis.pack(fill=X)
zakoncz.pack(side=BOTTOM)

main.mainloop()
