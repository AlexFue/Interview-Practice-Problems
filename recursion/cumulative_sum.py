Problem:
Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

For example, if n=4 , return 4+3+2+1+0, which is 10.

This problem is very similar to the factorial problem presented during the introduction to recursion. Remember, always think of what the base case will look like. In this case, we have a base case of n =0 (Note, you could have also designed the cut off to be 1).

In this case, we have: n + (n-1) + (n-2) + .... + 0




Solution:
def rec_sum(n):
	if n == 0:
		return 0
	else:
		return n + rec_sum(n-1)




Process
So whenever you are working with recursion, you always want to set a base case.
A base case is set input that keeps the code from calling itself infinetly.
In this case we want to add all the numbers between our number n and 0. 
So we want to stop at zero because that is the last number we are adding, this will be our base case. 
Now all we have to do is keep adding all the numbers down to 0, and we can do that by adding our current number to the number before, number before that, ect. 
But how we we write that in code? Well we can send our current-1 number back to the same function recursivly which will keep adding all numbers to 0.
Once we hit 0, it stops, and since we were adding all the numbers when we were returning, it adds them because it never got to do that, it had to keep computing the function first.

Visualization for n = 5:
5 + 5-1
	4 + 4-1
		3 + 3-1
			2 + 2-1		
				1 + 1-1				 
					0		
					(stop, now we go back up to finish our process of adding the numbers)
