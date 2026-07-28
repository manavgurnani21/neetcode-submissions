class Solution:
    def calculateEatingSpeed(self, piles: List[int], proposed_k: int) -> int:
        # calculate the number of hours given a set of piles and a theoretical rate
        # use ceiling division
        numHours = 0
        for pile in piles:
            numHours += math.ceil(pile / proposed_k)
        
        return numHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # simple logic for searching for the right value
        # start with lo = 1, hi = max(piles)
        l = 1
        r = max(piles)

        min_k = r
        # then for each midpoint, find eating hours
        while l <= r:
            mid_k = (l + r) // 2
            # if <= h, then change hi to k - 1 (no point searching ahead) and update min
            if self.calculateEatingSpeed(piles, mid_k) <= h:
                r = mid_k - 1
                min_k = min(min_k, mid_k)
            # else, change lo to k + 1
            else:
                l = mid_k + 1
            # repeat whole process till lo > hi
        
        return min_k