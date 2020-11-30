Problem:
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".




Solution:
class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for m in range(len(s)):
            counter += 1
            counter = self.helper(m-1, m+1, s, counter)
            counter = self.helper(m, m+1, s, counter)
        return counter
                
    def helper(self, l, r, s, c):
        while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
        return c




Process 
The way we are going to solve this problem is with pointers
So since we want to return the number of palindromic substrings, all we have to do is keep a counter to 
keep track of them especially since each letter is unique. First we loop through every elements in the string and at each element we are going to do a test where we expand the length of the current substring until we do not have a palindromic substring anymore. The first test is for odd length substrings where we have a left and right side of the current element in the string. The second test is for even length substrings where we have also have a left and right but our current element represents the left. We increment our counter at each palindromic substring and return it after we gone through the whole string

1.) Variable: 
    a.) counter - to keep track of different palindromic substrings
    
2.) For Loop: 
    a.) increment counter for current substring which is an element 
    b.) call helper function for odd length substrings 
    c.) call helper function for even length substrings
    
3.) return counter


def helper(left ponter, right pointer, string, counter of palindromic substrings)
    - do loop while both pointers are within range of string and both left and right ponter are equal to eachother(palindromes always have same front and ends so check them and keep increasing the length until the ends are not equal)
        - increment counter, decrement left pointer, increment right pointer
    
    - return counter



        
  



