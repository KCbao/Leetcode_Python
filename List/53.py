# idea: new added number is negative, then cursum start from next num
# if a positive, then update cursum
# main idea, maxsubarray must start and end with positives, o/w can always reduce size to get a larger sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxsum, cursum = nums[0], nums[0]
        for i in nums[1:]:
            cursum = max(i, cursum+i)
            maxsum = max(maxsum,cursum)
        return maxsum
                
                