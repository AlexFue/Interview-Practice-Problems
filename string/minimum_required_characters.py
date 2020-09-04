Problem:
Minimum Characters required to make a String Palindromic

You are given a string. The only operation allowed is to insert characters in the beginning of the string. Return the number of characters that are needed to be inserted to make the string a palindrome string

Examples:Input: ABC
Output: 2
Input: AACECAAAA
Output: 2




Solution:
def minimumCharacters(n):
  counter = 0
  temp = ''
  for x in range(1, len(n)+1):
    temp = temp + n[-x]  
    counter += 1
    if (temp + n) == (temp + n)[::-1]:
      break
  return counter




Process:
since we want to make a palindrome by adding the minimum amount of chars, we can create a temp string and keep on adding chars from the back of the original string one by one and checking each time if it is a palidrome when added to the original string 
we take words from the back of the original string because that is the best way to create a palidrome and when we add it to the temp string, we added it to the back because when we check, it will be like mirroring 
ex: string = 'abcd'
	temp = 'd', check for palindrome 'd' + 'abcd' = dabcd, NOT PALINDROME
	temp = 'dc', check for palindrome 'dc' + 'abcd' = dcabcd, NOT PALINDROME
	temp = 'dcb', check for palindrome 'dcb' + 'abcd' = dcbabcd, YES PALINDROME


counter variable 

create temp variable to add the letters to check if string is an palindrome

loop through the length of the original string starting from the end

	we add the current element to the back of temp

	increment counter

	we check if it is a palindrome

		if it is then break

return the counter




Teacher Solution:
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # A palindromic string is equal to its reverse
        reverse = A[::-1]
        if reverse == A:
            return 0
            
        # Every string can be made a palindrome by prepending
        # (or appending) the reverse, and the outermost letter
        # can be ignored. An initial part of the reverse might
        # suffice if there are duplicate letters, so just count
        # how much of the reverse we need:
        for i in range(1, len(reverse)):
            if reverse[:i] + A == reverse + A[-i:]:
                break
        return i






