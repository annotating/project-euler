"""
2520 is the smallest number that can be divided by each 
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
"""

""" 
Take 1-20, and extract their prime factors. Keep a count of how
many times each prime factor appears for each number in the sequence
from 1-20. Take the max count for each prime, then multiply everything
together.

For example, 1-10:
1    2    3    4    5    6    7    8    9    10
               2^2       3x2       2^3  3^2  2x5

1    3     1        1        1     MAX COUNT
1    2^3  3    5    7    = 2520    TOTAL
"""

"FUCK, JUST DO IT BY HAND"

def divisible(testNum, N):
    for i in range(2,N):
        if (testNum%i != 0):
            return False
    return True

def main(N):
    testNum = N
    while(not(divisible(testNum, N))):
        print "testNUM: ", testNum
        testNum += N
    return testNum
    
main(20)        
    
    
    