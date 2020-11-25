Problem:

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]




Solution:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        m = -1
        d = {}
        
        for n in nums:
            d[n] = d.get(n, 0) + 1
            m = max(m, d[n])
        
        l = [-1] * (m + 1)
        
        for key, val in d.items():
            if l[val] == -1:
                l[val] = [key]
            else:
                l[val] += [key]
        
        ans = []
        x = len(l)-1
        while len(ans) != k:
            if l[x] != -1:
                ans += l[x]
            x -= 1
                
        return ans[:k]




Process:
The way we are going to solve this is with a dictionary
So we are going to create a dictionary to store all the occurences of each element, also we keep track of teh most occurences of a element. Then we create a list that will store all the elements and their occurences based on their index. So if the number 1 occurs 3 times, we would insert number 1 into index 3. We do this so when we loop through the list backwards and return the first k numbers with greatest occurences. 

1.) Variables:
    a.) Dictionary - to store occurences of numbers
    b.) max - holds the most occurences of a number
    
2.) Loop 1: 
    - tallies all the occurences from the nums list and stores in dictionary
    - also gets the most occences of a number

3.) Loop 2:
    - Creates a list of size of the most occurences + 1, and puts -1 as he default values
    - Stores all the keys from dictionary into their correct index into the list, based on their occurence
    
4.) Loop 3:
    - creates a list to store the top k number occurences
    - loops through occurence list to get the top k num occured and stores them into the other list.
    (there may be some values in the list from the second loop that are still -1, we skip over those) 
    
    
    
    
    
    
    
            
        
    
