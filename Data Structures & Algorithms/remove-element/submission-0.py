class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                k-=1
        nums.sort()
        print(nums[0:k])
        return k