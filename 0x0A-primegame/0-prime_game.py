#!/usr/bin/python3
"""Prime Game. Maria and Ben are playing a game."""


def isWinner(x, nums):
    """
    Determining the winner of the Prime Game.
    
    Args:
        x (int): Number of rounds
        nums (list): List of n values for each round
    
    Returns:
        str: Name of the player who wins the most rounds
        None: If no winner
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    maria_winner = 0
    ben_winner = 0
    
    for n in nums:
        # Create set of numbers from 1 to n
        numbers = set(range(1, n + 1))
        current_player = 'Maria'  # Maria starts first
        
        while True:
            # Find available primes in the current set
            available_primes = [p for p in range(2, n + 1) if is_prime(p) and p in numbers]
            
            # If no primes available, current player loses
            if not available_primes:
                # Last player to make a move was opposite of current player
                if current_player == 'Maria':
                    ben_winner += 1
                else:
                    maria_winner += 1
                break
            
            # Choose the smallest prime
            chosen_prime = min(available_primes)
            
            # Remove chosen prime and its multiples from the set
            numbers = {num for num in numbers if num % chosen_prime != 0}
            
            # Switch players
            current_player = 'Ben' if current_player == 'Maria' else 'Maria'
    
    # Determine overall winner
    if maria_winner > ben_winner:
        return 'Maria'
    elif ben_winner > maria_winner:
        return 'Ben'
    return None