#!/usr/bin/python3
"""Solves the lock boxes puzzle using a depth-first search approach"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): Each box may contain keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = set([0])  # The first box (index 0) is initially unlocked
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if isinstance(key, int) and 0 <= key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n

# The following lines are not necessary for the solution, but can be used for testing
if __name__ == "__main__":
    # Test cases
    print(canUnlockAll([[1], [2], [3], [4], []]))
    print(canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]))
    print(canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]))
