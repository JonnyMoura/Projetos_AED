# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:46:05 2022

@author: joanm
"""

from random import randint


def criarRaster(f, linhas: int, colunas: int):
    random = 0
    f.write(f"RASTER {linhas} {colunas}\n")
    for j in range(linhas):
        for k in range(colunas):
            random = randint(0, linhas * colunas)
            if k == colunas - 1:

                f.write(f"{random}\n")
            else:
                f.write(f"{random} ")

ficheiro = open("teste1000000.txt", "w")

total = 1000000
n = 2
m = int(total / n)
criarRaster(ficheiro, n, m)
ficheiro.write(f"PERCENTIL {total}\n")
for j in range(total):
   random = randint(0, total)
   if j == total - 1:
       ficheiro.write(f"{random}\n")
   else:
       ficheiro.write(f"{random} ")
ficheiro.close()