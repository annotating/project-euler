"""
PROBLEM 14

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), it 
is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

def main(n):
    t0= time.clock()
    maxLen = 0
    maxStartNum = 0
    lens = dict()
    for i in range(2,n):
        j = i
        len = 1
        while (j != 1):
            if (j%2 == 0):
                if (lens.has_key(j/2)):
                    len += lens[j/2]
                    j=1
                else:
                    len += 1
                    j = j/2
            else:
                if (lens.has_key(3*j+1)):
                    len += lens[3*j+1]
                    j=1
                else:
                    len += 1
                    j = 3*j+1
        lens[i] = len
#        print "START AT", i, "LENGTH IS", len
        if len > maxLen:
            maxLen = len
            maxStartNum = i
    print "MAX CHAIN STARTS AT:", maxStartNum,"WITH LENGTH:", maxLen
    t = time.clock() - t0
    print "TIME ELAPSED:", t
    
main(1000000)