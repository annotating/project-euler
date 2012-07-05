"""
PROBLEM 12

The sequence of triangle numbers is generated 
by adding the natural numbers. So the 7th triangle 
number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number 
to have over five divisors.

What is the value of the first triangle number to 
have over five hundred divisors?
"""

""" 
Generate triangle numbers, get factors, count length.
SHOULD REWRITE FACTORS METHOD FOR BETTER EFFICIENCY LATER.

NEW APPROACH: Get list of prime numbers. Multiply them together
in all possible combinations increasing the list of primes until
you have 500 factors. Find lcd of prime list.

EDIT: YOU DUMMY, WHY DID YOU MAKE IT SO COMPLICATED
"""

import math
import time


def factors(N):
    factors = []
    sqrtN = int(math.ceil(math.sqrt(N)))
    for i in range(1,sqrtN):
        if (N%i == 0):
            factors.append(i)
            factors.append(N/i)
    factors.sort()
    l = len(factors)
    print N, l, factors
    return l

def main(numFact):
    t0= time.clock()
    n0 = 0
    n1 =  1
    next = n0+n1
    while ((factors(next)) < numFact):
        n0 = next
        n1 = n1+1
        next = n0+n1
    print "SUCCESS!", next
    t = time.clock() - t0
    print "TIME ELAPSED:", t

main(500)