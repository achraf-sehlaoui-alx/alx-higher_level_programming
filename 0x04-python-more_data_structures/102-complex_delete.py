#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
