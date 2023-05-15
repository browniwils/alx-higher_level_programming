#!/usr/bin/python3

def multiple_returns(sentence):
    """ Return tuple with length of sentence and first character """
    if not sentence:
        return (0, None)
    slen = len(sentence)
    frist_char = sentence[0]
    return (slen, first_char)
