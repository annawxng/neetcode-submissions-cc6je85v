class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find the max pile - loop through and find the max => O(n)
        # from 1 - max, bianry search and figure out what the minimum k value is
        max_b = max(piles)
        
        left = 1
        right = max_b
        min_k = float("inf")
        while left <= right:
            # find potential k
            pot_k = (left + right) // 2
            # calculate total # of hours koko takes to eat all piles
            total_hours = 0
            for bans in piles:
                total_hours += (bans + pot_k - 1) // pot_k
            # if total hours > h -- koko is too slow
            # if total hours <= h -- koko is fast enough - try slower
            if total_hours > h:
                left = pot_k + 1
            else:
                right = pot_k - 1
                min_k = min(pot_k, min_k)
        return min_k