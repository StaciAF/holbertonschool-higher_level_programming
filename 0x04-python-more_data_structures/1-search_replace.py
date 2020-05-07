#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newLIST = []
    if my_list:
        for n, i in enumerate(my_list):
            if i == search:
                newLIST.append(replace)
            else:
                newLIST.append(i)
        return (newLIST)
