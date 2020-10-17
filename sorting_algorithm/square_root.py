Problem:
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.




Solution:
def squareRoot(num):
	return int(num**.5)




Process:
example 1
input = 9
output = 3

The way we solve this is like we normally find squareroots in math. We can convert the squareroot
symbol to a power of .5 which is the equivalent and then make it an int

sqrt(n) -> n^(1/2) -> n^(.5) : turn it to an int 
so we can convert the square root to the power of 1/2 or .5 
find the answer to that and turn it to an int 

return integer n^.5