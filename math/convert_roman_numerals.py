Problem: 
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example:
Two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Prompt
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.



Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

We've gone ahead and provided you a helper function- this is an idea you should match from. Breaking the problem down into smaller bits is a great tactic- rather than solving the whole problem, break it down into smaller problems!




Solution: 
def roman_to_decimal(roman_numeral):
  arabic_numeral = 0
  i = 0
  
  while (i < len(roman_numeral)): 

    # Getting value of symbol s[i] 
    s1 = value(roman_numeral[i]) 

    if (i+1 < len(roman_numeral)):

      # Getting value of symbol s[i+1] (the next number)
      s2 = value(roman_numeral[i+1])

      # Comparing both values 
      if (s1 >= s2): 
        arabic_numeral += s1
        i += 1
        # when you see "pass", replace it with your code
        # Value of current symbol is greater 
        # or equal to the next symbol 

      else: 
        arabic_numeral += (s2 - s1)
        i += 2
        # when you see "pass", replace it with your code
        # Value of current symbol is less than 
        # the next symbol 
    else:
      arabic_numeral += s1
      i += 1
      # when you see "pass", replace it with your code
      
  return arabic_numeral 

def value(r): 
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000
    return -1
    
print(roman_to_decimal('XIXXV'))




Process: 
make a varible called arabic numeral which is the final value that we are going to return 
var i for the index 
while loop to get each char of the roman numeral 
  get the value of the current roman numeral and put it in a var
  if there is a roman numeral after the current
    we get its value and store it in a var
    if the first roman numeral > second roman numeral 
      add both together to arabic_numeral
    else 
      arabic_numeral = second roman numeral - first roman numeral 
  else
    then we are at the last roman numeral and we can add its value to arabic_numeral
  increment i by 2 because you already added the first two roman numerals 






Solution 2: 
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000}
        
        previous = 'I' # setting the previous to the smallest numeral because when we first start the loop, since we are at the end, it doesnt have a previous and so we just want to add it 
        
        total = 0 # variable to keep track of our total 
        
        for cur in s[::-1]: # loop through string, starting from the end
            if d[cur] < d[previous]: total -= d[cur] # if the current numeral is less than the previous, then you are at the edge case so subtract the current numeral
            else: total += d[cur] # otherwise, add the current numeral
            previous = cur # always set the cur to the previous before going to the next number
        
        return total



Process 2:
The way I solved this problem is with string manipulation

Since the roman numerals go from biggest left to smallest right and the only time that is not the case is when you have IV or IX, etc. 
We can traverse the string from right to left and check for those cases. 
You just have to remember the previous numeral and check if the current one is not less than the previous one. 
If it is, then you are at a edge subtraction case and so you would have to subtract that current number from the total.
For everything else, just add like normal. 

