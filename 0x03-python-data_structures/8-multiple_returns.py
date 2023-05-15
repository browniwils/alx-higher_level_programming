#!/usr/bin/python3

def multiple_returns(sentence):
    """ Return tuple with length of sentence and first character """
    slen = len(sentence)
    if slen == 0:
        first_char = None
    else:
        frist_char = sentence[0]
    return (slen, first_char)
