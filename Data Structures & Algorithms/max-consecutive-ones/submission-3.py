class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        longest = 0
        for i in nums:
            if i == 1:
                count+=1
                longest = max(longest, count)
            else:
                count = 0
        return longest

