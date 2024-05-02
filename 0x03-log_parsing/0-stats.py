#!/usr/bin/python3
""" Log parsing """

import sys

def parse_logs():
    """
    Function to parse logs
    """
    line_number = 0
    file_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            line_number += 1
            parts = line.split()
            try:
                file_size += int(parts[-1])
                if parts[-2] in status_codes:
                    status_codes[parts[-2]] += 1
            except (IndexError, ValueError):
                pass

            if line_number == 10:
                print_report(file_size, status_codes)
                line_number = 0

        print_report(file_size, status_codes)

    except KeyboardInterrupt:
        print_report(file_size, status_codes)
        raise

def print_report(file_size, status_codes):
    """
    Function to print report
    """
    print("File size: {}".format(file_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

if __name__ == '__main__':
    parse_logs()
