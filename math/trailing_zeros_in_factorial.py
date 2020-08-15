Problem:
Below is the prompt for a stretch problem. This problem involves all the same operations you're used to, but with the added complexity of needing to solve it without brute-force (eg, you can't just calculate the factorial manually.)

Originally located here: https://www.interviewbit.com/problems/trailing-zeros-in-factorial/

Prompt

Given an integer n, return the number of trailing zeroes in n!.

Your solution should be in logarithmic time complexity.




Solution: 
def fast_trailing_zero_factorial(n):
  trailing_zeros = 0
  power = 1
  while 5**power <= n:
    trailing_zeros += (n // (5**power))
    power += 1

  return trailing_zeros

 


Process: 
variable called var_zeros
find out how many times 5 goes into n and set it to var_zeros
return var_zeros

we do this because there is a pattern
the number of trailing zeros increases by one after each 5 numbers not including 0
so from 1 - 4 theres 0 trailing zeros 
5 - 9 theres 1 trailing zero, 10 - 14 theres 2 trailing zeros, etc.


n	n!	Trailing zeros
1	1.00	0
2	2.00	0
3	6.00	0
4	24.00	0
5	120.00	1
6	720.00	1
7	5,040.00	1
8	40,320.00	1
9	362,880.00	1
10	3,628,800.00	2
11	39,916,800.00	2
12	479,001,600.00	2
13	6,227,020,800.00	2
14	87,178,291,200.00	2
15	1,307,674,368,000.00	3
16	20,922,789,888,000.00	3
17 3
18 3
19 3
20 4
21 4
22 4
23 4
24 4
25 6
26 6