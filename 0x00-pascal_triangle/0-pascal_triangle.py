#!/usr/bin/python3
"""
Implementing Pascal’s Triangle in Python
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle with the given number of rows.

    Args:
        n (int): The number of rows for Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle as a list of lists of integers.
    """
    p_triangle = []

    if n > 0:
        for row in range(1, n + 1):
            current_row = []
            current_value = 1
            
            for col in range(1, row + 1):
                current_row.append(current_value)
                current_value = current_value * (row - col) // col
            
            p_triangle.append(current_row)
    
    return p_triangle
