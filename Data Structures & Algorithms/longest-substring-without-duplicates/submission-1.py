class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # set to keep track of duplicate chars, set contains all the unique chars in current substring
        # shrink from the left until there are no more duplicate chars in the set, aka no more dupes in current substring
        # return longest substring


        # init phase
        char_set = set()
        longest = 0
        left = 0
        # we dont need ot initialize right pointer, that will be kept track of when we loop through s

        for r in range(len(s)):
            curr_char = s[r]
            while curr_char in char_set:
                # remove left from set
                char_set.remove(s[left])
                left += 1
            char_set.add(curr_char)
            longest = max(longest, r - left + 1)
        return longest

