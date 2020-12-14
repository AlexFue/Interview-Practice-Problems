Problem:
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

 

Example 1:

Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.




***Reservoir Solution***
Solution:
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """   
        cur = self.head # pointer to head
        result = 0 # the returning value 
        divisor = 1 # the divisor when trying to chose a number randomly
        while cur:
            if random.random() < (1/divisor): # checks to see if we got the node randomly, given the current number of nodes 
                result = cur.val # sets it if we got the node 
            cur = cur.next #moves to next node 
            divisor += 1 # increments divisor for next nodes if there are any 
        
        return result 




Process:
The way this problem works is by using reservoir sampling.
Basically, whenever you have a group of things, the chances of you getting something is 1 out of 
the total number of things there are. So there is 5 balls, you have a 1/5 chance of getting each at 
random. 
So for this problem, we want to be able to get all things equally at random, so we use reservoir sampling. 
What we can do is loop through each node and generate a random number 0 - 1 and we chose that node if our random number is less than 1 out of the total number of nodes we have seen. 
So if we are at node 3 and we get a number less than 1/3, that means we picked it randomly and choose it as the one to pick if we do not pick another as we go through the linked list. 




***Less Efficient Solution***
Solution:
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        r = random.randint(0,len(self.nums)-1)
        return self.nums[r]




Process: 
This solution works by storing all node values into a list and randomly picking one with random number generator 



