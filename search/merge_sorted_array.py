Problem:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n




Solution:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for x in range(len(nums1)-1, len(nums1)-1-n, -1):
            nums1.pop()
        for num in nums2:
            nums1.append(num)
        nums1.sort()




Process:
since the zeros in back of the first list represent the amount of numbers we are inserting from list2, we can pop them. (we can use a forloop and start from the back, and do this for how ever many numbers are in list2)
then, we have to add the numbers into from list2 into the first list
now we have all the numbers in list1 but it is not sorted, so we use the sort function







