Problem:
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

 

Example 1:

Input: arr = [85], pieces = [[85]]
Output: true
Example 2:

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]
Example 3:

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].
Example 4:

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]
Example 5:

Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false
 

Constraints:

1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
The integers in arr are distinct.
The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).




Solution:
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {} # store all sublists of pieces with first num from them as keys
        
        for piece in pieces: # loop to store sublists into dictionary 
            d[piece[0]] = piece
        
        ans = [] # list to hold ans from contatenating sublists from dictionary 
        
        for num in arr: # loop through each num in arr and check if its in dictionary to add its sublist its connected to to ans
            if num in d:
                ans += d[num]
        
        return arr == ans # check if ans and arr are the same after concatenation




Process:
The way we are going to solve this is with a dictionary

Since we have to sort the pieces without actually moving any of the nums in the list, we can use a dictionary. 
In the dictionary, store the first num of each sublist in pieces with the value as the sublist. 
Do this to be able to get each sublist in pieces and put them together into another list 

Then create another list and put all the sublists from the dictionary in order of arr. 
We can loop through each num in arr and get the array thats associated with it in dictionary and add it to the new list we made. 

We only check the first num since we cant move any of the nums in the sublists, checking what they are will be pointless and we only hope that at the end it is sorted unless its impossible. 





