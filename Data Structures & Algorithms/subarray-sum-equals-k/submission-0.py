class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sliding window with hashmap to keep track of our prefix sums and count
        # to get to a certain sum, can we subtract the prefixSum to obtain the sum? and how many subarrays can do so

        # loop through nums
            # add currentNum to currentSum
            # diff = currentSum - k
            # if diff is in the map, add that count to our res -- note we are NOT updating the map here with diff
            # add our currentSum to our map or increment if it exists
        res = 0
        currentSum = 0

        # base case of {0 : 1}, because 3-3 = 0, we want that to be technically an option too
        # note remembver its colon, not a comma, a comma would init it as a set(), not a dict{}
        prefixSum = { 0 : 1}

        for n in nums:
            currentSum += n
            diff = currentSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1
        return res