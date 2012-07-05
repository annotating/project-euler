"""
PROBLEM 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math
def main():
#    num=999999
#    sqnm=math.floor(math.sqrt(num))
    sqnm = 1999999
    numset=set(range(2,math.trunc(sqnm)))
    maxim=max(numset)
    #generate primes
    x=2
    while x<maxim:
        if x in numset:
            y=2
            while x*y<math.floor(sqnm):
                if x*y in numset:
                    numset.remove(x*y)
                y=y+1
        x=x+1

    print numset
    sum = 0
    for p in numset:
        sum += p
    print sum
    
main()