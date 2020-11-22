Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]




Solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        
        for s in strs:
            l = ''.join(sorted(s))
            if l in d:
                d[l] += [s]
            else:
                d[l] = [s]
            
        return [g for g in d.values()]




Process: 
The way we are going to solve this problem is with a dictionary
We create a dictionary to store all the groups of anagrams. Basically we loop through each string in the strs list, 
and we sort each string in a variable. We do this so we can use the it as a key in the dictionary, and have the anagram groups as the values. This is an easier way to check if a string belongs into a group. And if there is no group for it, we can make one. You may wonder wonder why we insert the sorted string in a set of []. well this 
keeps the elements of the string together becaue without it, the characters of the string are seperated. 

1.) Dictionary: 
    - to store anagram groups and sort them. 
    
2.) Loop through the strs list: 
    a.) Sort the current string into a variable to use it as a key in the dictionary
    b.) check if the sorted string group is already in the dictionary
        - if it is then add the nonsorted string into the group 
    c.) if not then create a group for it and add the nonsorted string
    
3.) loop through the values of the dictionary and add them into one list to return 




