Problem:
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500




Solution:
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = {} # dictionary to store modulo times we have
        ans = 0 # counter for num of pairs
        for t in time: 
            inverse = -t%60 # the inverse modulo, in other words, the other num we need to make a pair with our current modulo num
            if inverse in dic: # check if we have the inverse in the dictionary and increment how many we have because we could have multiple pairs. 
                ans += dic[inverse] # add the num of occurences of the inverse
            dic[t%60] = dic.get(t%60,0)+1 # our our cur modulo num we have to offer to dictionary
        return ans




Proces:
They way we solve this problem is with dictionary and math 

The idea is to loop through the list of times and for each time, store the modulo time needed to make zero inside a dictionary.
If you come across a inverse time you need in the dictionary, increment your answer counter because you just found a pair. 

The inverse if theh num we need and so that is why we find it. 
But we store our normal modulo of our cur num because that is the num we have to offer and found in the list. 
We could have the inverse in the dictionary that was the normal modulo of another number, that is why we check all the time and store our modulo nums. 




