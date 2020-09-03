Problem:
Given two strings s and t , write a function to determine if t is an anagram of s.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false





Solution:
def valid_anagram(s,t):
  return sorted(s) == sorted(t)




Process:
an anagram is rewording a word to make another, so we can sort the strings so that both have the characters in the same place and then test if they are equal 
if the strings are not exactly the same then they are not anagrams because again, anagrams have to have the same characters


sort both of the strings and see if they are equal to eachother, if they are then they are anagrams