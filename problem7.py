"""
PROBLEM 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, 
and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

"""
Borrow Andrew's prime number generator, and initialize a variable
to keep count.
"""

import math
def main():
    num=999999
#    sqnm=math.floor(math.sqrt(num))
    sqnm = 999999
    numset=range(2,math.trunc(sqnm))
    numset=set(numset)
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
        
    #Find 10001th prime
    count = 0;
    print count
    for i in numset:
        count += 1;
        print i
        if (count==10001):
            print i, "<- OMG!"
            break
                
main()

