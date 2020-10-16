Problem:
Getting a Different Number
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4 
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ MAX_INT
0 ≤ arr[i] ≤ MAX_INT for every i, 0 ≤ i < MAX_INT
[output] integer




Solution:
def get_different_number(arr):
  m = 0
  s = set(arr)
  
  while m < len(arr):
    if m in s:
      m+=1
    else:
      return m 
  return m




Process:
So we are going to solve this problem using a set and a variable to keep track the missing number. 
We are going to put all the numbers from the array in to a set and check if our min number is
in there, if it is then thats not the missing number so we increment, else we did find it so 
we return it. We repeat this process and if we go through the whole array without finding the missing 
number, we return our min because that is the next number. 


1.) Variables:
	a.) min variable 
		- We want to find the first missing number and we only have an array of positive numbers 
		  so we can set a min variable to 0. 
	b.) set variable 
		- He is where we will put all the variables from the array into the set to be able to 
		  check if the min variable is there

2.) Loop: 
	a.) We want to find the first missing min so we check if our min is in the set()
		- if it is then thats not the missing min, so we increment it 
	b.) if our min wasnt in the set then thats the missing num and we return it 

3.) if we made it out the loop, the sets wasnt missing a min number so we return our min, which is the next min 


Time Complexity: O(n), depends on how big the array is 
Space Complexity: O(n), we duplicate the array data into a set 

Tips: With sets, we can check if a element is in at linear time. Its likes a set but w/o the values





