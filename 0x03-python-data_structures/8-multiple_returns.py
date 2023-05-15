#!/usr/bin/python3

def multiple_returns(sentence):
    """ Return tuple with length of sentence and first character """
    if len(sentence) < 1:
        return (0, None)

    slen = len(sentence)
    first_char = sentence[0]
    return (slen, first_char)
