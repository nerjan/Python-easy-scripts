import math


# metoda obliczajaca wartosc wielomianu metoda hornera w punkcie x
def horner(wielomian, x):
    stopien = len(wielomian)  # stopien wielomianu + 1
    result = wielomian[0]
    for i in range(1, stopien):
        result = result * x + wielomian[i]
    return result


# obliczenie pochodnej wielomianu
def pochodna(wielomian):
    stopien = len(wielomian) - 1  # stopien wielomianu
    return [(stopien - i) * wielomian[i] for i in range(0, stopien)]


# znajdz xn+1 wedlug algorytmu newtona
def newtonNext(wielomian, x0=0):
    poch = horner(pochodna(wielomian), x0)
    # jezeli pochodna jest rowna 0, sprobuj inny pierwiastek
    if poch == 0:
        x0 += 1
    return x0 - horner(wielomian, x0) / horner(pochodna(wielomian), x0)


# znajdywanie pierwiastka metoda hornera-newtona, wykonywane tak dlugo az xn+1 w przyblizeniu rowne xn
def findRoot(wielomian, x):
    previous = newtonNext(wielomian, x)  # wartosc xn
    next = newtonNext(wielomian, previous)  # nastepna wartosc xn+1
    sub = abs(abs(previous) - abs(next))  # wartosc bezwgledna z roznicy xn i xn+1
    if sub < 0.000000001:  # jesli roznica jest mala, jest to w przyblizeniu szukany pierwiastek
        return next
    else:
        return findRoot(wielomian, next)  # jesli sub jest niewystarczajaco male, powtorz


# funkcja przeprowadzajaca dzielenie wielomianu szesciennego przez dwumian metoda hornera
def dzielenieWielomianuSzesciennego(wielomian, pierwiastek):
    return [round(wielomian[0], 2), round(wielomian[1] + pierwiastek * wielomian[0], 2),
            round(wielomian[2] + pierwiastek * (wielomian[1] + pierwiastek * wielomian[0]), 2)]


# funkcja przeprowadzajaca dzielenie wielomianu kwadratowego przez dwumian, metoda hornera
def dzielenieWielomianuKwadratowego(wielomian, pierwiastek):
    return [round(wielomian[0], 2), round((wielomian[1] + pierwiastek * wielomian[0]), 2)]


# glowna funkcja przeprowadzajaca poszukiwanie pierwiastkow rownania
def roots(wielomian):
    result = []
    try:
        first = findRoot(wielomian, 0)  # pierwszy pierwiastek rownania szesciennego
        result.append(round(first, 2))
    except:
        return result
    try:
        w2 = dzielenieWielomianuSzesciennego(wielomian, first)
        # jesli nie ma bledu, to znaczy istnieja inne pierwiastki (algorytm jest w stanie je odnalezc przy odpowiedniej
        # przecyzji)
        second = findRoot(w2, first)
        result.append(round(second, 2))
    except (RecursionError, ZeroDivisionError) as e:  # blad nieskonczonego odwolywania sie do funkcji oraz dzielenia przez zero
        return result
    try:
        w3 = dzielenieWielomianuKwadratowego(w2, second)
        third = findRoot(w3, second)
        result.append(round(third, 2))
    except (RecursionError, ZeroDivisionError) as e:
        return result
    return result
