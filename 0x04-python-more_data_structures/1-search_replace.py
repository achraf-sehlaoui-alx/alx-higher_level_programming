#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mew_list = my_list.copy()
    for i in mew_list:
        if i == search:
            idx = mew_list.index(i)
            mew_list.remove(i)
            mew_list.insert(idx, replace)
    return mew_list
