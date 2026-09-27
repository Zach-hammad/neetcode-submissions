class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        compliment = 0
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in dic:
                return [dic[compliment], i]
            dic[num] = i
        return
            
            


