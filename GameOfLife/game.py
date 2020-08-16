#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from pygame.locals import *
from widok import rysuj_populacje
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('Hello', 'Bring cells to life by clicking on them with LMB. Use RMB to kill them. Press Enter to start the simulation or to stop it.')

pygame.init()

window_width = 1400
window_height = 700

# inicjacja okna gry
window = pygame.display.set_mode((window_width, window_height), 0, 32)
# tytuł okna gry
pygame.display.set_caption('GAME OF LIFE')

# rozmiar komórki
cell_size = 20
# ilość komórek w poziomie i pionie
KOM_POZIOM = int(window_width / cell_size)
KOM_PION = int(window_height / cell_size)

# wartości oznaczające komórki "martwe" i "żywe"
KOM_MARTWA = 0
KOM_ZYWA = 1
color_alive = (77, 179, 113)
color_dead = (105, 100, 100)

POLE_GRY = [KOM_MARTWA] * KOM_POZIOM
# rozszerzamy listę o listy zagnieżdżone, otrzymujemy więc listę dwuwymiarową
for i in range(KOM_POZIOM):
    POLE_GRY[i] = [KOM_MARTWA] * KOM_PION
# przygotowanie następnej generacji komórek, czyli zaktualizowanego POLA_GRY
def przygotuj_populacje(polegry):
    # na początku tworzymy 2-wymiarową listę wypełnioną zerami
    nast_gen = [KOM_MARTWA] * KOM_POZIOM
    for i in range(KOM_POZIOM):
        nast_gen[i] = [KOM_MARTWA] * KOM_PION

    # iterujemy po wszystkich komórkach
    for y in range(KOM_PION):
        for x in range(KOM_POZIOM):

            # zlicz populację (żywych komórek) wokół komórki
            populacja = 0
            # wiersz 1

            if polegry[(x - 1 + KOM_POZIOM)%KOM_POZIOM][(y - 1+KOM_PION)%KOM_PION] == KOM_ZYWA:
                populacja += 1

            if polegry[x][(y - 1 + KOM_PION)%KOM_PION] == KOM_ZYWA:
                populacja += 1

            if polegry[(x + 1+KOM_POZIOM)%KOM_POZIOM][(y - 1 + KOM_PION)%KOM_PION] == KOM_ZYWA:
                populacja += 1

        # wiersz 2

            if polegry[(x - 1 + KOM_POZIOM)%KOM_POZIOM][y] == KOM_ZYWA:
                populacja += 1

            if polegry[(x + 1 + KOM_POZIOM)%KOM_POZIOM][y] == KOM_ZYWA:
                populacja += 1

            # wiersz 3

            if polegry[(x - 1 + KOM_POZIOM)%KOM_POZIOM][(y + 1 + KOM_PION)%KOM_PION] == KOM_ZYWA:
                populacja += 1


            if polegry[x][(y + 1 + KOM_PION)%KOM_PION] == KOM_ZYWA:
                populacja += 1

            if polegry[(x + 1 + KOM_POZIOM)%KOM_POZIOM][(y + 1 + KOM_PION)%KOM_PION] == KOM_ZYWA:
                populacja += 1

            # "niedoludnienie" lub przeludnienie = śmierć komórki
            if polegry[x][y] == KOM_ZYWA and (populacja < 2 or populacja > 3):
                nast_gen[x][y] = KOM_MARTWA
            # życie trwa
            elif polegry[x][y] == KOM_ZYWA \
                    and (populacja == 3 or populacja == 2):
                nast_gen[x][y] = KOM_ZYWA
            # nowe życie
            elif polegry[x][y] == KOM_MARTWA and populacja == 3:
                nast_gen[x][y] = KOM_ZYWA

    # zwróć nowe polegry z następną generacją komórek
    return nast_gen


zycie_trwa = False
przycisk_wdol = False

# pętla główna programu
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_RETURN:
            if zycie_trwa:
                zycie_trwa = False
            else:
                zycie_trwa = True

        if zycie_trwa is False:
            if event.type == MOUSEBUTTONDOWN:
                przycisk_wdol = True
                przycisk_typ = event.button

            if event.type == MOUSEBUTTONUP:
                przycisk_wdol = False

            if przycisk_wdol:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x = int(mouse_x / cell_size)
                mouse_y = int(mouse_y / cell_size)
                # lewy przycisk myszy ożywia
                if przycisk_typ == 1:
                    POLE_GRY[mouse_x][mouse_y] = KOM_ZYWA
                # prawy przycisk myszy uśmierca
                if przycisk_typ == 3:
                    POLE_GRY[mouse_x][mouse_y] = KOM_MARTWA

    if zycie_trwa is True:
        POLE_GRY = przygotuj_populacje(POLE_GRY)

    window.fill((0, 0, 0))  # ustaw kolor okna gry
    widok.rysuj_populacje()
    pygame.display.update()
    pygame.time.delay(100)
