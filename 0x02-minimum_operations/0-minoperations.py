#!/usr/bin/python3
"""
Module for calculating minimum operations needed to achieve exactly n H
characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations to get exactly target_chars
    H characters.
    """
    if n <= 1:
        return 0

    total_operations = 0
    current_divisor = 2

    while n > 1:
        while n % current_divisor == 0:
            # Add current_divisor to total operations
            total_operations += current_divisor
            # Divide target_chars by current_divisor
            n //= current_divisor
        # Move to the next divisor
        current_divisor += 1

    return total_operations
