Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000




Solution:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2: return 0
        if len(nums1) == 1 and len(nums2) == 0: 
            return nums1[0]
        if len(nums1) == 0 and len(nums2) == 1: 
            return nums2[0]
        nums1 = nums1 + nums2
        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[(len(nums1)//2)] + nums1[(len(nums1)//2-1)]) / 2
        else:
            return nums1[len(nums1)//2]




Process:
The way we are going to solve this is adding the list together and using a sort method. 
First we do some edge cases to get rid of the weird data. After we add two list together and sort it with the built in python method. Then we check if there are an odd or even amount of numbers in the list to get the median. For a even list, we get two middle numbers to get the median, while in the odd list we just get the middle number 

1.) Edge cases:
    a.) check if one list is empty and the other is not
        - return a the element from the non empty list
    b.) do the same check base but opposite of the one before. 
    
2.) Combine lists:
    a.) add both lists together to create one
    b.) sort the list 
    
3.) Check if list is even or odd:
    a.) if list has even amount of numbers
        - get the 2 even numbers, add them, then divide for median and return
    b.) if list has odd amount of numbers
        - get the middle number and return it
    






