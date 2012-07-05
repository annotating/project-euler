"""
A palindromic number reads the same both ways. The largest 
palindrome made from the product of two 2-digit numbers is 
9009 = 91 * 99.

Find the largest palindrome made from the product of two 
3-digit numbers.
"""

""" 
Maybe reverse engineer? Start with the largest possible n-digit
number. Subtract 1 from it until we find a palindrome, and then
check if both if it's factors have lenght n.
"""

import math
    
def isPalindrome(N):
    nString = str(N)
    # nString[::-1] reverses the string
    if nString == nString[::-1]:
        return True
    else:
        return False   
    
def factor(N):
    i = math.ceil(math.sqrt(N))
    while (N%i != 0):
        i -= 1
    return (int(i),int(N/i))

def main(digits):
    start = str(9)
    for i in range(1, digits):
        start += "9"
    start = int(start)*int(start)
    for i in reversed(range(1,start)):
        if (isPalindrome(i)):
            factors = factor(i)
            print i, 'factors', factors
            if (len(str(factors[0])) == digits and len(str(factors[1])) == digits):
                print i,'factors', factors, "<- OMG!"
                print "DONE!"
                break
    
main(3)
    
    
    