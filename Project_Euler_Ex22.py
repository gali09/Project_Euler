from typing import List

import pandas as pd
import numpy as np
import string
"""
with open("p022_names.txt") as archivo:
    a = archivo.read()
archivo.close()

a = a.strip().split(',')
print('A', a)
print('A listado', a[1:-1])
b = [x[1:-1] for x in a]
# b = [x for x in a]

print('B', b)
lista: List[str] = sorted(b)
print('lista ordenada', lista)
"""
"""
df = pd.read_table("p022_names.txt", delimiter=",")
print("df",df)
lista = df.to_numpy().tolist()
print("lista",lista)
lista = sorted(lista)
print("lista ordenada", lista)
"""
"""
alfabeto = [chr(chNum) for chNum in range(ord('A'), ord('Z') + 1)]
print(alfabeto)

n = "AARON"


def sumaNombre(nombre):
    sumaletras = 0
    name = list(nombre)
    for i in name:
        for j in alfabeto:
            if i == j:
                sumaletras += alfabeto.index(j) + 1

    return sumaletras


prueba = sumaNombre(n)
snombre = []
print(lista[937])
print('suma nombre colin', sumaNombre(lista[937]), 'index', lista.index(lista[937]))
for i in lista:
    snombre.append(sumaNombre(i))

total = 0

print(snombre[937] * (937 + 1))
print('index colin', lista.index(lista[937 + 1]))

print(snombre)
print(len(snombre))
for i in range(1, len(snombre)):
    print(i, ' ', lista[i], 'suma nombre ', snombre[i])
    total += snombre[i] * (lista.index(lista[i]))

print(total, 'el total:')
"""
import time

start = time.time()

file = open("p022_names.txt")
names = file.readlines()
file.close()

listNames = names[0].split(",")

listNames.sort()
print(listNames)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetScore = []

for i in range(len(alphabet)):
    pair = []
    pair.append(alphabet[i])
    pair.append(i + 1)
    alphabetScore.append(pair)

print(alphabetScore)
totalScore = 0

for i in range(len(listNames)):
    indexScore = i + 1
    wordScore = 0
    for letter in listNames[i]:
        for score in range(len(alphabetScore)):
            if letter == alphabetScore[score][0]:
                wordScore += alphabetScore[score][1]

    totalScore = totalScore + (wordScore * indexScore)

print(totalScore)

elapsed = time.time() - start
print("Time elapsed:", elapsed, "sec.")