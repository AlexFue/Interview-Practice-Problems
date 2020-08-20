Problem: 
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

There are several approaches to this problem. Start with one that makes sense to you- so long as you pass all the tests. 

Remember to try to solve the problem first by using the most naive solution, then start asking yourself questions about the operations you're doing to try to reduce the amount of time and space used. 




Solution:
def single_number(integers):
  integers.sort()
  # loops through every two numbers in the list because they should be the same
  for index in range(0, len(integers), 2):
  	# first part of the if statement is for if the single number is at the end, second part checks if two connsective numbers match and if not then returns the first of the two
    if (index + 1 == len(integers)) or (integers[index] != integers[index+1]):
      # returns number at current index because its the only place it can be when comparing two numbers at a time 
      return integers[index]
  return 0




Process: 
sort the list of integers

for loop through the list of integers, incrementing by 2

	if (number at current index and number at index plus one not the same) or (index+1 == len(list))

		return the number at current index




Teacher Solution: 
def single_number(integers):
  seen_numbers = []
  for integer in integers:
    if integer in seen_numbers:
      seen_numbers.remove(integer)
    else:
      seen_numbers.append(integer)
  return seen_numbers.pop()




More Efficient Solution: 
def single_number(integers):
  while len(integers) > 1:
    if integers[0] in integers[1:]:
      repeated_int = integers[0]
      integers.remove(repeated_int)
      integers.remove(repeated_int)
  return integers[0]




