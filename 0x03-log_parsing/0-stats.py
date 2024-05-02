#!/usr/bin/python3
"""
Log parsing
"""


def parseLogs():
    """
    parseLogs function
    """
    stdin = __import__('sys').stdin
    num = 0
    size = 0
    status_c = {}
    status = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            num += 1
            line = line.split()
            try:
                size += int(line[-1])
                if line[-2] in status:
                    try:
                        status_c[line[-2]] += 1
                    except KeyError:
                        status_c[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if num == 10:
                report(size, status_c)
                num = 0
        report(size, status_c)
    except KeyboardInterrupt as e:
        report(size, status_c)
        raise


def report(size, status_c):
    """
    report function
    """
    print("File size: {}".format(size))
    for key, value in sorted(status_c.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    parseLogs()
