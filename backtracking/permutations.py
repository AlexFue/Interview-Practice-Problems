Problem:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]




Solution:
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper([], nums, ans)
        return ans
        
        
    def helper(self, arr, nums, ans):
        if not nums:
            ans.append(arr)
        else:
            for x in range(len(nums)):
                self.helper(arr + [nums[x]], nums[:x] + nums[x+1:], ans)




Process: 
The way we are going to solve this problem is with recursion and back tracking.
We first create a answer list that will store all the permuations of the nums list. We then insert into our helper 
method that will find all the permutations. It takes in a permutation array, the nums array, and the answer array. 
If the nums array is empty, meaning our current permuation list is done, we add it to the answer list. If not then 
we run a for loop that goes through all the nums in the nums list. For each num it recursively calls the function 
by taking in the permutation list with the current added num, the nums list without the current number that was 
just added to theh permuation list, and the answer list. Once the nums list is empty, it back tracks to find the 
other permutations. 

1.) Variable
    a.) ans list - holds all the permuations 

2.) call helper function - will update the ans list with all the permutation

3.) Return the updated ans list


helper function(permuation list, nums list, ans list)
    a.) checks if nums array is empty to add current permutation to ans list
    b.) loops through nums in nums list
        - calls function recursively(permuation list w/ current num added, nums list w/o current num added, ans list)
