Problem:
Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

**Example 1:**

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

```

**Example 2:**

```
Input: "cbbd"
Output: "bb"

```




Solution:
def longest_palindrome(input_string):
  longest = ""
  for x in range(len(input_string)-2):
    if input_string[x] != " ":
      cur_elem = input_string[x]
      if cur_elem in input_string[x+1:]:
        occurrences = input_string[x+1:].count(cur_elem)
        index = 0
        for repeat in range(occurrences):
          index += input_string[x+1+index+repeat:].find(cur_elem)
          if (input_string[x:x+index+2+repeat] == ((input_string[x:x+index+2+repeat])[::-1])) and (len(input_string[x:x+index+2+repeat]) > len(longest)):
            longest = input_string[x:x+index+2+repeat]
          
  return longest




Process:
example 1
input: "jfjshdddhi" jfj hdddh
output: "hdddh"

example 2
intput: "cbdbcbdb"  cbdbc bdbcbdb
output "bdbcbdb"


our process to solving this problem is look through the input string element by element.
at each element we stop and count if there are any more elements that are the same as our current one
we then loop x times, (x being the amount of times we found a matching element) and test the string from the first time we saw the element to each time we found the matching element 
(we look at the substrings that end in the same element because that is a faster way in telling if it is a palindrome)

   
make a string to store out longest palidrome
loop through string element by element
	check to see if current element is not a space
		check to see if our current element is anywhere else in the string and count the occurrences
			loop x amount of times (x is the amount of times you found a matching element as the current)
				find the index of the matching element
				check to see if the input string from the current element to the current matching element is a palindrome
					if so then set it to the longest palidrome
return the longest palidrome







