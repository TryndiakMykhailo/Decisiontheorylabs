#!/usr/bin/python

import sys
import re
import string

def open_file():
    try:
        return [open("tryndiaklab2_27.txt"), 5]
    except FileNotFoundError:
        print("Помилка - файл не існує")
        exit()


[file, years] = open_file()
lines = []
benefits = []

for line in file:
    if (not (line and not line.isspace()) or len(lines) >= 3): continue

    lines.append(re.split(';', re.sub('\n', '', line)))
print("Зчитані з файлу значення:")
A = { 'M1': float(lines[0][0]), 'D1': float(lines[0][1]), 'P1': float(lines[0][2]), 'D2': float(lines[0][3]), 'P2': float(lines[0][4]) }
B = { 'M2': float(lines[1][0]), 'D1': float(lines[1][1]), 'P1': float(lines[1][2]), 'D2': float(lines[1][3]), 'P2': float(lines[1][4]) }
C = { 'P3': float(lines[2][0]), 'P4': float(lines[2][1]), 'P1': float(lines[2][2]), 'P2': float(lines[2][3]) }

print("A:", A)
print("Б:", B)
print("В:", C)

print("\nРозрахунок значення вузла А:")
EVM_A = A['P1'] * A['D1'] * years - A['P2'] * A['D2'] * years - A['M1'];
print("Вузол(A) =", A['P1'], '*', A['D1'], '*', years, '-', A['P2'], '*', A['D2'], '*', years, '-', A['M1'], '=', EVM_A)

print("\nРозрахунок значення вузла Б:")
EVM_B = B['P1'] * B['D1'] * years - B['P2'] * B['D2'] * years - B['M2'];
print("Вузол(Б) =", B['P1'], '*', B['D1'], '*', years, '-', B['P2'], '*', B['D2'], '*', years, '-', B['M2'], '=', EVM_B)

print("\nРозрахунок значення вузла В:")
EVM_A1 = C['P1'] * A['D1'] * (years - 1) - C['P2'] * A['D2'] * (years - 1) - A['M1']
EVM_B1 = C['P1'] * B['D1'] * (years - 1) - C['P2'] * B['D2'] * (years - 1) - B['M2']
print("Вузол(A1) =", C['P1'], '*', A['D1'], '*', years - 1, '-', C['P2'], '*', A['D2'], '*', years - 1, '-', A['M1'], '=', EVM_A1)
print("Вузол(Б1) =", C['P1'], '*', B['D1'], '*', years - 1, '-', C['P2'], '*', B['D2'], '*', years - 1, '-', B['M2'], '=', EVM_B1)

EVM_MAX = max([EVM_A1, EVM_B1])
print("Найкраще значення -", EVM_MAX)

EVM_C = C['P3'] * EVM_MAX - C['P4'] * 0
print("Отже, Вузол(В) =", C['P3'], '*', EVM_MAX, '-', C['P4'], '*', 0, '=', EVM_C)

letters = ['A', 'Б', 'В']
bestSolution = max([EVM_A, EVM_B, EVM_C])

print("\nНайкраще рішення серед відповідей: { A:", EVM_A, ',', "Б:", EVM_B, ',', "В:", EVM_C, "} ----", letters[[EVM_A, EVM_B, EVM_C].index(bestSolution)], '{', bestSolution, '}')

