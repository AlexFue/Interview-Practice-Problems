Problem:
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4




Solution:
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return # lists < 3 are not allowed
        nums.sort() # sort to make algorithm easier and possible with pointers
        result = nums[0] + nums[1] + nums[2] # create a default result to just the first 3 
        for i in range(len(nums) - 2): # loops our initial pointer 
            l, r = i + 1, len(nums) - 1 # sets the left and right pointers to the end, but after the initial pointer 
            while l < r: # check for sum while left pointer is behind right 
                s = nums[i] + nums[l] + nums[r] # get current sum 
                if s == target: # check if curent sum is the target to return 
                    return s
                if abs(s - target) < abs(result - target): # check if cur sum difference < min sum difference 
                    result = s # set the min sum to cur sum if needed 
                if s < target: # if cur sum < target, move left pointer up to increase sum 
                    l += 1
                elif s > target: # if cur sum > target, move right pointer down to decrease sum 
                    r -= 1
        return result

    


Process:
The way we solve this problem is with pointer like 3sum.

What we want to do is create a initial pointer that will loop through out the array and 2 ending pointers, left and right. 
We check if the the current difference is less than the min difference, if so we update the our min to be the current sum so we can return it at the end 
We also increment / decrement out left/right pointer accordingly to get the sum to be closer to the target. 





