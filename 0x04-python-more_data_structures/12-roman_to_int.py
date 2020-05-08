#!/usr/bin/python3
def roman_to_int(roman_string):
    vals = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    newVALUE = 0
    if roman_string:
        for i in range(len(roman_string)):
            for key in vals:
                if roman_string[i] == vals[key]:
                    newVALUE = newVALUE + vals.get(value)
                return newVALUE
    else:
        return newVALUE
