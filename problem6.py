"""
PROBLEM 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 
3025 - 385 = 2640.

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
"""

"""
Doo-doo-doo...
"""

def main(N):
    sumSquare = 0
    squareSum = 0
    for i in range(1,N+1):
        sumSquare += i*i
    print "SUM OF SQUARES: ", sumSquare
    for i in range(1,N+1):
        squareSum += i
    squareSum = squareSum*squareSum
    print "SQUARE OF SUM: ", squareSum
    print "DIFFERENCE: ", squareSum-sumSquare
    
main(100)