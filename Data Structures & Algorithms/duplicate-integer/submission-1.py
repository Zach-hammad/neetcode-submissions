class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = list(set(nums))
        if len(list1) == len(nums):
            return False
        else:
            return True
