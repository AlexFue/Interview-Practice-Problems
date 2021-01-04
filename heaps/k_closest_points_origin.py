Problem:
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)




Solution:
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [] # heap to store distances/points from least to greatest
        ans = [] # list to store k min points 
        
        for point in points: # loop through points
            distance = math.sqrt(point[0]**2 + point[1]**2) # calculate distance from point to origin 
            heapq.heappush(heap, (distance, point)) # add distance and point to heap 
                
        while K > 0: # loop from 0 - k
            val = heapq.heappop(heap) # pop the min distance/point
            ans.append(val[1]) # add only point to list
            K -= 1 # decrement k since its one less points to get
        return ans




Process:
The way we are going to solve this is by using a min Heap 

The idea is we convert all points into distance and add them to our heap and the heap will sort it from least to greatest. 
When we add the distances to the heap, add both the distance and the point so we can return the point later 

Once that is done, loop from 0 to K and return the min distances. 
You can just pop from the heap since the popping gives the first/smallest distance.
Add these popped points into another list and return that list. 






