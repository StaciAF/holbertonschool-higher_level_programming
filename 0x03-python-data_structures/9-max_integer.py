#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    newMAX = my_list[0]
    if my_list:
        for i in my_list:
            if i > newMAX:
                newMAX = i
        return (newMAX)
