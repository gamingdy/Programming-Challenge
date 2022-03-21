"""
author: gamingdy

You must call the find_factor function, with a number between 2 and infinity as argument 
"""


def isPrime(number):
    for a in range(2, number):
        if not number % a:
            return False
    return True


def find_factor(number: int):
    for i in range(2, number + 1):
        if not number % i:
            if isPrime(i):
                highest_prime_factor = i

    return highest_prime_factor
