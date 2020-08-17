Problem:
Given an unsorted integer array, find the first missing positive integer.
Example:
	Given [1,2,0] return 3,
	[3,4,-1,1] return 2,
	[-8, -7, -6] returns 1
	Your algorithm should run in O(n) time.




Solution: 
def first_missing_positive_integer(integers):
  #sorts the array and creates a variable for the missing int
  integers.sort()
  missing_int = 1
  # loop thorugh all the numbers in the array
  for x in range(len(integers)):
  	# every number should be less than the missing number(also known as the next number) but if its greater than it, then we skipped a number and so we return the missing number variable
    if integers[x] < missing_int:
      continue
    elif integers[x] == missing_int:
      # increment missing number to see if its the one missing next time in the loop
      missing_int += 1
    else:
      return missing_int
  return missing_int



Process: 
sort the list of integers
missing_int = 1
for loop through the list 
  if list[index] less than missing_int
    continue
  elif list[index] equal missing_int
    increment missing_int
  else
    return missing_int
return the missing_int 

