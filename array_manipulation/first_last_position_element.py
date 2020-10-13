Problem:
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9





Solution:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while (l <= r) and (nums[l] != target or nums[r] != target):
            if nums[l] != target:
                l += 1
            if nums[r] != target:
                r -= 1
        if l > r:
            return [-1,-1]
        return [l, r]




Process:
The way we are going to be solving this is with pointers. Basically, we loop while both pointers 
are at either side of the target, meaning we found the range where it is located. 
Solution takes O(n) time and O(1) space.


1.) Create out variables:
	a. create a variable for our left pointers and our right pointer
		-these pointers will represent the sides of position for the element we are looking for 

2.) while loop: 
	- we are going to loop while our left pointer doesnt go past our right (if the pointers go past each other, that means that we never found are target in the list, so we break)
	- also, we loop while either of our pointers do not equal the target (we do this b/c what if one of out pointers found the target, but the other didnt so we want to still find it until pointers pointers find targets)
	a.) check if our left pointer is not on the target 
		- if not then we increment it (to see if the next value is the target )
	b.) check if our right pointer is not on the target
		- if not then we decrement it (to see if the next value is the target)
3.) returning 
	a.) if our left pointer past our right, that means we never found the target so we return [-1,-1]
	b.) if our pointers didnt pass eachother then we found the target and we return [left pointer, right pointer]




