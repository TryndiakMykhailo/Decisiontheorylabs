#!/usr/bin/python

import sys
import re
import string
from condorcet import condorcet
from borda import borda

def open_file():
    try:
        return open("tryndiaklab3_27.txt")
    except FileNotFoundError:
        print("Помилка - файл не існує")
        exit()



file = open_file()
lines = []
benefits = []

for line in file:
    if (not (line and not line.isspace())): continue
    row = re.split(';', re.sub('\n', '', line))
    new_benefits = re.split(',', row[1])
    for benefit in new_benefits:
        if benefit not in benefits: benefits.append(benefit)

    lines.append([row[0], new_benefits])

print("Зчитані дані з файлу:")
for line in lines: print(line)

print("\nМетод Кондорсе:")
condorcet_result = condorcet(lines, benefits)
print("Отже найкраще рішення:", ">".join(condorcet_result["places"]))

print("\nМетод Борда:")
borda_result = borda(lines, benefits)
print("Розрахунки:")
for note in borda_result['note'].keys():
    print(note, ": ", borda_result["note"][note], " = ", borda_result["sum"][note])
print("Отже накраще рішення:", ">".join(condorcet_result["places"]))
