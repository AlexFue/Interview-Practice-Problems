Problem:
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

 

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2

Explanation: 

 

Note:

The width sum of bricks in different rows are the same and wont exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.




Solution:
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = {} # dictionary to keep track of passes 
        m = 0 # max pass variable 
        for lst in wall: # loop through ever sublist 
            total = 0 # keep track of the total bricks we passed in the sublist 
            for x in range(len(lst)-1): # lop through every element in sublist, except last elements
                total += lst[x] # add current brick num to total 
                d[total] = d.get(total, 0) + 1 # add total to dictionary because after total, there is a pass we can go through 
                m = max(m, d[total]) # adjust max if current # of passes is greater 
                
        return len(wall) - m # get the num of walls we didnt pass for our best path. 




Process:
To solve this problem we are goin to use a hashmap. 

So we have to to find the least number of bricks to pass. 
To make it easier we can try to find the most number of bricks to pass in between. 

We can find a path if we look towards the right of a brick, except the last one since we cant use edges. 
In that case, we can loop through every brick in a wall and keep track at which brick there is a path. 
We can do this for every wall and also keep track of which wall has the most passes. 

Now we want the last walls to pass, and we have the most paths passed so we can subtract the length of wall variable by our max paths since that gets us the bricks we didnt pass. 

Heres how our dictionary will loop like with the given example after going through every brick
         d = {
            1:3
            3:3
            5:2
            4:4
            2:1
        }
