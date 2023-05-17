#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    b_score = ["", 0]
    for key in a_dictionary:
        if a_dictionary[key] > b_score[1]:
            b_score = [key, a_dictionary[key]]

    return b_score[0]
