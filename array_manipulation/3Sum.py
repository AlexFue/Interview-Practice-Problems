Problem:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105




Solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # these lines deal with corner cases
        if len(nums) <3: 
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]
        
        ans = []
        nums.sort()
        x = 0
        
        
        while x < len(nums): # incrementer for our initial pointer
            l = x + 1
            r = len(nums)-1
            while l < r: #do this loop while l < r so we dont get duplicated values 
                sums = nums[x] + nums[l] + nums[r]
                if sums == 0: # if sum is 0, store it 
                    ans.append([nums[x]] + [nums[l]] + [nums[r]])
                    left_val = nums[l]
                    while l < len(nums) and nums[l] == left_val: #this increments our left pointer to skip over duplicated numbers of current so we don't store them 
                        l += 1
                    right_val = nums[r]
                    while r > l and nums[r] == right_val: #does same with duplicated but for right and decrements
                        r -= 1   
                elif sums < 0: #checks if sum is less then to move left pointer
                    l += 1 
                else: #checks if sum is greater then to move right pointer
                    r -= 1
            while x+1 < len(nums) and nums[x] == nums[x+1]: #does same with duplicates but for initial pointer and increments
                x += 1
            x += 1 #always increment inital pointer after each initeration 
        return ans




Process:
The way we are going to solve this problem is with 3 pointers 
So we have our initial pointer that increments from left to right by 1. Within our initial
we have a left pointer and a right pointer, the left is 1 + initial and the right is 
1 - len(nums). We loop our from until left is not less than right pointer. We get the sum of our
current pointers values and create a sum. If sum is 0 we add the pointers to an ans list. 
We then increment the left pointer to the right until therenot more duplicates of the current 
left pointers value as seen in line 53, do the same for right pointer but to the left on line 56, 
then the same for the initial pointer on line 62. If our sum if less than 0 we increment left 
pointer and if its greater than 0, decrement right pointer. At the end we always increment our 
initial pointer.
    




