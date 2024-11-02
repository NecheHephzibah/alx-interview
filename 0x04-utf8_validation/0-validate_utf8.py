#!/usr/bin/python3
"""
UTF8 Validation.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: List of integers where each integer represents 1 byte of data

    Returns:
        True if data is a valid UTF-8 encoding, else False
    """

    num_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        byte = num & 255

        if num_bytes == 0:
            mask = 1 << 7
            while byte & mask:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
