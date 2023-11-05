#!/usr/bin/python3
def multiple_returns(sentence):
    my_len = len(sentence)
    return (0, None) if sentence == '' else (my_len, sentence[0])
