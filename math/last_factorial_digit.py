# problem: 
# Given a non-negative number, N, return the last digit of the factorial of N.



# The factorial of N, which is written as N!, is defined as the product of all of the integers from 1 to N.

# Given 3 as N, the factorial is 1 x 2 x 3 = 6
# Given 6 as N, the factorial is 1 x 2 x 3 x 4 x 5 x 6 = 720
# Given 9 as N, the factorial is 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 = 362,880

# As you can see, the number can grow to be quite large, quite quickly.

# Write a function that will return only the last digit of N!, given N.


# solution: 
import math
def last_factorial_digit(n):
  fac = 0
  fac = math.factorial(n)
  return int(str(fac)[-1])


# process: 
# get number n

# fac = 0

# find factorial of N with math.factorial(n)

# set the factorial above to the variable fac

# turn the factorial to a string and get the last element and then turn it back to a int and return it