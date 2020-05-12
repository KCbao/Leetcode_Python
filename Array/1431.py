class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandle = max(candies)
        return [item >= maxcandle-extraCandies for item in candies]
        