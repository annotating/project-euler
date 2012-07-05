"""
PROBLEM 9

A Pythagorean triplet is a set of three natural 
numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet 
for which a + b + c = 1000.
Find the product abc.
"""

"""
Generate triples using this formula:
Suppose that m and n are two positive integers, with m < n. 
Then n^2 - m^2, 2mn, and n^2 + m^2 is a Pythagorean triple.
This formula generates all the Pythagorean triples up to the
bound. 
"""

#N is the number in which a+b+c = N, where a, b, c, are
#a Pythagorean triple
def main(N):
    for n in range(2, N):
        for m in range(1, n):
            n1 = (n*n) - (m*m)
            n2 = 2*m*n
            n3 = (n*n) + (m*m)
            print n1,n2,n3,"=",n1+n2+n3
            if (n1+n2+n3 == N):
                print "SUCESS!" ,n1,n2,n3,"=",n1+n2+n3
                return
            
main(1000)       
            
    