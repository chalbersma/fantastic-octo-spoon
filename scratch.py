#!/usr/bin/env python3

import math

import sympy
import colors

print(colors.red("test"))
print(colors.blue("test"))

lines = [[1]]
integer = 1
for current_line in range (1, 15):

    print(current_line)

    last_line = [int(x) for x in lines[current_line-1]]

    needed_numbers = len(last_line) + 1
    midline = math.floor(needed_numbers / 2)

    print("index midline : {}".format(midline))
    print("Needed Numbers : {}".format(needed_numbers))

    iout = midline
    iin = midline -1
    onout = True

    newline = [None] * needed_numbers

    for y in range(last_line[0]+1, last_line[0]+needed_numbers+1):

        if onout is True:

            newline[iout] = str(y)
            iout += 1
            onout = False
        else:
            # onin
            if sympy.isprime(y):
                ystring = colors.red(str(y))
            else:
                ystring = str(y)

            newline[iin] = ystring
            iin -= 1
            onout = True

    lines.append(newline)


for ln in lines:
    print(ln)

