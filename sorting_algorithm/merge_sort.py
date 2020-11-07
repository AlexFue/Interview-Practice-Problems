Problem:
Here is the implementation of merge sort and how it works. I recommend copying this code and 
putting it in pythontutor.com to get a better understanding how it works




Code:
def merge(lst):
  # check if the lenth of list > 1 so we can split  
  if len(lst) > 1:
    # get the middle index
    m = len(lst) // 2
    # create 2 lists and to represent both sides of the list
    left = lst[m:]
    right = lst[:m]
    # recursively call on both sides until there is 1 elem in list
    merge(left)
    merge(right)
    # once list is broken down to ones, we backtrack and combine them 1 by 1 
    merger(lst, left, right)

# this adds all numbers from left/right list to the main but sorted with pointers
def merger(arr, left, right):
  # indexes to loop through left list and right list
  l = r = 0
  # index to loop through main list
  k = 0 

  # find the smallest number between left/right list and add it to main list, increment indexes that are needed
  while l < len(left) and r < len(right):
    if left[l] < right[r]:
      arr[k] = left[l]
      l += 1
    else:
      arr[k] = right[r]
      r += 1
    k += 1

  # if there are still numbers in the left/right list, add remaining nums to the main

  while l < len(left):
    arr[k] = left[l]
    l += 1
    k += 1

  while r < len(right):
    arr[k] = right[r]
    r += 1
    k += 1

arr = [3,2,7,5,0,9]
merge(arr)
print(arr)


we are going to implement merge sort 
the way merge sort works is by spliting up an array by halves, all the way until they are in ones. 
then you merge them back together in ascending order. 


