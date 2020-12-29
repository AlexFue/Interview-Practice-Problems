Problem:
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?






Solution:
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = [] # stack to store timestamps
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.ts.append(timestamp) # adding each timestamp to back of stack since times increase
        

    def getHits(self, timestamp: int) -> int: # we index through the queue by popping the elements in the front
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.ts: # loop while we have timestamps in stack
            diff = timestamp - self.ts[0] # get the difference from the beginning timestamp of stack, to the given timestamp 
            if diff >= 300: self.ts.pop(0) # checks if our current queue meets theh 5 minute requirement range, if not then pop the smallest timestamp 
            else: break # breaks if the queue meets the 5 minute range
        
        return len(self.ts) # returns the length since each timestamp is 1 hit




Process:
The way we solve this problem is by using a queue. 

We store the timestamps in the queue since each timestamp gets increasingly bigger. 

When we want to get theh hits at a certain timestamp, it says we should get the number of hits 5 minutes within the timestamp. 
5 minutes is 300 seconds so we should get the hits starting from somewhere in the queue, to the timestamp to get 300 range. 

To do that we can calculate the difference from the start timestamp of the queue to the given timestamp. 
If the difference is greater, then move on to the next timestamp in the queue. 
But if its less than 300, within 5 minutes, then we found the last 5 minutes so return the num of hits which is the range. 



