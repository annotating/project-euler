"""
PROBLEM 1

If we list all the natural numbers below 10 that are multiples of 
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
To generate the sum of multiples of 3 and 5 for n terms, we use the following
formulas:

For multiples of 3:
((n)(3n+3)) / 2

For multiples of 5:
((n)(5n+5)) / 2

We then set n = 1000, and add the two sums up to get our answer, remembering
to subtract any duplicates.

"""

def main():
    N = 999
    i = N/3
    j = N/5
    k = N/15
    sum = ((i)*(3*i+3))/2 + ((j)*(5*j+5))/2 - ((k)*(15*k+15))/2 
    print "MAX TERM: ", N
    print "SUM OF MULTIPLES OF 3 AND 5: ", sum
    
main()