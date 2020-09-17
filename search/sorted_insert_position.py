Problem:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Examples:

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0




Soultion[Linear, less efficient]:
def find_index(sorted_list, target):
  for x in range(len(sorted_list)):
    if target <= sorted_list[x]:
      return x 
  return len(sorted_list)




Process:
looping through the whole list until the target value is less than or equal to the current value
if the the target value is less than or equal to the current value, return the index of where we are in the list 
if we went through the whole list and did not meet out value, return the length of the list because that is the index where the number should be placed

for loop through the length of the list 
  if the target value is less than or equal to the number at the current index of the list, return the current index 
return the length of the list




Teacher Answer [Binary, most efficient]:
def find_index(sorted_list, target):
  start = 0
  end = len(sorted_list)-1
  while start <= end:
    mid = (end + start) // 2 
    if target == sorted_list[mid]:
      return mid
    elif target < sorted_list[mid]:
      end = mid-1
    elif target > sorted_list[mid]:
      start = mid+1
  return start

What they are doing is starting the search from the middle of the list to be 2x as fast as Linear.
they create vairables 'start' and 'end' to keep focus on parts of the list only.
basically we start with the whole list and look at the middle value, since our list is sorted we know where the number is or should be
if we find the number then we return the middle index but if not, we look if our target is less than the current mid number or greater
if our target is less then we adjust the end variable to be the index before mid since we know the target is not the mid number or anything greater than that. 
if our target is greater, we do the same as the step before but on the other side of the list, the start variable gets moved to be the index after our mid since our target isnt the mid number of anything less than it.
we repeat these past steps of adjusting the start and end variable and checking the middle.












