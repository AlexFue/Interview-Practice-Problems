Problem:
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length




Solution:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0 # variable to index through array 
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0): # checks if current num is 0, if the left and or right sides both have zeros to plant pot. also checks if we are at end and beginning of array 
                n -= 1 # minus number of pots we have to plant
                i += 2 # skip 2 indexes since the next one will not be plantable b/c current space is planted now
            else:
                i += 1 # move to next pot cause it coule be plantable 
            if n <= 0: return True # checks if all pots planted early before done with array 
        return False # if we didnt satisy check above, then we still have pots to plant 




Process: 
The way we solve this problem is with looping. 
So we want to loop through every element in the array but we have to first check if the current element is 0. 
Once we check that we can then check if the ends of the current index are also 0 to completely satisfy our ability to plant. 
If we can plant then we decrement the number of plots we have to plant and also increment our index by 2 since we know our in our next index we would not be able to plant since we just planted in the spot before. 
If we never satisfied our check then we increment by 1. 
We also always check if n <= 0 because we could be done planting early before we finish looping the array.
If we went through the whole array, then we never finish planting because it would of went with the early check, in that case we return False at the end. 
        


        