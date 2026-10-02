class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
                r += 1
            else:
                r+=1
        return l+1
            