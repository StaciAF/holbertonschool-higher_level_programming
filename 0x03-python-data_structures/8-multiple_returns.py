#!/bin/usr/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        length = 0
        firstCHAR = None
    else:
        length = len(sentence)
        firstCHAR = sentence[:1]
        newTUPLE = (length, firstCHAR)
    return (newTUPLE)
