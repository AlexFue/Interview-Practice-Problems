Problem:
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.





Solution:
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums # create class variable for heap 
        self.k = k # create class variable for kth element 
        heapq.heapify(self.heap) # turn nums to a minheap 
        while k < len(self.heap): # pop extra smallest nums if heap length > k
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k: # if heap doesnt have kth num, its too small, so add the val
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]: # if heap does have kth num, check if val is greater to pop kth num and add val 
            heapq.heapreplace(self.heap, val)
        return self.heap[0] # return first val in heap because its always the kth num




Process:
The way we are going to solve this problem is with heaps.

Since we want teh kth largest number, we can convert the list to a min heap of size k. 
We can pop all the smaller numbers before the kth largest element so then the first element in the heap will always be the kth. 


When we add a number we have 2 cases to check. 
If our heap is not at length k, then we do not have a kth largest num so we add the value. 
If our heap is at length k, we check if its greater than the kth num because in that case, it would be inserted to the right and so we would have a new kth num. 
	- Do this process we would replace the kth num with the new num and adjust the heap if needed
After everything, return the first element which is always the kth element, or the closest to the kth if the heap is still small and doesnt have a kth yet. 





