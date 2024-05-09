#!/usr/bin/python3
""" def UTF-8 validation function """


def validUTF8(data):
    """ UTF-8 Validation """
    te = 1 << 7
    x = 1 << 6
    byte_c = 0
    for code_point in data:
        name = 1 << 7
        if byte_c == 0:
            while name & code_point:
                byte_c += 1
                name = name >> 1
            if byte_c == 0:
                continue
            if byte_c == 1 or byte_c > 4:
                return False
        else:
            if not (code_point & te and not (code_point & x)):
                return False
        byte_c -= 1
    return not byte_c
