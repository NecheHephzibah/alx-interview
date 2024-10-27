#!/usr/bin/python3
import sys


def print_statistics(status_codes, total_size):
    """
    Method to print HTTP access log statistics
    Args:
        status_codes: dictionary of HTTP status codes and their frequencies
        total_size: total size of processed files in bytes
    Returns:
        Nothing
    """
    print("File size: {}".format(total_size))
    for status_code, frequency in sorted(status_codes.items()):
        if frequency != 0:
            print("{}: {}".format(status_code, frequency))


total_size = 0
http_status = 0
line_count = 0
status_codes = {
    "200": 0,  # OK
    "301": 0,  # Moved Permanently
    "400": 0,  # Bad Request
    "401": 0,  # Unauthorized
    "403": 0,  # Forbidden
    "404": 0,  # Not Found
    "405": 0,  # Method Not Allowed
    "500": 0   # Internal Server Error
}

try:
    for line in sys.stdin:
        log_entries = line.split()
        log_entries = log_entries[::-1]  # Reverse to get status code and size

        if len(log_entries) > 2:
            line_count += 1
            if line_count <= 10:
                # File size is first after reversal
                total_size += int(log_entries[0])
                # Status code is second after reversal
                http_status = log_entries[1]

                if http_status in status_codes.keys():
                    status_codes[http_status] += 1

            if line_count == 10:
                print_statistics(status_codes, total_size)
                line_count = 0
finally:
    print_statistics(status_codes, total_size)
