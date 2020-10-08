Problem:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

2 <= height.length <= 3 * 104
0 <= height[i] <= 3 * 104




Solution:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxarea = 0
        while left < right:
            if height[left] > height[right]:
                temp = (right - left) * min(height[left], height[right])
                maxarea = max(temp, maxarea)
                right -= 1
            else:
                temp = (right - left) * min(height[left], height[right])
                maxarea = max(temp, maxarea)
                left += 1
        return maxarea




Process:
given a array of numbers, you want to return the max area of a container(rectangle). The max area is determined by the length from one bar to the other, times the height of the smallest bar of the two you are using to get the max. 

example: [4,3,2,1,4] -> 16 

So we are going to solve this using pointers on both sides of the list. We are going to get the area of our current pointers and check if its a max. 
Then, depending on which pointer is smaller, we move it on position to the opposing side. We do this process until are pointers over lap eachother.

1.) Variables: creater two pointer variables, one points to the first element, the other points to the last element. Also create a maxarea variable to keep track of your max area. 
    
2.) While loop: we are going to do this while loop while the left pointer is less than the right one.
    a.)check if the element at the first pointer is greater.
        get the area of the two pointers. 
        check if the area is greater then the maxarea and set it.
        then since the element at the left pointer was greater, we decrement the right pointer to see if we find a greater element at the pointer that produces a greater area
        
    b.)check if the element at the left pointer is greater or equal.
        get the area of the two pointers. 
        check if the area is greater then the maxarea and set it.
        then since the element at the right pointer was greater or equal, we increment the left pointer to see if we find a greater element at the pointer that produces a greater area

3.) return the maxarea





