Problem:
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

*Note: A word is defined as a character sequence consists of non-space characters only.*

**Example:**

Given s = "Hello World",

return 5 as length("World") = 5.

*Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.*




Solution:
def lengthOfLastWord(string):
	counter = 0
	for x in range(len(string)-1, -1, -1):
		if string != " ":
			counter += 1
		if A[x] == " " and counter > 0:
            break
	return counter




Process:
example 1

s = "hello world"

output = 5


example 2

s = "my name alex e"

output = 1


example 3

s = "alex"

output = 0


we start from the back of the string since we want the last word. 
we start counting all the letters until we come across a space. make sure that we have atleast counter 1 character before we break because ther can be a space before we get to a character. 


create a counter variable as zero

for loop through the string, starting at the end of the string

	if the current element is a letter

		increment the counter variable

	if its not but the counter is greater than zero then break

return the counter











