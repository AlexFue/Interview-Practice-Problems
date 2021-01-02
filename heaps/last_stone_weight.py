Problem:
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.




Solution:
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for x in range(len(stones)): # turn each num negative to work with minHeap as a maxHeap
            stones[x] *= -1
            
        heapq.heapify(stones) # turn list into minHeap 
        
        while len(stones) > 1: # loop until less than 2 items to compare
            stone1 = heapq.heappop(stones) # pop 2 items, will return the top items which are the max, or min in this case since we are using a minHeap
            stone2 = heapq.heappop(stones)
            if stone1 != stone2: # if the items are not the same, subtract and add it back to heap 
                heapq.heappush(stones, stone1 - stone2)
        
        return -1 * heapq.heappop(stones) if stones else 0 # return last item if needed or 0




Process:
The way we are going to solve this is by using heaps. 

Python only has a minHeap class but we can inverse all the nums in stones to make our minHeap work like a maxHeap. 

After that we use the heapify function to turn stones into a heap. 

Then we should keep on taking the 2 max stones which are the top ones and if they are different substract and add the remainder to the heap. 
Each time you add and remove items using the heap functions, the heap gets adjusted to turn back to a min heap. 

We do this process until we only have 1 item or less since we cant compare 2 things and we return what we have left. 




