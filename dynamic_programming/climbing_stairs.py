Problem:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step




Solution:
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n # base case
        
        dp = [1,2] # set our memoization 
        
        while len(dp) < n+1: # add to our memoization until we get to n 
            dp.append(dp[-1]+dp[-2]) # the unique ways for the current step is the sum of the unique ways of the previous 2 steps
        return dp[-1] # return the unique steps for n 




Process:
They way we are going to solve this problem is using dynamic programming (bottom-up approach).

Since this is dp, we need to use memoization and for this case, it would be the all the distinct way of the previous steps before n. 

Steps from 0 - 2 are special cases where they return themselves so we can use that as a base case and for our memoization data structure. 

To get the all the ways for n steps, you need to find it for the 2 previous steps (n-1, n-2) and build off that.
So we start at the beginning and keep on getting the unique ways for the current number of steps from the previous 2, all the way till n. 

Once you do that, return the last element in memoization since thats the unique ways for n 






