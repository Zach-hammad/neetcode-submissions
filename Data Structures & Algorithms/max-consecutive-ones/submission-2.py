class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        lst = []
        for i in nums:
            if i == 1:
                count+=1
                lst.append(count)
            else:
                lst.append(count)
                count = 0
        return max(lst)

