#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newLIST = []
    if my_list:
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                newLIST.append(True)
            else:
                newLIST.append(False)
        return(newLIST)
