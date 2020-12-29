Problem:
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.




Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # keep track of smallest num 
        profit = 0 # keep track of greatest profit 
        for n in prices: 
            if n < min_price: min_price = n # checks if current num is smallest that min 
            if n - min_price > profit: profit = n - min_price # checks if current num makes a greater profit with the current min than the current profit 
        return profit # return profit




Process:
The way to solve this problem is buy using array manipulation. 

So for this problem, we are basically looking for the lowest valley and the highest peak that create teh greatest difference. 
Though, make sure that the valley comes before the peak. 

So we can create a variable that keep track of the smallest valley and a variable to keep track of the great difference. 

Then, we can loop through each element in prices to find the lowest num, while also finding the biggest difference by checking the difference at every num. 

This is so we can always check the biggest profit difference and for when we dont find a positive differnce, 
the profit is automatically set to zero for the special cases. 




