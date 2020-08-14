Problem: 
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false




Solution: 
import math 
def power_of_three(n):
  power = 0
  while 3**power <= n:
    if 3**power == n:
      return True
    power += 1
  return False




Process: 
varible power that represents the power of 3 and starts at 0

while 3**power <= n #does this while the power of 3 is under n 

	if 3**power == n  #checks if it is a power of three

		return true

	power +=1 #increments to check if the next power is under n

outside the while loop return false