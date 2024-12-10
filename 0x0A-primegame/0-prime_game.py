#!/usr/bin/python3
"""Prime Game. Maria and Ben are playing a game."""


def isWinner(x, nums):
    """function that checks for the winner"""
    if not nums or x < 1:
        return None
    max_number = max(nums)
    is_prime = [True for _ in range(max(max_number + 1, 2))]
    for prime_candidate in range(2, int(pow(max_number, 0.5)) + 1):
        if not is_prime[prime_candidate]:
            continue
        for multiple in range(prime_candidate * prime_candidate,
                              max_number + 1, prime_candidate):
            is_prime[multiple] = False
    is_prime[0] = is_prime[1] = False
    prime_count = 0
    for index in range(len(is_prime)):
        if is_prime[index]:
            prime_count += 1
        is_prime[index] = prime_count
    maria_wins = 0
    for round_number in nums:
        maria_wins += is_prime[round_number] % 2 == 1
    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
