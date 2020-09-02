Problem:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Examples:
"Race Car" # returns 1

"Race a Car" # returns 0

"otto" # returns 1

"A man, a plan, a canal, Panama." # returns 1




Solution:
def isPalindrome(word):
    temp = ''
    for x in range(len(word)):
        if word[x].isalpha():
            temp += word[x].lower()
    if temp == temp[::-1]:
        return 1
    return 0




Process:
so we can add only all the letters of the word into a new string since that is all we care about. 
once we have the new string, then just check if it is the same backwards (which is what a palindrome is) by reverse indexing


word has to be the same backwords, ignoring not letter characters and caps

loop through the original word

	if the character is a letter, add all letters to another variable, ignoring caps

if the variable is the same as it is backwards then its a palindrome