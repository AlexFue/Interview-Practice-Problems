Problem:
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array will not contain duplicates.

Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].

Hints on the original problem: https://www.interviewbit.com/problems/rotated-array/




Solution:
def find_pivot_index(input_list):
	# List is sorted, but then rotated.
	# Find the minimum element in less than linear time
	# return it's index
	low = 0
	high = len(input_list)-1
	while low <= high:
		if input_list[low] < input_list[high]: return low
		mid = (low + high) // 2
		if input_list[mid] <= input_list[mid+1] and input_list[mid] <= input_list[mid-1]: return mid
		if input_list[mid] <= input_list[high]: high = mid - 1
		else: low = mid + 1




Process:
to find the smallest number, you start by checking the middle of the list
if you know its not in the left, then ignore it and check the right by doing the same process
if you know its not in the right, then ignore it and check the left by doing the same process


create variables for low part of array(first index), high part(the last index), and mid part(high + 1 div 2)
loop this while the low is lower than the high 
  check if the element at low is less than high, return the first element 
  check to see if the element in the middle is less than the next element and greater than the prev, return the middle
  if middle is less than high, high is the new mid minus one
  if middle is greater than low, low is the new mid plus one




