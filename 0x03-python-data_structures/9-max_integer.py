#!/usr/bin/python3
def max_integer(my_list=[]):
    newMAX = my_list[0]
    if my_list:
        for i in my_list:
            if newMAX < i:
                newMAX = i
        return (newMAX)
