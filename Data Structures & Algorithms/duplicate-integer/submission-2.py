class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countmap = {}
        for num in nums:
            if num not in countmap:
                countmap[num] = 1
            else:
                return True
        return False