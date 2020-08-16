import random
class Szachownica():

    def __init__(self, n):
        self.n = n
        # x to lista kolumn, gdzie x[i] to numer wierwsza
        self.tabela = n * [None]
        # lista wierszy - szachowanie w poziomie - jeśli True, to znaczy że nie ma szacha
        self.wolne_wiersze = n * [True]

        # lista przekątnych \ - jest ich 2n-1 - True oznacza brak szacha
        self.wolne_przekatneP = (2*n-1) * [True]

        # lista przekątnych / Różnica wiersz-kolumna od (-N+1) do (N-1). 
        self.wolne_przekatneL = (2*n-1) * [True]
        self.lista_rozwiazan = []

    def dodaj_hetmana(self, col):
        for row in range(self.n):
            if self.sprawdz(row, col):
                self.zapisz(row, col)
                if col < (self.n-1):
                    self.dodaj_hetmana(col+1)
                else:
                    # self.rysuj_szachownice()
                    self.lista_rozwiazan.append([el for el in self.tabela])
                self.wymaz(row, col)

    def sprawdz(self, row, col):
        return self.wolne_wiersze[row] and self.wolne_przekatneP[row+col] and self.wolne_przekatneL[row-col]

    def zapisz(self, row, col):
        self.tabela[col] = row
        self.wolne_wiersze[row] = False
        self.wolne_przekatneP[row+col] = False
        self.wolne_przekatneL[row-col] = False


    def wymaz(self, row, col):
        self.wolne_wiersze[row] = True
        self.wolne_przekatneP[row+col] = True
        self.wolne_przekatneL[row-col] = True

    def rysuj_szachownice(self):
        self.dodaj_hetmana(0)
        pick = self.lista_rozwiazan[random.randint(0, len(self.lista_rozwiazan)-1)]
        for row in range(self.n):
            for col in range(self.n):
                if pick[col] == row:
                    print ("H", end=" ")
                else:
                    print ("0", end =" ")
            print()


n = int(input("Podaj dlugosc boku szachownicy"))

hetman = Szachownica(n)
#rysowanie szachownicy o wymierach nxn
hetman.rysuj_szachownice()
