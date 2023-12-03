#!/usr/bin/python3
def multiple_returns(sentence):
    z = len(sentence)
    if z == 0:
        return (0, None)
    else:
        return (z, sentence[0])
