#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from pygame.locals import *
from game import KOM_POZIOM,KOM_PION,KOM_MARTWA,KOM_ZYWA,POLE_GRY,cell_size,window

def rysuj_populacje():
    """Rysowanie komórek (kwadratów) żywych"""
    for y in range(KOM_PION):
        for x in range(KOM_POZIOM):
            if POLE_GRY[x][y] == KOM_ZYWA:
                pygame.draw.circle(window, (77, 179, 113), (int(x * cell_size + cell_size/2), int(y * cell_size + cell_size/2)), int(cell_size/2), 0)
            elif POLE_GRY[x][y] == KOM_MARTWA:
                pygame.draw.circle(window, (105, 100, 100), (int(x * cell_size + cell_size/2), int(y * cell_size + cell_size/2)), int(cell_size/2), 0)
# zmienne sterujące wykorzystywane w pętli głównej