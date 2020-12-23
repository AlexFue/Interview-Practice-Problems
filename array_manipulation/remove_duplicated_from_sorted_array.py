Problem:
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
 

Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.





Solution:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 # left pointer variable 
        for r in range(1,len(nums)) # loop for right pointer
            if nums[l] != nums[r]:  # checks if left ponter and right pointer variable are not the same, 
                l += 1 # if so we increment left pointer so we change change the num to what right pointer is pointing to 
                nums[l] = nums[j]
        return l + 1 # we return left pointer +1, bascially the number of unique nums since left only incremented when we found a new num
    
# EX: [0,0,1,1,1,2,2,3,3,4] -> [0,1,2,3,4,2,2,3,3,4]
# you see it put all the nums at the front 





Process:
The way we are going to solve this problem is with a 2 pointer approach. 

Basically we find when the nums that the pointers are pointing to are different, then we increment the left pointer and change the num to the value that the right pointer is pointing to. 

We are pretty much putting all the numbers in the front once.


