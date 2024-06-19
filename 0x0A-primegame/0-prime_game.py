#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Determine the winner of the game """
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0
    number = max(nums)
    primes = [True for _ in range(1, number + 1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for y in range(i + i, number + 1, i):
            primes[y - 1] = False

    for _, number in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: number])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
