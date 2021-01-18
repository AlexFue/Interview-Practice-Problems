Problem:
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.




Solution:
class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        for i, x in enumerate(a): # loop through array 
            if x > i + k: # if current num > then current index + k
                return i + k # return kth missing number which is index + k 
        return len(a) + k  # return length of array + k 




Process: 
The way we are going to solve this is by using array manipulation

Every number in should be <= to its index + k. 
This is because numbers should start at 1 and indexes start at 0 but when adding k, the sum should be at least equal or greater so the condition should statisfy. 

If the num gets > than the index + k, then we know that we skipped k nums so we return i + k which is the missing kth number.


If we did not find the kth missing number in the array, then return the length of arr + k because the kth missing number is k numbers after the last index of the arr
