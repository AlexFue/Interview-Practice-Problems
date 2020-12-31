Problem:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30




Process:
class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        
        dp = [0,1]
        
        for x in range(2, n+1):
            dp += [dp[x-1] + dp[x-2]]
        
        return dp[-1]




Solution:
The way we are going to solve this problem is by using dynamic programming(bottom-up approach)

Improve upon the recursive option by using iteration, still solving for all of the sub-problems and returning the answer for N, using already computed Fibonacci values. In using a bottom-up approach, we can iteratively compute and store the values, only returning once we reach the result.

Algorithm

If N is less than or equal to 1, return N
Otherwise, iterate through N, storing each computed answer in an array along the way.
Use this array as a reference to the 2 previous numbers to calculate the current Fibonacci number.
Once we've reached the last number, return it's Fibonacci number.

