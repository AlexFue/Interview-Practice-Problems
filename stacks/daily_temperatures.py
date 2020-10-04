Problem:
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].




Solution:
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        days = [0] * len(T)
        
        for x in range(len(T)-1, -1, -1):
            while stack and T[x] >= stack[-1][0]:
                stack.pop()
            if stack and T[x] < stack[-1][0]:
                days[x] = stack[-1][-1] - x
            stack.append((T[x], x))
        return days




Process:
so given a list of temps, for each temperature in the list, you have to find how many days til the next hot day comes and put that into a list. 

example: 
T = [73, 74, 75, 71, 69, 72, 76, 73]

so our idea is to use a stack and start from the back of the daily temperatures list. When we do this, we will know what the hottest day was already so we can just check the stack for when the hottest day was

create a stack to keep track of temps 
create a list to keep track of days and fill it with zeros as much as the length of T

for loop through temperatures, starting from the end
    while loop through stack and while last element of stack does not have a greater temp than our current one
        pop from stack 
    if we found a temp that is greater than our current one
        change our days list at x to the numbers of days apart from current temp to hotter temp
    then we always add out current temp into a stack as a set like this: (temperature, x). {x is the current index of the for loop}

return the days list
    