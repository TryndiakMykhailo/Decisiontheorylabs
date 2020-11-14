#!/usr/bin/python

import sys
import re

def open_file():
    try:
        return open("Tryndiak_27.txt")
    except FileNotFoundError:
        print("Помилка - файл не існує")
        exit()

file = open_file()
lines = []
for line in file:
    if (not (line and not line.isspace())): continue

    row = re.split(',\s?', re.sub('\n', '', line))

    lines.append([int(element) for element in row])
print("Задана матриця:")
for i in range(len(lines)):
  print(lines[i])

###############################################################################
def laplace_criterion(matrix):
    sumOfRows = []
    for row in matrix:
        sumOfRows.append(sum(row)/len(row))
    maxValue = max(sumOfRows)
    print("Ділення суми кожного рядка на кількість стовпців", sumOfRows)
    print("Найбільший елемент:", maxValue)
    return sumOfRows.index(maxValue)
file = open_file()
lines = []
for line in file:
    if (not (line and not line.isspace())): continue
    row = re.split(',\s?', re.sub('\n', '', line))
    lines.append([int(element) for element in row])
print("\nКритерій Лапласа:")
indexByLaplace = laplace_criterion(lines)
print("Найкраща вибірка значень::", lines[indexByLaplace])

############################################################################
def walds_criterion(matrix):
    minOfRows = []
    for row in matrix:
        minOfRows.append(min(row))
    maxValue = max(minOfRows)
    print("Найменше значення з кожного рядка:", minOfRows)
    print("Найбільше серед найменших елементів:", maxValue)
    return minOfRows.index(maxValue)
file = open_file()
lines = []
for line in file:
    if (not (line and not line.isspace())): continue
    row = re.split(',\s?', re.sub('\n', '', line))
    lines.append([int(element) for element in row])
print("\nКритерій Вальда:")
indexByWald = walds_criterion(lines)
print("Найкраща вибірка значень:", lines[indexByWald])

########################################################################
def hurwitz_criterion(matrix, coefficient):
    minOfRows = []
    maxOfRows = []
    for row in matrix:
        minOfRows.append(min(row))
        maxOfRows.append(max(row))
    result = []
    for i in range(len(minOfRows)):
        result.append(coefficient * minOfRows[i] + (1 - coefficient) * maxOfRows[i])
    print("Коефіцієнт", coefficient)
    print("Найменший елемент з кожного рядка", minOfRows)
    print("Найбільший елемент з кожного рядка", maxOfRows)
    print("Пораховані значення:", result)
    return result.index(max(result))
file = open_file()
lines = []
for line in file:
    if (not (line and not line.isspace())): continue
    row = re.split(',\s?', re.sub('\n', '', line))
    lines.append([int(element) for element in row])
print("\nКритерій Гурвіца:")
indexByHurwitz = hurwitz_criterion(lines, 0.6)
print("Найкраща вибірка значень:", lines[indexByHurwitz])

#################################################################################
def bayes_laplace_criterion(matrix, coefficients):
    result = [0 for x in range(len(matrix))] 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i] += coefficients[j] * matrix[i][j];
    print("Коефіцієнт", coefficients)
    print("Пораховані значення:", result)
    return result.index(max(result))
file = open_file()
lines = []
for line in file:
    if (not (line and not line.isspace())): continue
    row = re.split(',\s?', re.sub('\n', '', line))
    lines.append([int(element) for element in row])
print("\nКритерій Байеса-Лапласа:")
indexByBayesLaplace = bayes_laplace_criterion(lines, [0.3, 0.4, 0.45])
print("Найкраща вибірка значень:", lines[indexByBayesLaplace])


