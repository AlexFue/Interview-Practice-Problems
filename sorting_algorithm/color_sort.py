Problem: 
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]




Solution1:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            m = len(nums) // 2
            left = nums[:m]
            right = nums[m:]
            self.sortColors(left)
            self.sortColors(right)
            self.helper(nums, left, right)
        
    def helper(self, nums, left, right):
        l = r = 0
        i = 0
        
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[i] = left[l]
                l += 1
            else:
                nums[i] = right[r]
                r += 1
            i += 1
        
        while l < len(left):
            nums[i] = left[l]
            i += 1
            l += 1
            
        while r < len(right):
            nums[i] = right[r]
            r += 1
            i += 1

Solution2:
def color_sort(nums):
  moves_right = 0
  for x in range(len(nums)):
    if nums[x - moves_right] == 0:
      nums.insert(0, nums[x - moves_right])
      del nums[x - moves_right + 1]
    elif nums[x - moves_right] == 2:
      nums.append(nums[x - moves_right])
      del nums[x - moves_right]
      moves_right += 1 
  return nums





Process1:
The way we are going to solve this is by implementing the merge sort algorithm to sort our colors. 
If you do not know how that works. basically you seperate the list to halves until they are in singles, 
then you backtrack and start to join the lists back together but sorted. 

Process2:
example 
input = [1,2,0,2,1,0,2]
step = [1,0,2,1,0,2,2] moved 2 to the back 
step = [0,1,2,1,0,2,2] moved 0 to the front 
step = [0,1,1,0,2,2,2] moved 2 to the back 
step = [0,0,1,1,2,2,2] moved 0 to the front
output = [0,0,1,1,2,2,2]

do this process n amount of times 
  if a number is 2, move to back and dont go on to the next element
  if a number is 0, move to front and go on to the next elelment
  if it is a 1, go on to next element


for loop through the array
  if cur element is 0, move it at index 0
  if cur element is 2, move it to the back 
  keep track of the amount of elements that are moved to the back, when accessing an element from the array, subtract the index by the amount of times you moved an element to the back so you wont accidentally skip an element 
return sorted array










