# Idea: 
# Store numbers in a hash table, 
# Hash: (key, value) = (num, index) 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Dic = {}

        for i, value in enumerate(nums):
            # check if value already in hash
            if value in Dic.keys():
                return([Dic[value], i]) 
            else:  
                    Dic[target - value] = i
            
            

# 
nums = [2,7,11,15]
target = 9
# 
# nums = [3,2,4]
# target = 6
sol = Solution()
print(sol.twoSum(nums, target))