Problem:
Implement the RandomizedSet class:

bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
Follow up: Could you implement the functions of the class with each function works in average O(1) time?

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.




Solution:
import random
class RandomizedSet:
    def __init__(self):
        self.l = []
        self.d = {}
        

    def insert(self, val: int) -> bool:
        if val in self.d: 
            return False
        else: 
            self.d[val] = len(self.l)
            self.l.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.d:
            
            index_of_val = self.d[val]
            last_elem = self.l[-1]
            
            self.l[index_of_val] = last_elem
            self.l[-1] = val
            self.l.pop()
            
            self.d[last_elem] = index_of_val
            self.d.pop(val)
            
            
            return True 
        
        else: 
            return False

    def getRandom(self) -> int:
        r = random.randint(0,len(self.l)-1)
        return self.l[r]




Process:
he way we are going to solve this problem is with a list and a dictionary.
We create a list to store all the elements and a dictionary for checking if an elements is there because we can do it in O(1) time. In the insert function we use the dictionary to check if the value in inside, 
if not then we add it to both the list and dictionary, but in the dictionary we store the index of where it is as the value. In the remove function we also use the dictionary to check if it is inside. If it is 
then we are going to switch places of the last element of the list with the value we want to remove because we can just pop it(the value thats now at the end) in O(1). Also make sure to change the index of the num you moved in your dictionary and also pop the value there. Lastly in the random function we 
use the random int function to get a random number and return it

1.) init: 
    - create a list, to store the values
    - create a dictionary. to store the values and their indexes in the list
    
2.) insert:
    a.) check if the val is in the dictionary
        - if it is then return False
    b.) if not then add it to both the dictionary and then the list, return True
    
3.) remove: 
    a.) check if the value is in the dictionary 
        - get the index of the value we want to remove 
        - get the element at the end of list that we want to switch 
        
        - switch their places, the end element goes where the removing one is and the removing one goes
          where the end element was
            
        - change the index of last element that is now moved to where the removing one was
        
        - pop the last element of the list (the element that we want to remove)
        - pop the element that we want to remove from the dictionary 
        - return true
    b.) if value not in list then return false 
        
4.) random value 
    a.) use random int function to get a random number from 0 to the size of the list-1 and return it


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

