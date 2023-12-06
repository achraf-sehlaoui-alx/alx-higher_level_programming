#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > a:
            a = a_dictionary[key]
            key_max = key
    return key_max
