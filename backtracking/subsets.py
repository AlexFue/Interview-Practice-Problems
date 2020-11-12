Problem:
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]




Solution:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combos = []
        self.helper([], combos, nums)
        return combos
        
    def helper(self, combo, combos, nums):
        combos.append(combo)
        for x in range(len(nums)):
            self.helper(combo + [nums[x]], combos, nums[x+1:])




Process:
The way we are going to solve this problem is by backtracking.
To create all the combos, we create a helper function that will do the work for us. 
It takes in a list to keep track of the combos, a single combo list, and the nums list. 
Each time we call the function we add the current combo to our list of combose and run a loop. 
This loop will add each number from the nums list, return the combos list, and shift the nums list recursivley to do this process again. 
We basically creating different versions of each for the numbers with recursion. 
Use pthon tutor: visualization(http://www.pythontutor.com/visualize.html#mode=display 
and draw it out on a whiteboard

1.) Variable
    a.) create a list to store all the combos for the nums list, called combos
    
2.) Helper function
    - call it to do the whole process 
    - Takes in 
        a.) combo list, represents a single combo for each recursive function call 
        b.) combos list, the list of combos we created to store all the combos. 
        c.) nums list, the list of nums we are trying to create the combos from
    a.) add current combo list into combos list 
    b.) Loop
        - adds the current num from nums list into combo list 
        - changes the nums list index to the current index + 1, ex: [1,2,3] -> [2,3]. We shift the viewing of it to we can create other combos. 
        - we do all this recursive and send it to the function again. 

3.) Our combos list should now have all the possible combos so we can now return it. 





