class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABABBA 
        # windowLen - count[B] <-- count of most freq char
        # window is valid while windowLen - count[B] <= 2
        # max_freq
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            # check for invalid window
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            # for every valid window
            res = max(res, (r - l + 1))
        return res