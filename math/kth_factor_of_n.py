Problem:
Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

 

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
Example 4:

Input: n = 1, k = 1
Output: 1
Explanation: Factors list is [1], the 1st factor is 1.
Example 5:

Input: n = 1000, k = 3
Output: 4
Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].




Solution:
class Solution:
    def kthFactor(self, n: int, k: int) -> int:       
        for num in range(1, (n//2)+1): # loop though nums from 1 to n//2
            if n % num == 0: # checks if num is a factor
                k -= 1 # decrements the k everytime we find a factor 
                if k == 0: # if k is 0, that means we found the kth factor 
                    return num # so we return our current factor 
        if k - 1 == 0: return n # checks if kth factor is our num n since it is also a factor but we havent checked it yet
        return -1 # if k was greater than the num of factors n has





Process:
The way we solve this problem is with math. 
We know that a factor can not be higher than n//2 and n itself so we just loop to n//2 to save time.
We check every num if its a factor and if it is, we decrement k since that is one less factor we have to look at. 
Everytime we have a factor we check if k is zero because we could be on the kth factor.
At the end, we check if k is 1 because n could be the factor we want to return. 
If we have not returned a factor yet, return 0 because the kth factor is greater than the number of factors that n has. 

