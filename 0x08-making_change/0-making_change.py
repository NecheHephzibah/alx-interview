#!/usr/bin/python3
"""
Calculates the minimum number of coins needed to make up a
specific total amount.
"""
def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total amount.
    
    Args:
        coins (list): Available coin denominations
        total (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed
             0 if total is 0 or less
             -1 if total cannot be met by any combination of coins
    """
    # Validate input
    if not coins or coins is None:
        return -1
    
    # Handle base cases
    if total <= 0:
        return 0
    
    # Track number of coins used
    change = 0
    
    # Sort coins in descending order to use largest coins first
    coins = sorted(coins)[::-1]

    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1

        if total == 0:
            return change
    return -1