"""
PROBLEM 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
We start at sqrt(N), since that is the largest factor N can have.
Decreasing sqrt(N) by 1 each time, we will eventually find the largest
factor of N, which we can recurse over to find the other factors of N.
"""

import math

def main(N):
    factors = [1.0]
    helper(N, factors)
    factors.sort()
    primes = factors[1:]
    # Remove composites from list of factors
    for p1 in primes:
        for p2 in primes:
            if (p1%p2 == 0 and p1 != p2):
                primes.remove(p1)
            elif (p2%p1 == 0 and p1 != p2):
                primes.remove(p2)
    print "N: ", N
    print "FACTORS: ", factors        
    print "PRIME FACTORS: ", primes
    print "MAX PRIME FACTOR: ", max(primes)

def helper(N, factors):
        i = math.ceil(math.sqrt(N))
        # Find a factor of N
        while (N%i != 0):
            i -= 1
        # Add factor to list
        if (i not in factors):
            factors.append(i)
        if (N/i not in factors):
            factors.append(N/i)
        # Recurse over factor to obtain rest of factors
        if (i != N):    # If i or N/i == N, then we infinite loop    
            helper(i, factors)
        if (N/i != N):
            helper(N/i, factors)

main(975579)