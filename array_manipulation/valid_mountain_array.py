Problem:
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104




Solution:
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False # base case for the smaller nums
        
        index = 0 # variable for our index
        length = len(arr) # variable for length 
        
        while index + 1 < length and arr[index] < arr[index+1]: # increase: check that we are not at the end and our current num < the next one
            index += 1
            
        if index == 0 or index == length-1: return False # check if our peak is at the end of the array
        
        
        while index+1 < len(arr) and arr[index] > arr[index+1]: # decrease: check that we are not at the end and our current number > next one 
            index += 1
            
        return index == length - 1 # checks if we are at the end of the array or not, meaning we have a mountain array 




Process:
The way we are going to solve this is with array manipulation. 

Since the array has to increase then decrease, that means we can have check cases for both. 
We can a loop through all the increasing numbers then once we are at the peak, it breaks and goes into another loop that goes through all the decreasing numbers. 

We also check if we peak at early, meaning we never decrease and so we return false. 
Finally we check if we are at the end of the array, meaning we have a mountain array 




