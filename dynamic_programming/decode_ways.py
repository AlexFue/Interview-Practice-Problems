Problem:
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "111" can have each of its "1"s be mapped into 'A's to make "AAA", or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA". Note that "06" cannot be mapped into 'F' since "6" is different from "06".

Given a non-empty string num containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0. The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20".
Since there is no character, there are no valid ways to decode this since all digits need to be mapped.
Example 4:

Input: s = "1"
Output: 1
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).




Solution:
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0]*(len(s)+1)

        # base case initialization
        dp[0] = 1 # a string  of length 0 can always be decoded once
        dp[1] = 0 if s[0] == "0" else 1 # the beginning can be decoded once if its a num > 0 or 0 if the num is 0

        for i in range(2, len(s) + 1): # loop through each num, starting at 2 b/c so we can check for 2 digit nums 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9: # check for 1 digit num and add its decoded ways to the current length we are checking 
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: # check for 1 digit num and add its decoded ways to the current length we are checking
                dp[i] += dp[i - 2]
        return dp[len(s)] # returning last value, also known as the total decoded ways. Its llike the summation of all the decoded substrings ways of s. 




Process:
The way we solve this problem is by using dynamic programming, bottom up approach. 

First create the memoization array and to store the number of ways a substring can be decoded. 
A empty string can be decoded once so at dp[0], its 1 and at dp[1], its 1 or zero, depending if the num is zero or not. 

In our dp, the index represents the length of the substring and the value is the number of ways that substring of that length can be decoded.

We loop through every character +1, starting from 2 since we are going to be looking back.
Each time we check for a single digit num and add the number of ways it can decoded whch is the number of ways the index of that substring was decoded
Also check for a 2 digit num and add the number of ways it can be decoded which is the number of ways the index of that substring was decoded


Then return the last element in the dp array which is total number of ways s can be decoded as a whole. 

We solved this with an initial small substring and enlarging it each time.









