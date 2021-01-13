Problem:
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
 

Constraints:

1 <= slots1.length, slots2.length <= 10^4
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 10^9
1 <= duration <= 10^6 





Solution:
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        p1, p2 = 0, 0 # points to loop through slots 
        s1_len, s2_len = len(slots1), len(slots2) # get the length of the slots 
        
        slots1.sort() # sort both slots so they are in order to check 
        slots2.sort()

        while p1 < s1_len and  j < s2_len: # loop through slots until out of range of one of them or both 

            max_s = max(slots1[p1][0], slots2[p2][0]) # get the max start
            min_e = min(slots1[p1][1], slots2[p2][1]) # get the min end 

            if min_e - max_s >= duration: # check if the duration between max start and min end is within duration 
                return [max_s, max_s + duration] # return the duration 

            if slots2[p2][1] - max_s < duration : # check if the duration for slot2 if it failed to meet duration time 
                p2 += 1 # increment its pointer if so 

            if slots1[p1][1] - max_s < duration : # check if the duration for slot1 if it failed to meet duration time 
                p1 += 1 # increment its pointer if so 

        return [] # return empty if no slot found 




Process:	
The way we are going to solve this problem is by using pointers. 

Create a pointer to loop through each slot. 

We are going to loop through the slots using the pointers until we are out of range. 
Here we get the max starting time and min ending time for both slots because thats the range where both slots are available. 

First check if the range betwen the max and min is within the duration, if so we found the time slot

If not, check which slot fails by checking them individually

Check if time range between the max start and end time of slot2 is less than duration, then increment its pointer 

Check if time range between the max start and end time of slot1 is less than duration, then increment its pointer. 

If we finish the loop, return [] because we never found a available timeslot.   





