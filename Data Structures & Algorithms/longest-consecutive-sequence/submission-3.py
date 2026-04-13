class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find starts: for each num x, if x-1 is not in set, that is starter
            # if x-1 is in set, skip / continue until u find a start
            # once u find a starter, start counting
             # while (x-1, x-2, x-3 etc) exist in set, increase curr_max
                # compare curr_max with longest
        if not nums:
            return 0
        num_set = set()
        longest = 1
        for num in nums:
            num_set.add(num)
        for num in num_set:
            if num - 1 not in num_set:
                curr_max = 1
                counter = 1
                while (num + counter) in num_set:
                    curr_max += 1
                    counter += 1
                longest = max(longest, curr_max)
        return longest
