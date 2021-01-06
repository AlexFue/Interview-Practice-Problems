Problem:
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
 

Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.




Solution:
import collections
class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list) # create a dictionary of lists
        

    def set(self, key, value, timestamp):
        self.map[key].append((timestamp, value)) # adds value/timestamp to the dictionary value of the key 
        

    def get(self, key, timestamp):
        values = self.map[key] # gets all the values/timestamps of the key
        if not values: return '' # if key doesnt exist, return ''
        left, right = 0, len(values) - 1 # get left/right points for binary search of key values
        while left < right:
            mid = (left + right + 1) // 2 # get the middle value of values list
            pre_time, value = values[mid] # get theh pretimestamp and value 
            if pre_time > timestamp: # if pretimestamp is greater than timestamp, move right pointer left 
                right = mid - 1
            else: # if pretimestamp is less than timestamp, move left pointer right 
                left = mid
        return values[left][1] if values[left][0] <= timestamp else '' # return the lasting value if the pretimestamp <= timestamp, else return ''




Process:
The way we are going to solve this problem is with dictionaries and binary search


We use a dictionary as a way to store the items. 
Use the key as the dictionary key and the value/timestamp in a tuple as a dictionary value 
For items that have the same key, add them to the already existing key in the dictionary but as another tuple in the dictionary value 


To get an item we can use binary search since the items are added in ascending timestamp order to the dictionary
If key does not exist or if previous timestamp is great than the current timestamp we are trying to get, return ''

