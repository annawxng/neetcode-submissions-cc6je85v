class HitCounter:

    def __init__(self):
        self.times = [0] * 300 # timestamp at idx i
        self.count = [0] * 300 # count at idx i


    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.times[idx] == timestamp:
            self.count[idx] += 1
        else:
            self.times[idx] = timestamp
            self.count[idx] = 1
         
 
    def getHits(self, timestamp: int) -> int:
        # exmaple get400
        total = 0
        #we only want to count 101-300, (300-101 + 1 = 400)
        for i in range(300):
            if self.times[i] > (timestamp - 300):
                total += self.count[i]
        return total




# times: 1:1, 2:2, 3:3
# count: 1:1  2:1, 3:2,

# HitCounter hitCounter = new HitCounter();
# hitCounter.hit(1);       // hit at timestamp 1.
# hitCounter.hit(2);       // hit at timestamp 2.
# hitCounter.hit(3);       // hit at timestamp 3.
# hitCounter.hit(3);       // hit at timestamp 3.
# hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
# hitCounter.hit(73);     // hit at timestamp 73
# hitCounter.hit(300);     // hit at timestamp 300.
# hitCounter.getHits(300); // get hits at timestamp 300, return 4.
# hitCounter.getHits(301); // get hits at timestamp 301, return 3.
# hitCounter.hit(373);     // hit at timestamp 373.
# hitCounter.getHits(400);     


        

# hint: fixed size array of 300
# for each index 0 - 299, of this array, would represents seconds 1 - 300
# arr[3] would give u hits at second idx + 1, or second 4

# u cannot do like hit[73] after specifying gethits(301), u can just shift the window then

#maybe our array of elemnets can have: timestamp: hits,
#  but then wouldnt we have to loop throuhg our entire array and decrement the hits by 1 if we slide our window from 1-300 to 2-301??

# hint: use 2 arrays of size 300 - one array stores timestamp
# the other array stores the count of hits at that specific seecond


# arr1[300] = 1-300
# arr2[300] = 1, 2, 3, 4

# hit



# so my idea with the grping by index was correct, i would just do % 300 instead of dividing by 301

        
# brute force, store every single timestamp with its number of hits
# 301 - 300 = 1, , so it owuld be
# mp[301] - mp[1],which would be 4 - 1 = 3, 

# ok im having a hard time figuring out how to do the sliding window thing...

# smth to keep track of hits for a certain timestamp

# past 300 sec range only, need buckets of 300
# brute force: for each timestamp, keep track of the current number of hits
# 1:1, 2:2, 3:3, 4:3, 300:1
# sliding window?  to keep track of the 300 sec

# HitCounter hitCounter = new HitCounter();
# hitCounter.hit(1);       // hit at timestamp 1.
# hitCounter.hit(2);       // hit at timestamp 2.
# hitCounter.hit(3);       // hit at timestamp 3.
# hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
# hitCounter.hit(300);     // hit at timestamp 300.
# hitCounter.getHits(300); // get hits at timestamp 300, return 4.
# hitCounter.getHits(301); // get hits at timestamp 301, return 3.
# hitCounter.hit(42);       // hit at timestamp 42.
# hitCounter.getHits(70); // get hits at timestamp 70, return 5

# divide into brackets of 300, or, maybe do % 300?

# 72 / (300 + 1)= 0
# 320 / 300 + 1 = 1
# 623 / 300 + 1 = 2
# 600 / 300 + 1 = 1
# then keep track of each hits for each index, in a mp
# 0:4, 1:3, ==> 0:5 

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)