#!/usr/bin/python3
"""
Module for calculating the perimeter of an island grid.
"""
def calculate_island_perimeter(terrain_grid):
    """
    Computes the perimeter of an island with no lakes.
    
    Args:
        terrain_grid (list): 2D grid representing land and water cells.
                              1 represents land, 0 represents water.
    
    Returns:
        int: Total perimeter of the island.
    """
    total_perimeter = 0
    
    if not isinstance(terrain_grid, list):
        return 0
    
    num_rows = len(terrain_grid)
    
    for row_index, current_row in enumerate(terrain_grid):
        num_columns = len(current_row)
        
        for col_index, cell_value in enumerate(current_row):
            if cell_value == 0:
                continue

            exposed_edges = (
                row_index == 0 or (len(terrain_grid[row_index - 1]) > col_index and terrain_grid[row_index - 1][col_index] == 0),
                col_index == num_columns - 1 or (num_columns > col_index + 1 and current_row[col_index + 1] == 0),
                row_index == num_rows - 1 or (len(terrain_grid[row_index + 1]) > col_index and terrain_grid[row_index + 1][col_index] == 0),
                col_index == 0 or current_row[col_index - 1] == 0
            )
            total_perimeter += sum(exposed_edges)
    
    return total_perimeter